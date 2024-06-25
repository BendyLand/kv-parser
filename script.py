import re
import tests


test = tests.generate_random_key_val_str()
# test = """
# {
#         simple-key38: False,
#         simple-key64: tHe QUiCk bRoWn fOX,
#         simple-key30: c,
#         complex-key55: (5.0, 4.0, 3.0, 2.0, 1.0)
#         simple-key64: False,
#         simple-key49: True,
#         complex-key9: {
#                 inner-key1: 1,
#                 inner-key2: 2,
#                 inner-key3: 3,
#                 inner-key4: 4,
#                 inner-key5: 5,
#                 inner-key6: 6,
#                 inner-key7: 7
#         },
#         complex-key89: [1, 2, 3, 4, 5],
#         simple-key48: 5,
#         simple-key27: w,

# }
# """


def normalize(text: str) -> str:
    # Removes tabs.
    lines = text.split("\n")
    lines = [*filter(lambda x: x != "", lines)]
    lines = lines[1:-1]  # removes outer {}
    lines = [*map(lambda x: x.strip(" \t"), lines)]
    text = "\n".join(lines)

    i = 0
    temp_line = ""
    inner_dict = False
    result = []
    while i < len(lines):
        if inner_dict:
            temp_line += lines[i] + " "
            if "}" in lines[i]:
                inner_dict = False
                result.append(temp_line)
                temp_line = ""
            i += 1
            continue
        if "{" in lines[i]:
            temp_line += lines[i]
            inner_dict = True
        else:
            result.append(lines[i])
        i += 1
    return "\n".join(result)


def extract_collections(text: str) -> list:
    text = normalize(text)
    lines = text.split("\n")
    result = []
    for line in lines:
        lists = re.findall(r"\[.*\]", line)
        dicts = re.findall(r"\{.*\}", line)
        tuples = re.findall(r"\(.*\)", line)
        has_collection = len(lists) > 0 or len(dicts) > 0 or len(tuples) > 0
        if has_collection:
            if len(lists) > 0:
                result.append(lists[0])
            if len(dicts) > 0:
                result.append(dicts[0])
            if len(tuples) > 0:
                result.append(tuples[0])
    return result


def find_matching_collection(entry, collections):
    for coll in collections:
        if entry is not None:
            if entry in coll:
                return coll


def initial_parse(text: str) -> dict:
    result = {}
    text = normalize(text)
    lines = text.split("\n")
    for line in lines:
        res = line.split(":", 1)
        if len(res) > 1:
            k, v = res[0], res[1]
            if k is not None:
                result[k] = v.strip(" ,")
    return result


print(test)
result = initial_parse(test)
for k in result:
    print(f"{k} = {result[k]}")
