# Key-Value Parser

*This project is in its development stages and has limited functionality.*

An easy-to-use parser for more generic looking key-value pairs than actual formats, like JSON.

For when you just can't be bothered to enter everything manually!

## (Projected) Usage

```python
import kv-parser as kv

test = """
{
        simple-key38: False,
        simple-key64: tHe QUiCk bRoWn fOX,
        simple-key30: c,
        complex-key55: (5.0, 4.0, 3.0, 2.0, 1.0)
        simple-key64: False,
        simple-key49: True,
        complex-key9: {
                inner-key1: 1,
                inner-key2: 2,
                inner-key3: 3,
                inner-key4: 4,
        },
        complex-key89: [1, 2, 3, 4, 5],
        simple-key48: 5,
        simple-key27: w,

}
"""

result = kv.loads(test)
for key in result:
    print(f"{key}: {result[key]}")
# "simple-key38": False 
# "simple-key64": "tHe QUiCk bRoWn fOX" 
# "simple-key30": "c" 
# "complex-key55": (5.0, 4.0, 3.0, 2.0, 1.0) 
# "simple-key64": False 
# "simple-key49": True 
# "complex-key9": {"inner-key1": 1, "inner-key2": 2, "inner-key3": 3, "inner-key4": 4} 
# "complex-key89": [1, 2, 3, 4, 5] 
# "simple-key48": 5 
# "simple-key27": "w"
```

## Current Project Status

 - Basic key-value parsing and type inference works on most types in the outermost layer.
     - Dictionaries are currently represented as a single line string of the keys and values. 
 - Nesting can only go one layer deep.
     - Anything further will all be parsed inside of the current layer.
 - The elements found inside of collection types (lists, dicts, tuples) currently don't get type inference like basic values themselves. 
     - They're just represented as strings, and for some reason, from index 1 onward, each item has a space prepended to it. (I imagine that once I find and fix that bug, the type inference will happen soon after.) 
