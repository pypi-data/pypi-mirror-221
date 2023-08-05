import base36
import time
import re
from isodate import parse_duration

################################################################################

def generate_id(prefix):
    time.sleep(.001)
    return '{}-{}'.format(prefix, base36.dumps(int(time.time() * 1000)))  ## for time in ms


################################################################################

def days_from_iso8601duration(iso8601duration):
    """A simple function to convert ISO8601 duration strings to days. This is
    potentially lossy since it does not include time parsing."""

    # TODO: check format
    is_isodate_duration = re.match(r'^P\d+?[YMD](\d+?[M])?(\d+?[D])?', iso8601duration)
    if not is_isodate_duration:
        return False

    duration = parse_duration(iso8601duration)
    days = 0
    try:
        days += int(duration.years) * 365.2425
    except AttributeError:
        pass
    try:
        days += int(duration.months) * 30.4167
    except AttributeError:
        pass
    try:
        days += int(duration.days)
    except AttributeError:
        pass

    return days


################################################################################

def hex_2_rgb( hexcolor ):

    rgb = [127, 127, 127]
    h = hexcolor.lstrip('#')
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    return rgb

################################################################################

def set_pagination_range(d_count, byc):
    r_range = [
        byc["pagination"]["skip"] * byc["pagination"]["limit"],
        byc["pagination"]["skip"] * byc["pagination"]["limit"] + byc["pagination"]["limit"],
    ]

    if byc["pagination"]["skip"] == 0 and byc["pagination"]["limit"] == 0:
        byc["pagination"].update({"range": [0, d_count]})
        return

    r_l_i = d_count - 1

    if r_range[0] > r_l_i:
        r_range[0] = r_l_i
    if r_range[-1] > d_count:
        r_range[-1] = d_count

    byc["pagination"].update({"range": r_range})


################################################################################

def paginate_list(this, byc):
    if byc["pagination"]["limit"] < 1:
        return this

    r = byc["pagination"]["range"]

    t_no = len(this)
    r_min = r[0] + 1
    r_max = r[-1]

    if r_min > t_no:
        return []
    if r_max > t_no:
        return this[r[0]:r_max]

    return this[r[0]:r[-1]]

