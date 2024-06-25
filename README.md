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
