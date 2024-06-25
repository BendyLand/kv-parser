import tests
import utils


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
#                 inner-key4: {
# doesn't work yet     more-inner-key: 0,
#                 },
#                 inner-key5: 5,
#                 inner-key6: 6,
#                 inner-key7: 7
#         },
#         complex-key89: [1, 2, 3, 4, 5],
#         simple-key48: 5,
#         simple-key27: w,

# }
# """

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


print(test)
result = initial_parse(test)
for k in result:
    print(f"{k} = {result[k]}")
