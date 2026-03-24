# Pyramid()

Generate highly customizable text-based pyramid patterns.

## Function Signature
```python
pyramid(
    n: int,
    char: str = "*",
    alignment: Literal["center", "left", "right"] = "center",
    inversion: bool = False,
    hollow: bool = False,
    numeric: bool = False,
    palindrome: bool = False,
) -> str
```

## Parameters
| Name         | Type | Default    | Description                                              |
| ------------ | ---- | ---------- | -------------------------------------------------------- |
| `n`          | int  | —          | Height of the pyramid. Must be positive.                 |
| `char`       | str  | `"*"`      | Character used for drawing. Ignored when `numeric=True`. |
| `alignment`  | str  | `"center"` | Pyramid alignment: `center`, `left`, or `right`.         |
| `inversion`  | bool | `False`    | If `True`, generates an inverted pyramid.                |
| `hollow`     | bool | `False`    | If `True`, only borders are drawn.                       |
| `numeric`    | bool | `False`    | Enables numeric patterns instead of characters.          |
| `palindrome` | bool | `False`    | Enables mirrored numeric patterns (e.g., `12321`).       |

## Returns
- str — A newline-separated string representing the pyramid.

## Raise
| Exception    | Condition                                                 |
| ------------ | --------------------------------------------------------- |
| `ValueError` | If `n <= 0`                                               |
| `ValueError` | If `alignment` is not one of `center`, `left`, or `right` |

## Usage
- Character Mode (default)
   - Builds pyramids using a repeated character.
- Numeric Mode
   - Uses increasing numbers per row
   - Ignores char
- Palindrome Mode
   - Produces symmetric numeric sequences
   - Example: 12321
- Hollow Mode
   - Only edges are drawn
   - Interior is filled with spaces
- Inversion
   - Flips the pyramid vertically

### Default Pyramid
```
   *
  ***
 *****
*******
```

#### Usage Examples

##### 1. Default Pyramid
```python
from patlab.pyramid import pyramid
print(pyramid(4))
```

```
   *
  ***
 *****
*******
```

##### 2. Default Pyramid (with `hollow=True`)
```python
print(pyramid(4, hollow=True))
```

```
   *
  * *
 *   *
*******
```

##### 3. Default Pyramid (with `inversion=True`)
```python
from patlab.pyramid import pyramid
print(pyramid(4, inversion=True))
```

```
*******
 *****
  ***
   *
```

##### 4. Default Pyramid (with `inversion=True` and `hollow=True`)
```python
from patlab.pyramid import pyramid
print(pyramid(4, inversion=True, hollow=True))
```

```
*******
 *   *
  * *
   *
```



### Left-Aligned Pyramid
```
*
**
***
****
```

#### Usage Examples

##### 1. Left Pyramid
```python
print(pyramid(4, alignment="left"))
```

```
*
**
***
****
```

##### 2. Left Pyramid (with `hollow=True`)
```python
print(pyramid(5, alignment="left", hollow=True))
```

```
*
**
* *
*  *
*****
```

##### 3. Left Pyramid (with `inversion=True`)
```python
print(pyramid(5, alignment="left", inversion=True))
```

```
*****
****
***
**
*
```

##### 4. Left Pyramid (with `inversion=True` and `hollow=True`)
```python
print(pyramid(5, alignment="left", inversion=True, hollow=True))
```

```
*****
*  *
* *
**
*
```

### Right-Aligned Pyramid
```
   *
  **
 ***
****
```

#### Usage Examples
##### 1. Right Pyramid
```python
print(pyramid(4, alignment="right"))
```

```
   *
  **
 ***
****
```

##### 2. Right Pyramid (with `hollow=True`)
```python
print(pyramid(4, alignment="right"))
```

```
   *
  **
 * *
****
```

##### 3. Right Pyramid (with `inversion=True`)
```python
print(pyramid(4, alignment="right", inversion=True))
```

```
****
 ***
  **
   *
```

##### 4. Right Pyramid (with `inversion=True` and `hollow=True`)
```python
print(pyramid(4, alignment="right", inversion=True, hollow=True))
```

```
****
 * *
  **
   *
```

#### Numeric Pyramid
```
   1
  123
 12345
1234567
```

##### 1. Numeric Pyramid
```python
print(pyramid(4, numeric=True))
```
```
   1
  123
 12345
1234567
```

##### 1. Numeric Pyramid (with `hollow=True`)
```python
print(pyramid(4, numeric=True, hollow=True))
```
```
   1
  1 3
 1   5
1234567
```

##### 2. Numeric Pyramid (with `palindrome=True`)
```python
print(pyramid(4, numeric=True, palindrome=True))
```
```
   1
  121
 12321
1234321
```

##### 3. Numeric Pyramid (with `palindrome=True` and `hollow=True`)
```python
print(pyramid(4, numeric=True, palindrome=True, hollow=True))
```
```
   1
  1 1
 1   1
1234321
```

##### 4. Numeric Pyramid (with `inversion=True`)
```python
print(pyramid(4, numeric=True, inversion=True))
```
```
1234567
 12345
  123
   1
```

##### 5. Numeric Pyramid (with `inversion=True`, `hollow=True`)
```python
print(pyramid(4, numeric=True, inversion=True))
```
```
1234567
 1   5
  1 3
   1
```

##### 6. Numeric Pyramid (with `inversion=True` and `palindrome=True`)
```python
print(pyramid(4, numeric=True, inversion=True, palindrome=True))
```
```
1234321
 12321
  121
   1
```

##### 7. Numeric Pyramid (with `inversion=True` and `palindrome=True` and `hollow=True`)
```python
print(pyramid(4, numeric=True, inversion=True, palindrome=True))
```
```
1234321
 1   1
  1 1
   1
```


## Convenience Function
`numeric_pyramid()`
A simplified wrapper for numeric pyramids.

### Signature
```python
numeric_pyramid(
    n: int,
    alignment: Literal["center", "left", "right"] = "center",
    inversion: bool = False,
    hollow: bool = False,
    palindrome: bool = False,
) -> str
```

### Description
Equivalent to:
```pytho
pyramid(..., numeric=True)
```

### Example
```python
print(numeric_pyramid(4, palindrome=True))
```

```
   1
  121
 12321
1234321
```

## Notes
- `char` is ignored when `numeric=True`
- `palindrome=True` only applies in numeric mode
- Hollow pyramids always preserve borders
- Output is returned as a string (not printed) 

## Tips
- Use `center` alignment for traditional pyramids
- Use l`eft/right` for staircase-style patterns
- Combine `numeric + palindrome` for symmetric designs
- Use `hollow=True` for visual clarity in large pyramids