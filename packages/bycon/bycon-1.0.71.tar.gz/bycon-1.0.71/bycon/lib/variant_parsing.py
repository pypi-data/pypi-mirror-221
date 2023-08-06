import bson.objectid

from cgi_parsing import *
from query_execution import mongo_result_list

################################################################################

def parse_variants(byc):
    __parse_variant_parameters(byc)
    __get_variant_request_type(byc)


################################################################################

def __parse_variant_parameters(byc):
    v_d = byc["variant_parameters"]
    v_p_defs = v_d["parameters"]
    v_t_defs = byc["variant_type_definitions"]

    variant_pars = { }

    for p_k in v_p_defs.keys():
        v_default = None
        if "default" in v_p_defs[ p_k ]:
            v_default = v_p_defs[ p_k ][ "default" ]
        variant_pars[ p_k ] = v_default
        if p_k in byc["form_data"]:
            variant_pars[ p_k ] = byc["form_data"][p_k]

        if variant_pars[ p_k ] is None:
            variant_pars.pop(p_k)

    # value checks
    v_p_c = { }
    translate_reference_name(variant_pars, byc)

    for p_k in variant_pars.keys():
        if not p_k in v_p_defs.keys():
            continue
        v_p = variant_pars[ p_k ]
        if "variant_type" in p_k:
            v_s = variant_state_from_variant_par(v_p, byc)
            if v_s is False:
                v_p_c[ p_k ] = None
            else:
                v_s_id = v_s["id"]  # on purpose here leading to error if ill defined
                v_p_c[ p_k ] = { "$in": v_t_defs[v_s_id]["child_terms"] }
        elif "array" in v_p_defs[ p_k ]["type"]:
            v_l = set()
            for v in v_p:
                if re.compile( v_p_defs[ p_k ][ "items" ][ "pattern" ] ).match( str( v ) ):
                    if "integer" in v_p_defs[ p_k ][ "items" ][ "type" ]:
                        v = int( v )
                    v_l.add( v )
            v_p_c[ p_k ] = sorted( list(v_l) )
        else:
            if re.compile( v_p_defs[ p_k ][ "pattern" ] ).match( str( v_p ) ):
                if "integer" in v_p_defs[ p_k ][ "type" ]:
                    v_p = int( v_p )
                v_p_c[ p_k ] = v_p

    byc.update( { "variant_pars": v_p_c } )


################################################################################

def __get_variant_request_type(byc):

    """podmd
    This method guesses the type of variant request, based on the complete
    fulfillment of the required parameters (all of `all_of`, one if `one_of`).
    In case of multiple types the one with most matched parameters is prefered.
    This may be changed to using a pre-defined request type and using this as
    completeness check only.
    TODO: Verify by schema ...
    podmd"""

    if not "variant_pars" in byc:
        return

    variant_request_type = "no correct variant request"

    v_pars = byc["variant_pars"]
    v_p_defs = byc["variant_parameters"]["parameters"]

    brts = byc["variant_parameters"]["request_types"]
    brts_k = brts.keys()
    
    # DODO HACK: setting to range request if start and end with one value
    if "start" in v_pars and "end" in v_pars:
        if len(v_pars[ "start" ]) == 1:
            if len(v_pars[ "end" ]) == 1:
                brts_k = [ "variantRangeRequest" ]

    vrt_matches = [ ]

    for vrt in brts_k:

        matched_par_no = 0
        needed_par_no = 0
        if "one_of" in brts[vrt]:
            needed_par_no = 1
            for one_of in brts[vrt][ "one_of" ]:
                if one_of in v_pars:
                    matched_par_no = 1
                    continue
        
        if "all_of" in brts[vrt]:
            needed_par_no += len( brts[vrt][ "all_of" ] )

            for required in brts[vrt][ "all_of" ]:
                if required in v_pars:
                    matched_par_no += 1
        
        # print("{} {} of {}".format(vrt, matched_par_no, needed_par_no))

        if matched_par_no >= needed_par_no:
            vrt_matches.append( { "type": vrt, "par_no": matched_par_no } )


    if len(vrt_matches) > 0:
        vrt_matches = sorted(vrt_matches, key=lambda k: k['par_no'], reverse=True)
        variant_request_type = vrt_matches[0]["type"]

    byc.update( { "variant_request_type": variant_request_type } )


################################################################################

def variant_state_from_variant_par(variant_type, byc):
    v_d = byc["variant_parameters"]
    v_t_defs = byc["variant_type_definitions"]

    for k, d in v_t_defs.items():
        for p, v in d.items():
            if v is None:
                continue
            if type(v) is list:
                continue
            if "variant_state" in p:
                v = v.get("id", "___none___")
            if type(v) is not str:
                continue
            if variant_type.lower() == v.lower():
                return d["variant_state"]

    return False


################################################################################

def variant_vcf_type_from_variant_par(variant_type, byc):
    v_d = byc["variant_parameters"]
    v_t_defs = byc["variant_type_definitions"]

    for k, d in v_t_defs.items():
        for p, v in d.items():
            if v is None:
                continue
            if type(v) is list:
                continue
            if "variant_state" in p:
                v = v.get("id", "___none___")
            if type(v) is not str:
                continue
            if variant_type.lower() == v.lower():
                return d.get("VCF")

    return False


################################################################################

def translate_reference_name(variant_pars, byc):

    if not "reference_name" in variant_pars:
        return variant_pars

    r_n = variant_pars[ "reference_name" ]
    g_a = byc.get("genome_aliases", {})
    r_a = g_a.get("refseq_aliases", {})

    if not r_n in r_a.keys():
        variant_pars.pop("reference_name")
        return variant_pars

    variant_pars.update({"reference_name": r_a[r_n] })

    return variant_pars



################################################################################

def create_variantTypeRequest_query( byc ):

    if byc["variant_request_type"] != "variantTypeRequest":
        return

    """
    A query just for a variant type w/o any additional parameter has to be blocked
    due to size concerns.
    Queries with additional parameters (start ...) will be handled through other
    query types.
    """

    if len(byc.get("filters", [])) < 1:
        return

    vp = byc["variant_pars"]
    v_p_defs = byc["variant_parameters"]["parameters"]

    v_q_l = [
        { v_p_defs["variant_type"]["db_key"]: vp[ "variant_type" ] }
    ]

    if "reference_name" in vp:
        v_q_l.append( { v_p_defs["reference_name"]["db_key"]: vp[ "reference_name" ] })

    if len(v_q_l) == 1:
        v_q = v_q_l[0]
    else:     
        v_q = { "$and": v_q_l }

    expand_variant_query(v_q, byc)

################################################################################

def create_variantIdRequest_query( byc ):

    if byc["variant_request_type"] != "variantIdRequest":
        return

    # query database for gene and use coordinates to create range query
    vp = byc["variant_pars"]
    v_p_defs = byc["variant_parameters"]["parameters"]

    if "_id" in vp:
        v_q = {v_p_defs["_id"]["db_key"] : bson.objectid.ObjectId(vp["_id"])}
    elif "id" in vp:
        v_q = { 
            "$or": [
                {v_p_defs["_id"]["db_key"] : bson.objectid.ObjectId(vp["id"])},
                { v_p_defs["id"]["db_key"] : vp[ "id" ] }
            ]
        }
    else:
        return

    expand_variant_query(v_q, byc)

################################################################################

def create_geneVariantRequest_query( byc ):

    if byc["variant_request_type"] != "geneVariantRequest":
        return

    # query database for gene and use coordinates to create range query
    vp = byc["variant_pars"]
    v_p_defs = byc["variant_parameters"]["parameters"]


    query = { "symbol" : vp[ "gene_id" ] }

    results, error = mongo_result_list( "progenetix", "genes", query, { '_id': False } )

    # Since this is a pre-processor to the range request
    byc["variant_pars"].update( {
        "reference_name": "refseq:{}".format(results[0]["accession_version"]),
        "start": [ results[0]["start"] ],
        "end": [ results[0]["end"] ]
    } )

    # translate_reference_name(byc["variant_pars"], byc)
    byc.update( {"variant_request_type": "variantRangeRequest"} )
    create_variantRangeRequest_query( byc )

################################################################################

def create_variantAlleleRequest_query( byc ):

    """podmd
 
    podmd"""

    if byc["variant_request_type"] != "variantAlleleRequest":
        return

    vp = byc["variant_pars"]
    v_p_defs = byc["variant_parameters"]["parameters"]

    # TODO: Regexes for ref or alt with wildcard characters

    v_q_l = [
        { v_p_defs["reference_name"]["db_key"]: vp[ "reference_name" ] },
        { v_p_defs["start"]["db_key"]: int(vp[ "start" ][0]) }
    ]
    for p in [ "reference_bases", "alternate_bases" ]:
        if not vp[ p ] == "N":
            if "N" in vp[ p ]:
                rb = vp[ p ].replace("N", ".")
                v_q_l.append( { v_p_defs[p]["db_key"]: { '$regex': rb } } )
            else:
                 v_q_l.append( { v_p_defs[p]["db_key"]: vp[ p ] } )
        
    v_q = { "$and": v_q_l }

    expand_variant_query(v_q, byc)

################################################################################

def create_variantCNVrequest_query( byc ):

    if not byc["variant_request_type"] in [ "variantCNVrequest" ]:
        return

    vp = byc["variant_pars"]
    v_p_defs = byc["variant_parameters"]["parameters"]

    v_q = { "$and": [
        { v_p_defs["reference_name"]["db_key"]: vp[ "reference_name" ] },
        { v_p_defs["start"]["db_key"]: { "$lt": vp[ "start" ][-1] } },
        { v_p_defs["end"]["db_key"]: { "$gte": vp[ "end" ][0] } },
        { v_p_defs["start"]["db_key"]: { "$gte": vp[ "start" ][0] } },
        { v_p_defs["end"]["db_key"]: { "$lt": vp[ "end" ][-1] } },
        create_in_query_for_parameter("variant_type", v_p_defs["variant_type"]["db_key"], vp)
    ]}

    expand_variant_query(v_q, byc)

################################################################################

def create_variantRangeRequest_query( byc ):

    if not byc["variant_request_type"] in [ "variantRangeRequest" ]:
        return
    
    vp = byc["variant_pars"]
    v_p_defs = byc["variant_parameters"]["parameters"]

    v_q_l = [
        { v_p_defs["reference_name"]["db_key"]: vp[ "reference_name" ] },
        { v_p_defs["start"]["db_key"]: { "$lt": int(vp[ "end" ][-1]) } },
        { v_p_defs["end"]["db_key"]: { "$gt": int(vp[ "start" ][0]) } }
    ]

    p_n = "variant_min_length"
    if p_n in vp:
        v_q_l.append( { v_p_defs[p_n]["db_key"]: { "$gte" : vp[p_n] } } )
    p_n = "variant_max_length"
    if "variant_max_length" in vp:
        v_q_l.append( { v_p_defs[p_n]["db_key"]: { "$lte" : vp[p_n] } } )

    p_n = "variant_type"
    if p_n in vp:
        v_q_l.append( create_in_query_for_parameter(p_n, v_p_defs[p_n]["db_key"], vp) )
    elif "alternate_bases" in vp:
        # the N wildcard stands for any length alt bases so can be ignored
        if vp[ "alternate_bases" ] == "N":
             v_q_l.append( { v_p_defs["alternate_bases"]["db_key"]: {'$regex': "." } } )
        else:
            v_q_l.append( { v_p_defs["alternate_bases"]["db_key"]: vp[ "alternate_bases" ] } )

    v_q = { "$and": v_q_l }

    expand_variant_query(v_q, byc)

################################################################################

def expand_variant_query(variant_query, byc):

    if "variants" in byc["queries"]:
        byc["queries"].update({"variants": { "$and": [ byc["queries"]["variants"], variant_query ] } } )
    else:
        byc["queries"].update( {"variants": variant_query } )

################################################################################

def create_and_or_query_for_list(logic, q_list):

    if not isinstance(q_list, list):
        return q_list

    if not q_list:
        return {}

    if len(q_list) > 1:
        return { logic: q_list }

    return q_list[0]

################################################################################

def create_in_query_for_parameter(par, qpar, q_pars):

    if not isinstance(q_pars[ par ], list):
        return { qpar: q_pars[ par ] }

    try:
        q_pars[ par ][0]
    except IndexError:
        return { }
 
    if len(q_pars[ par ]) > 1:
        return { qpar: {"$in": q_pars[ par ]} }

    return { qpar: q_pars[ par ][0] }

################################################################################

def variant_create_digest(v, byc):

    # TODO: remove / part of ByconVariant

    t = v["variant_state"]["id"]
    t = re.sub(":", "_", t)

    v_i = v["location"]
    return f'{v_i["chromosome"]}:{v_i["start"]}-{v_i["end"]}:{t}'

################################################################################

def chroname_from_refseqid(refseqid, byc):

    chr_re = re.compile(r'^refseq:NC_0+([^0]\d?)\.\d\d?$')
    chro = chr_re.match(refseqid).group(1)

    return chro

################################################################################

def normalize_pgx_variant(variant, byc, counter=1):
    g_a = byc.get("genome_aliases", {})
    r_a = g_a.get("refseq_aliases", {})
    c_a = g_a.get("chro_aliases", {})
    v_t_defs = byc["variant_type_definitions"]
    errors = []

    var_id = variant.get("id", counter)

    seq_id = variant["location"].get("sequence_id")
    chromosome = variant["location"].get("chromosome")
    start = variant["location"].get("start")
    end = variant["location"].get("end")
    if not seq_id:
        if chromosome:
            variant["location"].update({"sequence_id": r_a.get(str(chromosome))})
    if not chromosome:
        if seq_id:
            variant["location"].update({"chromosome": c_a.get(str(seq_id))})
    if not isinstance(end, int):
        try:
            ref = variant.get("reference_sequence")
            alt = variant.get("sequence")
            v_l = len(ref) - len(alt)
            end_pos = start + abs(v_l) + 1
            # TODO: VRS would do a left-clipping -> start shift ...
            variant["location"].update({"end": end_pos})
        except:
            pass

    # TODO: Some fixes ...
    if "-" in variant.get("sequence", "."):
        variant["sequence"] = re.sub("-", "", variant["sequence"])
    if "-" in variant.get("reference_sequence", "."):
        variant["sequence"] = re.sub("-", "", variant["reference_sequence"])

    var_state_id = variant["variant_state"].get("id")
    variant_type = variant.get("variant_type")
    if not var_state_id:
        if variant_type:
            variant.update({ "variant_state": variant_state_from_variant_par(variant_type, byc) })

    try:
        variant["variant_state"].update({"label": v_t_defs[var_state_id].get("label")})
    except:
        pass


    for v_l_k in [ "sequence_id", "chromosome", "start", "end" ]:
        if not variant["location"].get(v_l_k):
            errors.append(f'¡¡¡ Parameter `location.{v_l_k}` undefined in variant {var_id} !!!')
    for v_s_k in [ "id", "label" ]:
        if not variant["variant_state"].get(v_s_k):
            errors.append(f'¡¡¡ Parameter `variant_state.{v_s_k}` undefined in variant {var_id} !!!')

    return variant, errors

################################################################################
