"""
pyramid.py

Module for generating various pyramid shapes in text form.

Available pyramid variants:
- centered: A classic centered pyramid.
- right: Right-aligned pyramid (staircase style).
- numeric: Pyramid with ascending numbers.
"""

from typing import Literal


def centered(n: int, char: str = "*", hollow: bool = False) -> str:
    """
    Generate a centered pyramid of height `n`.

    Parameters
    ----------
    n : int
        The height of the pyramid. Must be a positive integer.
    char : str, optional
        The character used to build the pyramid (default is '*').
    hollow : bool, optional
        If True, generate a hollow pyramid (default is False).

    Returns
    -------
    str
        A string representation of the centered pyramid.

    Raises
    ------
    ValueError
        If `n` is not positive.

    Examples
    --------
    >>> print(centered(4))
       *
      ***
     *****
    *******

    >>> print(centered(4, hollow=True))
       *
      * *
     *   *
    *******
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    lines = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        if not hollow:
            stars = char * (2 * i - 1)
            lines.append(spaces + stars)
        else:
            if i == 1:
                line = spaces + char
            elif i == n:
                line = char * (2 * i - 1)
            else:
                line = spaces + char + " " * (2 * i - 3) + char
            lines.append(line)
    return "\n".join(lines)


def right_aligned(n: int, char: str = "*", hollow: bool = False) -> str:
    """
    Generate a right-aligned pyramid (staircase style) of height `n`.

    Parameters
    ----------
    n : int
        The height of the pyramid. Must be positive.
    char : str, optional
        The character used to build the pyramid (default is '*').
    hollow : bool, optional
        If True, generate a hollow right-aligned pyramid (default is False).

    Returns
    -------
    str
        A string representation of the right-aligned pyramid.

    Raises
    ------
    ValueError
        If `n` is not positive.

    Examples
    --------
    >>> print(right_aligned(4))
    *
    **
    ***
    ****

    >>> print(right_aligned(4, hollow=True))
    *
    **
    * *
    ****
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    lines = []
    for i in range(1, n + 1):
        if not hollow:
            lines.append(char * i)
        else:
            if i == 1:
                lines.append(char)
            elif i == n:
                lines.append(char * i)
            else:
                lines.append(char + " " * (i - 2) + char)
    return "\n".join(lines)


def numeric(n: int) -> str:
    """
    Generate a numeric pyramid of height `n`.

    Each row displays numbers from 1 up to the row number.

    Parameters
    ----------
    n : int
        The height of the pyramid. Must be positive.

    Returns
    -------
    str
        A string representation of the numeric pyramid.

    Raises
    ------
    ValueError
        If `n` is not positive.

    Examples
    --------
    >>> print(numeric(4))
       1
      12
     123
    1234
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    lines = []
    for i in range(1, n + 1):
        line = " " * (n - i) + "".join(str(x) for x in range(1, i + 1))
        lines.append(line)
    return "\n".join(lines)


def make(n: int, variant: Literal["centered", "right", "numeric"] = "centered", char: str = "*") -> str:
    """
    Factory function to generate a pyramid of a specified variant.

    Parameters
    ----------
    n : int
        The height of the pyramid. Must be positive.
    variant : {'centered', 'right', 'numeric'}, optional
        The pyramid style to generate (default is 'centered'):
        - 'centered': classic centered pyramid.
        - 'right': right-aligned (staircase) pyramid.
        - 'numeric': pyramid of ascending numbers (ignores `char`).
    char : str, optional
        The character used for drawing the pyramid (default is '*').
        Ignored if `variant='numeric'`.

    Returns
    -------
    str
        A string representation of the chosen pyramid variant.

    Raises
    ------
    ValueError
        If `variant` is not one of the supported options.

    Examples
    --------
    >>> print(make(4, variant='centered'))
       *
      ***
     *****
    *******

    >>> print(make(4, variant='right', char='#'))
    #
    ##
    ###
    ####

    >>> print(make(4, variant='numeric'))
       1
      12
     123
    1234
    """
    variants = {
        "centered": centered,
        "right": right_aligned,
        "numeric": numeric,
    }

    if variant not in variants:
        raise ValueError(
            f"Unknown pyramid variant: {variant}. Available: {list(variants.keys())}"
        )

    return variants[variant](n, char) if variant != "numeric" else variants[variant](n)