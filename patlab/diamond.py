from typing import Literal

def diamond(
    n: int,
    char: str = "*",
    hollow: bool = False,
    numeric: bool = False,
    space: bool = False,
) -> str:
    """
    Generate a diamond pattern of size `n` using the specified character.

    Parameters:
    -----------
    n : int
        The size of the diamond (number of rows). Must be a positive integer.
    char : str, optional
        The character to use for building the diamond. Default is '*'.
        Should be a single character.
    hollow : bool, optional
        If True, generates a hollow diamond (only borders are drawn). Default is False.
    numeric : bool, optional
        If True, generates a numeric diamond instead of using the specified character.
        Each row will contain the row number repeated as needed. Default is False.
    space : bool, optional
        If True, adds spaces between characters or numbers for better readability. Default is False.

    Returns:
    --------
    str
        A string representing the diamond pattern, with each row separated by a newline.

    Raises:
    -------
    ValueError
        If `n` is not a positive integer.
    ValueError
        If `char` is not a single character.
    ValueError
        If `char` is specified while `numeric` is True.

    Examples:
    ---------
    >>> print(diamond(3))
      *
     ***
      *

    >>> print(diamond(5, hollow=True))
      *
     * *
    *   *
     * *
      *

    >>> print(diamond(4, numeric=True, space=True))
       1
      2 2
     3 3 3
      2 2
       1

    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if numeric and char != "*":
        raise ValueError("Character is ignored when numeric is True.")
    if not numeric and len(char) != 1:
        raise ValueError("char must be a single character.")

    def make_line(i: int) -> str:
        width = 2 * i + 1
        pad = " " * (n - i - 1)

        val = str(i + 1) if numeric else char

        if hollow and width > 1:
            middle = " " * (width - 2)
            core = val + middle + val
        else:
            core = val * width

        if space:
            core = " ".join(core)

        return pad + core

    lines = []

    # top
    for i in range(n):
        lines.append(make_line(i))

    # bottom
    for i in range(n - 2, -1, -1):
        lines.append(make_line(i))

    return "\n".join(lines)