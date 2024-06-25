import re


def parse_int(value):
    num = re.findall(r"\d+", value)
    if len(num) > 0:
        return int(num[0])
    else:
        print("Error parsing int")
        return -1


def parse_float(value):
    num = re.findall(r"\d+\.\d+", value)
    if len(num) > 0:
        return float(num[0])
    else:
        print("Error parsing float")
        return -1.0


def parse_bool(value):
    if value == "True":
        return True
    else:
        return False


def parse_list(value):
    value = value[1:-1]
    return value.split(",")


def parse_dict(value):
    #todo: IMPLEMENT
    return value


def parse_tuple(value):
    value = value[1:-1]
    return tuple(value.split(","))


def parse_unknown_type(value):
    ints = re.findall(r"\d+", value)
    floats = re.findall(r"\d+\.\d+", value)
    bools = re.findall(r"True|False", value)
    lists = re.findall(r"\[.*,*\]", value)
    tuples = re.findall(r"\(.*,*\)", value)
    dicts = re.findall(r"\{.*,*\}", value)

    no_collections = len(lists) == 0 and len(tuples) == 0 and len(dicts) == 0
    val_type = ""
    if len(ints) > 0 and len(floats) == 0 and no_collections:
        val_type = "int"
    elif len(floats) > 0 and no_collections:
        val_type = "float"
    elif len(bools) > 0:
        val_type = "bool"
    elif len(lists) > 0:
        val_type = "list"
    elif len(tuples) > 0:
        val_type = "tuple"
    elif len(dicts) > 0:
        val_type = "dict"
    else:
        val_type = "string"

    match val_type:
        case "int":
            return parse_int(value)
        case "float":
            return parse_float(value)
        case "bool":
            return parse_bool(value)
        case "list":
            return parse_list(value)
        case "tuple":
            return parse_tuple(value)
        case "dict":
            return parse_dict(value) # not implemented yet
        case "string":
            return value
