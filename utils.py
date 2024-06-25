import re


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
