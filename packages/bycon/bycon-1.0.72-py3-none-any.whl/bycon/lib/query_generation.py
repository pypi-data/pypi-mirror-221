import pymongo
from bson import SON

from bycon_helpers import days_from_iso8601duration, paginate_list, set_pagination_range
from filter_parsing import *
from variant_parsing import *


################################################################################

def generate_dataset_queries(byc, ds_id):

    byc.update({"queries": {}})
    __update_queries_from_path_id(byc)
    __update_queries_from_id_values(byc)
    __update_queries_from_cohorts_query(byc)
    __update_queries_from_variants(byc)
    __update_queries_from_geoquery(byc)
    __update_queries_from_hoid(byc)
    __update_queries_from_filters(byc, ds_id)
    __replace_queries_in_test_mode(byc)
    __purge_empty_queries(byc)

    # TODO: HOT FIX
    if "runs" in byc["queries"].keys():
        if "callsets" not in byc["queries"].keys():
            byc["queries"]["callsets"] = byc["queries"].pop("runs")


################################################################################

def __purge_empty_queries(byc):
    empties = []
    for k, v in byc["queries"].items():
        if not v:
            empties.append(k)
    for e_k in empties:
        byc["queries"].pop(e_k, None)


################################################################################

def __replace_queries_in_test_mode(byc):
    if byc["test_mode"] is not True:
        return

    try:
        collname = byc["response_entity"]["collection"]
    except Exception:
        return

    ret_no = int(byc.get('test_mode_count', 5))

    ds_id = byc["dataset_ids"][0]
    mongo_client = pymongo.MongoClient(host=environ.get("BYCON_MONGO_HOST", "localhost"))
    data_db = mongo_client[ds_id]
    data_collnames = data_db.list_collection_names()

    if collname not in data_collnames:
        return

    data_coll = mongo_client[ds_id][collname]
    rs = list(data_coll.aggregate([{"$sample": {"size": ret_no}}]))

    _ids = []
    for r in rs:
        _ids.append(r["_id"])

    byc.update({
        "queries": {collname: {"_id": {"$in": _ids}}},
        "empty_query_all_count": data_coll.estimated_document_count()
    })


################################################################################

def __update_queries_from_path_id(byc):
    b_mps = byc["beacon_mappings"]

    if "service" in byc["request_path_root"]:
        b_mps = byc.get("services_mappings", byc["beacon_mappings"])

    if not byc["request_entity_id"]:
        return

    r_e_id = byc["request_entity_id"]
    p_id_v = byc["request_entity_path_id_value"]

    if not byc["request_entity_path_id_value"]:
        return

    if r_e_id not in b_mps["response_types"]:
        return

    collname = b_mps["response_types"][r_e_id]["collection"]

    if not collname:
        return

    byc["queries"].update({collname: {"id": p_id_v}})
    __id_query_add_variant_query(byc, r_e_id, p_id_v)


################################################################################

def __id_query_add_variant_query(byc, entity, entity_id):

    if entity not in ("biosample", "individual", "callset", "analysis", "run"):
        return

    v_q_id = f'{entity}_id'
    v_q_id = re.sub("analysis", "callset", v_q_id)
    v_q_id = re.sub("run", "callset", v_q_id)
    query = {v_q_id: entity_id}

    __update_query_for_scope(byc, query, "variants")


################################################################################

def __update_queries_from_cohorts_query(byc):
    if "cohorts" not in byc["queries"]:
        return

    if "cohort" in byc["response_entity_id"]:
        return

    c_q = byc["queries"]["cohorts"]

    query = {}
    if "id" in c_q:
        query = {"cohorts.id": c_q["id"]}

    byc["queries"].pop("cohorts", None)

    __update_query_for_scope(byc, query, "biosamples")


################################################################################

def __update_queries_from_id_values(byc):
    id_f_v = byc["beacon_mappings"]["id_queryscope_mappings"]
    form = byc["form_data"]

    r_e_id = byc.get("request_entity_id")
    this_id_k = r_e_id + "_ids"

    if "ids" in form and this_id_k not in form:
        form.update({this_id_k: form["ids"]})

    id_v_s = form.get(this_id_k, [])
    q = False
    if len(id_v_s) < 1:
        return
    elif len(id_v_s) == 1:
        q = {"id": id_v_s[0]}
        __id_query_add_variant_query(byc, r_e_id, id_v_s[0])
    elif len(id_v_s) > 1:
        q = {"id": {"$in": id_v_s}}

    if q is not False:
        __update_query_for_scope(byc, q, r_e_id)


################################################################################

def __update_queries_from_hoid(byc):
    if "accessid" in byc["form_data"]:

        accessid = byc["form_data"]["accessid"]
        ho_client = pymongo.MongoClient(host=environ.get("BYCON_MONGO_HOST", "localhost"))
        ho_db = ho_client[byc["config"]["housekeeping_db"]]
        ho_coll = ho_db[byc["config"]["handover_coll"]]
        h_o = ho_coll.find_one({"id": accessid})

        # accessid overrides ... ?
        if h_o:
            t_k = h_o["target_key"]
            t_v = h_o["target_values"]
            c_n = h_o["target_collection"]
            t_c = h_o["target_count"]

            byc.update({"original_queries": h_o.get("original_queries", None)})

            set_pagination_range(t_c, byc)
            t_v = paginate_list(t_v, byc)
            h_o_q = {t_k: {'$in': t_v}}
            if c_n in byc["queries"]:
                byc["queries"].update({c_n: {'$and': [h_o_q, byc["queries"][c_n]]}})
            else:
                byc["queries"].update({c_n: h_o_q})


################################################################################

def __update_queries_from_filters(byc, ds_id="progenetix"):
    """The new version assumes that dataset_id, scope (collection) and field are
    stored in the collation entries. Only filters with exact match to an entry
    in the lookup "collations" collection will be evaluated.
    While the Beacon v2 protocol assumes a logical `AND` between filters, bycon
    has a slightly differing approach:
    * filters against the same field (in the same collection) are treated as
    logical `OR` since this seems, well, logical (since otherwise the query would
    fail or result in incomplete matches in the case of terms from the same term
    tree); and also allows the use of the same query object for hierarchical
    (`child_terms`) query expansion
    * the `bycon` API allows to pass a `filterLogic` parameter with either a
    global `AND` (default value) or `OR`

    CAVE: Filters are assumed to be id values in the collation collection
    OR have a `collationed` flag in the filter_definitions set to `false`.

    TODO: The `excluded` query option currently will **not** positively match
    entries with an `excluded` flag (this is a specific Phenopackets construct
    for e.g. defining patients which have one phenotype _but not_ another one).
    """

    f_defs = byc["filter_definitions"]
    f_lists = {}

    logic = byc["filter_flags"]["logic"]
    f_desc = byc["filter_flags"]["descendants"]
    # precision = byc[ "filter_flags" ][ "precision" ]

    mongo_client = pymongo.MongoClient(host=environ.get("BYCON_MONGO_HOST", "localhost"))
    coll_coll = mongo_client[ds_id]["collations"]

    filters = byc.get("filters", [])

    f_infos = {}

    for f in filters:

        f_val = f["id"]
        f_neg = f.get("excluded", False)
        if re.compile(r'^!').match(f_val):
            f_neg = True
            f_val = re.sub(r'^!', '', f_val)

        f_desc = f.get("includeDescendantTerms", f_desc)
        f_scope = f.get("scope", False)

        f_info = coll_coll.find_one({"id": f_val})

        if f_info is None:

            for f_d in f_defs.values():
                f_re = re.compile(f_d["pattern"])
                if f_re.match(f_val):
                    f_info = {
                        "id": f_val,
                        "scope": f_d["scope"],
                        "db_key": f_d["db_key"],
                        "type": f_d.get("type", "ontology"),
                        "format": f_d.get("format", "___none___"),
                        "child_terms": [f_val]
                    }
                    f_desc = False
                    if f_d["collationed"] is True:
                        ftw = f'Filter `{f_val}` matches a `{f_d["scope"]}` pattern but is not in the list of existing `filtering_terms` for {ds_id}'
                        response_add_filter_warnings(byc, ftw)                        

        if f_info is None:
            f_info = {
                "id": f_val,
                "scope": "biosamples",
                "type": "___undefined___",
                "db_key": "___undefined___",
                "child_terms": [f_val]
            }

        if f_neg is True:
            f_info.update({"is_negated": True})

        f_field = f_info.get("db_key", "id")

        if f_scope is False:
            f_scope = f_info["scope"]

        if f_scope not in byc["config"].get("queried_collections", []):
            fsw = f'The scope `{f_scope}` for filter `{f_val}` is not in the queried models'
            response_add_filter_warnings(byc, fsw)

        if f_scope not in f_lists.keys():
            f_lists.update({f_scope: {}})
        if f_scope not in f_infos.keys():
            f_infos.update({f_scope: {}})

        if f_field not in f_lists[f_scope].keys():
            f_lists[f_scope].update({f_field: []})
        if f_field not in f_infos[f_scope].keys():
            f_infos[f_scope].update({f_field: f_info})

        # TODO: move somewhere; this is just for the age prototype
        if "alphanumeric" in f_info.get("type", "ontology"):
            f_class, comp, val = re.match(r'^(\w+):([<>=]+?)(\w[\w.]+?)$', f_info["id"]).group(1, 2, 3)
            if "iso8601duration" in f_info.get("format", "___none___"):
                val = days_from_iso8601duration(val)
            f_lists[f_scope][f_field].append(__mongo_comparator_query(comp, val))

        elif f_desc is True:
            if f_neg is True:
                f_lists[f_scope][f_field].append({'$nin': f_info["child_terms"]})
            else:
                f_lists[f_scope][f_field].extend(f_info["child_terms"])
        else:
            if f_neg is True:
                f_lists[f_scope][f_field].append({'$nin': [f_info["id"]]})
            else:
                f_lists[f_scope][f_field].append(f_info["id"])

    # creating the queries & combining w/ possible existing ones
    for f_scope in f_lists.keys():
        f_s_l = []
        for f_field, f_query_vals in f_lists[f_scope].items():
            if len(f_query_vals) == 1:
                f_s_l.append({f_field: f_query_vals[0]})
            else:
                if "alphanumeric" in f_infos[f_scope][f_field].get("type", "ontology"):
                    q_l = []
                    for a_q_v in f_query_vals:
                        q_l.append({f_field: a_q_v})
                    f_s_l.append({"$and": q_l})
                else:
                    f_s_l.append({f_field: {"$in": f_query_vals}})

        if f_scope in byc["queries"]:
            f_s_l.append(byc["queries"][f_scope])

        if len(f_s_l) == 1:
            byc["queries"].update({f_scope: f_s_l[0]})
        elif len(f_s_l) > 1:
            byc["queries"].update({f_scope: {logic: f_s_l}})


################################################################################

def __update_query_for_scope(byc, query, scope, bool_mode="AND"):
    logic = boolean_to_mongo_logic(bool_mode)

    if scope not in byc["queries"]:
        byc["queries"].update({scope: query})
    else:
        byc["queries"].update({scope: {logic: [byc["queries"][scope], query]}})


################################################################################

def __update_queries_from_geoquery(byc):
    geo_q, geo_pars = geo_query(byc)

    if not geo_q:
        return

    __update_query_for_scope(byc, geo_q, "biosamples", bool_mode="AND")


################################################################################

def __mongo_comparator_query(comparator, value):

    mongo_comps = {
        ">": '$gt',
        ">=": '$gte',
        "<": '$lt',
        "<=": '$lte',
        "=": '$eq'
    }

    c = mongo_comps.get(comparator, '$eq')

    return {c: value}

################################################################################


def __update_queries_from_variants(byc):
    if "variant_request_type" not in byc:
        return

    if byc["variant_request_type"] not in byc["variant_parameters"]["request_types"].keys():
        if "variants" not in byc["queries"]:
            return

    if "variantTypeRequest" in byc["variant_request_type"]:
        create_variantTypeRequest_query(byc)
    elif "variantIdRequest" in byc["variant_request_type"]:
        create_variantIdRequest_query(byc)
    elif "variantCNVrequest" in byc["variant_request_type"]:
        create_variantCNVrequest_query(byc)
    elif "variantAlleleRequest" in byc["variant_request_type"]:
        create_variantAlleleRequest_query(byc)
    elif "variantRangeRequest" in byc["variant_request_type"]:
        create_variantRangeRequest_query(byc)
    elif "geneVariantRequest" in byc["variant_request_type"]:
        create_geneVariantRequest_query(byc)


################################################################################
################################################################################
################################################################################

def geo_query(byc):
    geo_q = {}
    geo_pars = {}

    if "geoloc_definitions" not in byc:
        return geo_q, geo_pars

    g_p_defs = byc["geoloc_definitions"]["parameters"]
    g_p_rts = byc["geoloc_definitions"]["request_types"]
    geo_root = byc["geoloc_definitions"]["geo_root"]

    req_type = ""
    # TODO: Make this modular & fix the one_of interpretation to really only 1
    for rt in g_p_rts:
        g_p = {}
        min_p_no = 1
        mat_p_no = 0
        if "all_of" in g_p_rts[rt]:
            g_q_k = g_p_rts[rt]["all_of"]
            min_p_no = len(g_q_k)
        elif "one_of" in g_p_rts[rt]:
            g_q_k = g_p_rts[rt]["one_of"]
        else:
            continue

        # print(rt)
        # print(byc["form_data"]["filters"])
        all_p = g_p_rts[rt].get("any_of", []) + g_q_k

        for g_k in g_p_defs.keys():

            if g_k not in all_p:
                continue

            g_default = None
            if "default" in g_p_defs[g_k]:
                g_default = g_p_defs[g_k]["default"]

            # TODO: This is an ISO lower hack ...

            if g_k.lower() in byc["form_data"]:
                g_v = byc["form_data"][g_k.lower()]
            else:
                g_v = g_default
            if g_v is None:
                continue
            if not re.compile(g_p_defs[g_k]["pattern"]).match(str(g_v)):
                continue
            if "float" in g_p_defs[g_k]["type"]:
                g_p[g_k] = float(g_v)
            else:
                g_p[g_k] = g_v

            if g_k in g_q_k:
                mat_p_no += 1

        if mat_p_no < min_p_no:
            continue

        req_type = rt
        geo_pars = g_p

    if "city" in req_type:
        geo_q = return_geo_city_query(geo_root, geo_pars)
        return geo_q, geo_pars

    if "id" in req_type:
        geo_q = {"id": re.compile(geo_pars["id"], re.IGNORECASE)}
        return geo_q, geo_pars

    if "ISO3166alpha2" in req_type:
        geo_q = {"provenance.geo_location.properties.ISO3166alpha2": byc["form_data"]["iso3166alpha2"].upper()}
        return geo_q, geo_pars

    if "geoquery" in req_type:
        geoq_l = [return_geo_longlat_query(geo_root, geo_pars)]
        for g_k in g_p_rts["geoquery"]["any_of"]:
            if g_k in geo_pars.keys():
                g_v = geo_pars[g_k]
                if len(geo_root) > 0:
                    geopar = ".".join([geo_root, "properties", g_k])
                else:
                    geopar = ".".join(["properties", g_k])
                geoq_l.append({geopar: re.compile(r'^' + str(g_v), re.IGNORECASE)})

        if len(geoq_l) > 1:
            geo_q = {"$and": geoq_l}
        else:
            geo_q = geoq_l[0]

    return geo_q, geo_pars


################################################################################

def return_geo_city_query(geo_root, geo_pars):
    geoq_l = []

    for g_k, g_v in geo_pars.items():

        if len(geo_root) > 0:
            geopar = ".".join([geo_root, "properties", g_k])
        else:
            geopar = ".".join(["properties", g_k])

        geoq_l.append({geopar: re.compile(r'^' + str(g_v), re.IGNORECASE)})

    if len(geoq_l) > 1:
        return {"$and": geoq_l}
    else:
        return geoq_l[0]


################################################################################

def return_geo_longlat_query(geo_root, geo_pars):
    if len(geo_root) > 0:
        geojsonpar = ".".join((geo_root, "geometry"))
    else:
        geojsonpar = "geo_location.geometry"

    geo_q = {
        geojsonpar: {
            '$near': SON(
                [
                    (
                        '$geometry', SON(
                            [
                                ('type', 'Point'),
                                ('coordinates', [
                                    geo_pars["geo_longitude"],
                                    geo_pars["geo_latitude"]
                                ])
                            ]
                        )
                    ),
                    ('$maxDistance', geo_pars["geo_distance"])
                ]
            )
        }
    }

    return geo_q

################################################################################
