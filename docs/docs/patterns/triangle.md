# right_triangle()

Generate configurable right-angled triangle patterns using characters or numbers.



## Overview

The `right_triangle()` function creates a right-angled triangle of height `n` with flexible styling options, including:

- Character or numeric output
- Left or right alignment
- Inverted orientation
- Hollow (border-only) structure
- Optional spacing for readability

This function is suitable for CLI visualization, pattern generation, and educational demonstrations.


## Function Signature

```python
right_triangle(
    n: int,
    char: str = "*",
    alignment: Literal["left", "right"] = "left",
    inversion: bool = False,
    hollow: bool = False,
    numeric: bool = False,
    space: bool = False
) -> str
```

## Parameters

| Name        | Type | Default  | Description                                                     |
| ----------- | ---- | -------- | --------------------------------------------------------------- |
| `n`         | int  | —        | Height of the triangle. Must be positive.                       |
| `char`      | str  | `"*"`    | Character used to draw the triangle. Ignored if `numeric=True`. |
| `alignment` | str  | `"left"` | Alignment of the triangle: `left` or `right`.                   |
| `inversion` | bool | `False`  | If `True`, generates an inverted triangle.                      |
| `hollow`    | bool | `False`  | If `True`, draws only the border of the triangle.               |
| `numeric`   | bool | `False`  | Uses numbers instead of characters (e.g., `1`, `12`, `123`).    |
| `space`     | bool | `False`  | Adds spaces between elements for better readability.            |

## Returns
- str — A newline-separated string representing the triangle.

## Raises

| Exception    | Condition                                   |
| ------------ | ------------------------------------------- |
| `ValueError` | If `n <= 0`                                 |
| `ValueError` | If `alignment` is not `"left"` or `"right"` |
| `ValueError` | If `numeric=True` and `char` is specified   |

## Usage
### Default Pyramid
```
*
**
***
****
```
#### Usage Example
##### 1. Default Right-Triangle
```python
print(right_triangle(4))
```
```
*
**
***
****
```

##### 2. Right-Triangle (with `space=True`)
```python
print(right_triangle(4, space=True))
```
```
*
* *
* * *
* * * *
```

##### 3. Right-Triangle (with `hollow=True`)
```python
print(right_triangle(5, hollow=True))
```
```
*
**
* *
*  *
*****
```

##### 4. Right-Triangle (with `hollow=True` and `space=True`)
```python
print(right_triangle(5, hollow=True, space=True))
```
```
*
* *
*   *
*     *
* * * * *
```

##### 5. Right-Triangle (with `inversion=True`)
```python
print(right_triangle(4, inversion=True))
```
```
****
***
**
*
```

##### 6. Right-Triangle (with `inversion=True` and `space=True`)
```python
print(right_triangle(4, inversion=True, space=True))
```
```
* * * *
* * *
* *
*
```

##### 7. Right-Triangle (with `inversion=True` and `hollow=True`)
```python
print(right_triangle(5, inversion=True, hollow=True))
```
```
*****
*  *
* *
**
*
```

##### 8. Right-Triangle (with `inversion=True` and `hollow=True` and `space=True`)
```python
print(right_triangle(5, inversion=True, hollow=True, space=True))
```
```
* * * * *
*     *
*   *
* *
*
```

### Right-Aligned Triangle

```
*
**
***
****
```

#### Usage Examples

##### 1. Right-Aligned Triangle (`alignment=right`)
```python
print(right_triangle(4, alignment="right"))
```
```
   *
  **
 ***
****
```

##### 2. Right-Aligned Triangle (`alignment=right` and `space=True`)
```python
print(right_triangle(4, alignment="right"))
```
```
      *
    * *
  * * *
* * * *
```
##### 3. Right-Aligned Triangle (`alignment=right` and `hollow=True`)
```python
print(right_triangle(5, alignment=True, hollow=True))
```
```
    *
  * *
 *  *
*****
```

##### 4. Right-Aligned Triangle (`alignment=right` and `inversion=True`)
```python
print(right_triangle(4, alignment="right", inversion=True))
```
```
****
 ***
  **
   *
```

##### 5. Right-Aligned Triangle (`alignment=right` and `inversion=True` and `hollow=True`)
```python
print(right_triangle(5, alignment="right", inversion=True, hollow=True))
```
```
*****
 *  *
  * *
   **
    *
```

### Numeric Right-Triangle
```
1
12
123
1234
```
#### Usage Examples
##### 1. Numeric Triangle (`numeric=True`)
```python
print(right_triangle(4, numeric=True))
```
```
1
12
123
1234
```

##### 2. Numeric Triangle (`numeric=True` and `space=True`)
```python
print(right_triangle(4, numeric=True, space=True))
```
```
1
1 2
1 2 3
1 2 3 4
```

##### 3. Numeric Triangle (`numeric=True` and `hollow=True`)
```python
print(right_triangle(5, numeric=True, hollow=True))
```
```
1
12
1 3
1  4
12345
```

### More Examples
##### Example 1
```python
print(right_triangle(4,char="#",space=True))
```
```
#
# #
# # #
# # # #
```

##### Example 2
```python
print(right_triangle(5,"1",hollow=True))
```
```
1
11
1 1
1  1
11111
```

## Warnings
- Hollow triangles may not render properly for very small sizes (n <= 3)
- The function prints a warning message in such cases
- Space option may not work well with right alignment

## Notes
- char is ignored when numeric=True
- Output is always returned as a string (not printed)
- Alignment padding is based on n
- Spacing affects both numeric and character modes

## Tips
- Use space=True for clearer visual output in larger triangles
- Use right alignment for staircase-style visuals
- Combine hollow=True with larger n for better patterns
- Numeric mode is useful for teaching loops and sequences