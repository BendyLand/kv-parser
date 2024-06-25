import random as rand


def generate_random_collection():
    length = rand.randint(1, 10)
    kind = rand.sample(["list", "dictionary", "tuple"], 1)[0]
    if kind == "list" or kind == "tuple":
        result = range(length)
        match kind:
            case "list":
                result = list(result)
            case "tuple":
                result = tuple(result)
    else:
        result = {}
        for i in range(length):
            key = "inner-key" + str(i + 1)
            result[key] = i + 1
    return result


def sponge_case(input):
    result = ""
    for c in input:
        check = rand.randint(1, 10)
        if check % 2 == 0:
            result += c.lower()
        else:
            result += c.upper()
    return result


def generate_random_simple_pair():
    num = rand.randint(1, 100)
    key = "simple-key" + str(num)
    rand_type = rand.sample(["int", "float", "char", "string", "bool"], 1)[0]
    value = "0"
    match rand_type:
        case "int":
            value = rand.randint(1, 10)
        case "float":
            integer = rand.randint(1, 10)
            decimal = rand.randint(1, 99)
            value = float(str(integer) + "." + str(decimal))
        case "char":
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            choice = rand.randint(0, 25)
            value = alphabet[choice]
        case "string":
            cutoff = rand.randint(20, 43)
            value = sponge_case("The quick brown fox jumps over the lazy dog")[:cutoff]
        case "bool":
            check = rand.randint(1, 5)
            if check % 2 == 0:
                value = True
            else:
                value = False
    result = key + ": " + str(value) 
    return result


def generate_random_complex_key():
    num = rand.randint(1, 100)
    return "complex-key" + str(num)


def dict_to_str(original):
    result = "{\n"
    for key in original:
        result += "\t\t" + str(key) + ": " + str(original[key]) + ",\n"
    return result[:-2] + "\n\t}"


def list_to_str(original):
    result = "["
    for c in original:
        result += str(c) + ", "
    return result[:-2] + "]"


def tuple_to_str(original):
    result = "("
    for c in original:
        result += str(c) + ", "
    return result[:-2] + ")"


def generate_random_complex_pair():
    result = ""
    key = generate_random_complex_key()
    value = generate_random_collection()
    if isinstance(value, dict):
        value = dict_to_str(value)
    elif isinstance(value, tuple):
        value = tuple_to_str(value)
    elif isinstance(value, list):
        value = list_to_str(value)
    else:
        value = str(value)
    result = key + ": " + value
    return result


def generate_random_key_value_pair():
    check = rand.randint(1, 100)
    if check < 75:
        return generate_random_simple_pair()
    else:
        return generate_random_complex_pair()


def generate_random_key_val_str():
    entries = rand.randint(3, 10)
    result = "{\n"
    for _ in range(entries-1):
        pair = generate_random_key_value_pair()
        result += "\t" + pair + ",\n"
    result = result + "\n}"
    return result 

