# Pyramid

## Centered Pyramid

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

## Left-Aligned

```python
print(pyramid(4, alignment="left"))
```

```
*
**
***
****
```

## Right-Aligned

```python
print(pyramid(4, alignment="right"))
```

```
   *
  **
 ***
****
```

## Inverted

```python
print(pyramid(4, inversion=True))
```

```
*******
 *****
  ***
   *
```

## Hollow

```python
print(pyramid(4, hollow=True))
```

```
   *
  * *
 *   *
*******
```

## Numeric

```python
print(pyramid(4, numeric=True))
```

```
   1
  121
 12321
1234321
```