# Square

The function `square()` can be used to generate square patterns using characters or numbers
---
## Function Signature
```python
square(
    n: int,
    char: str = "*"
    numeric: bool = False,
    increment: bool = False,
    space: bool = False
) -> str
```
`square()` creates an `n * n` grid based on configuration options:
- Character-based patterns (default)
- Numeric patterns
- Incremental sequences
- Optional spacing for readabiility
---

## Parameter
| Name        | Type | Default | Description                                                                            |
| ----------- | ---- | ------- | -------------------------------------------------------------------------------------- |
| `n`         | int  | —       | Size of the square (rows and columns). Must be positive.                               |
| `char`      | str  | `"*"`   | Character used to build the square. Must be a single character.                        |
| `numeric`   | bool | `False` | If `True`, generates numeric patterns instead of characters.                           |
| `increment` | bool | `False` | If `True`, rows contain `1 → n` instead of repeating numbers. Requires `numeric=True`. |
| `space`     | bool | `False` | Adds spaces between elements for better readability.                                   |
---

## Returns
- str — A string representing the square pattern with newline-separated rows
---

## Raises
| Exception    | Condition                                |
| ------------ | ---------------------------------------- |
| `ValueError` | If `n <= 0`                              |
| `ValueError` | If `char` is not a single character      |
| `ValueError` | If `numeric=True` and `char` is provided |
| `ValueError` | If `increment=True` but `numeric=False`  |
---

## Basic Usage
### Charater Mode (default)
Repeats the given character across all rows.
```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

#### Usage
##### Default Square
```python
print(square(3))
```
```
***
***
***
```

#### Default Square (with spaces)
```python
print(square(3, space=True))
```
```
* * *
* * *
* * *
```

#### Custom character
```python
print(square(4, "#"))
```
```
####
####
####
####
```
```python
print(square(3, "1"))
```
```
111
111
111
```

#### Custom character (with spaces)
```python
print(square(4,"#",space=True))
```
```
# # # #
# # # #
# # # #
# # # #
```
```python
print(square(3, "1", space=True))
```
```
1 1 1
1 1 1
1 1 1
```


### Numeric Mode
- Each row uses its row number:
```
1 1 1
2 2 2
3 3 3
```

#### Usage
##### Simple Numeric Pattern
```python
from patlab import square

print(square(4, numeric=True))
```
```
1111
2222
3333
4444
```

#### Simple Numeric Pattern (with spaces)
```python
from patlab import square

print(square(4, numeric=True, space=True))
```
```
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

#### Simple Incremental Numeric Pattern
```python
from patlab import square

print(square(4, numeric=True, incremental=True))
```
```
1234
1234
1234
1234
```

#### Simple Incremental Numeric Pattern (with spaces)
```python
from patlab import square

print(square(4, numeric=True, incremental=True, spaces=True))
```
```
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
```

## Notes
- `charr` is ignored when `numeric=True`
- `incremental=True` only works when `numeric=True`
- Output is always returned as a string (not printed)

## Tips
- Combine options carefully to avoid `ValueError`