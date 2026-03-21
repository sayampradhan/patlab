# Right Triangle

## Basic

```python
from patlab.right_triangle import right_triangle
print(right_triangle(4))
```

```
*
**
***
****
```

## Right-Aligned

```python
print(right_triangle(4, alignment="right"))
```

```
   *
  **
 ***
****
```

## Inverted

```python
print(right_triangle(4, inversion=True))
```

```
****
***
**
*
```

## Hollow

```python
print(right_triangle(4, hollow=True))
```

```
*
**
* *
****
```

## Numeric

```python
print(right_triangle(4, numeric=True))
```

```
1
12
123
1234
```