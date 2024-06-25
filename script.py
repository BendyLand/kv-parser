import tests
import utils
import my_parser


test = tests.generate_random_key_val_str()


def initial_parse(text: str) -> dict:
    result = {}
    text = utils.normalize(text)
    lines = text.split("\n")
    for line in lines:
        res = line.split(":", 1)
        if len(res) > 1:
            k, v = res[0], res[1]
            if k is not None:
                result[k] = v.strip(" ,")
    return result


def infer_types(init_parse: dict) -> dict:
    result = {}
    for k in init_parse:
        result[k] = my_parser.parse_unknown_type(init_parse[k])
    return result


def display_dict(dict):
    for k in dict:
        print(f"{k} = {dict[k]} (Type: {type(dict[k])})")
    print()


print(test)
result = initial_parse(test)
result = infer_types(result)
display_dict(result)
