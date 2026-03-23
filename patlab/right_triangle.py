from typing import Literal

Alignment = Literal["left", "right"]
Variant = Literal["classic", "inverted"]


def right_triangle(
    n: int,
    char: str = "*",
    alignment: Alignment = "left",
    inversion: bool = False,
    hollow: bool = False,
    numeric: bool = False,
) -> str:
    """
    Generate a right-angled triangle with configurable style.

    This function creates a text-based right triangle of height `n`,
    with options for alignment, inversion, hollow structure, and
    numeric output.

    Parameters
    ----------
    n : int
        Height of the triangle. Must be a positive integer.
    char : str, optional
        Character used to draw the triangle (default is '*').
        Ignored if `numeric=True`.
    alignment : {'left', 'right'}, optional
        Alignment of the triangle:
        - 'left'  : left-aligned triangle (default)
        - 'right' : right-aligned triangle
    inversion : bool, optional
        If True, generates an inverted triangle (top-down).
        Default is False.
    hollow : bool, optional
        If True, generates a hollow triangle (only borders).
        Default is False.
    numeric : bool, optional
        If True, uses numbers instead of characters.
        Each row increases sequentially (e.g., 1, 12, 123).
        Default is False.

    Returns
    -------
    str
        A string representation of the generated triangle.

    Raises
    ------
    ValueError
        If `n` is not positive.
    ValueError
        If `char` is specified while `numeric=True`.
    ValueError
        If `alignment` is invalid.

    Examples
    --------
    >>> print(right_triangle(4))
    *
    **
    ***
    ****

    >>> print(right_triangle(4, alignment="right"))
       *
      **
     ***
    ****

    >>> print(right_triangle(4, inversion=True))
    ****
    ***
    **
    *

    >>> print(right_triangle(4, numeric=True))
    1
    12
    123
    1234
    """
    if alignment not in {"left", "right"}:
        raise ValueError(f"Invalid alignment: {alignment}. Must be 'left' or 'right'.")
    if n <= 0:
        raise ValueError("n must be positive")

    if numeric and char != "*":
        raise ValueError("Cannot specify 'char' when numeric=True")
    
    if hollow and n <= 3:
        print("Warning: Value should be greater than 3 to create hollow right triangle")

    lines = []

    levels = range(1, n + 1)
    if inversion:
        levels = reversed(list(levels))

    for i in levels:
        if numeric:
            if not hollow:
                content = "".join(str(x) for x in range(1, i + 1))
            else:
                if i == 1:
                    content = "1"
                elif i == n:
                    content = "".join(str(x) for x in range(1, n + 1))
                else:
                    content = "1" + " " * (i - 2) + str(i)
        else:
            if not hollow:
                content = char * i
            else:
                if i == 1:
                    content = char
                elif i == n:
                    content = char * n
                else:
                    content = char + " " * (i - 2) + char

        if alignment == "left":
            line = content.ljust(n)
        elif alignment == "right":
            line = content.rjust(n)
        else:
            raise ValueError("Invalid alignment")

        lines.append(line)
    return "\n".join(lines)