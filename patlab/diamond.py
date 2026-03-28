from typing import Literal

def diamond(
    height: int,
    char: str = "*",
    hollow: bool = False,
    numeric: bool = False,
) -> str:
    """
    Generate a symmetric diamond pattern using a character or numbers.

    Parameters
    ----------
    height : int
        Total number of rows in the diamond. Must be a positive **odd** integer
        to ensure symmetry.
    char : str, optional
        The character used to build the diamond (default is '*').
        Must be a single character. Ignored if `numeric` is True.
    hollow : bool, optional
        If True, generates a hollow diamond (only the border is drawn).
        Default is False.
    numeric : bool, optional
        If True, generates a numeric diamond instead of using `char`.
        Each row contains the row number repeated. Default is False.

    Returns
    -------
    str
        A string representing the diamond pattern, with rows separated by newline characters.

    Raises
    ------
    ValueError
        If `height` is not a positive integer.
    ValueError
        If `height` is even (diamond must be symmetric).
    ValueError
        If `char` is not a single character when `numeric` is False.
    ValueError
        If `char` is specified while `numeric` is True.

    Examples
    --------
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

    >>> print(diamond(5, numeric=True))
      1
     222
    33333
     222
      1
    """
    if height <= 0:
        raise ValueError("n must be a positive integer.")
    if numeric and char != "*":
        raise ValueError("Character is ignored when numeric is True.")
    if not numeric and len(char) != 1:
        raise ValueError("char must be a single character.")
    if height % 2 == 0:
        raise ValueError("Height must be an odd number for a symmetric diamond.")

    def make_line(width: int) -> str:
        count = 2 * width + 1
        pad = " " * (height - width - 1)
        val = str(width + 1) if numeric else char

        if hollow and count > 1:
            middle = [" "] * (count - 2)
            elems = [val] + middle + [val]
        else:
            elems = [val] * count

        sep = ""
        return pad + sep.join(elems)

    lines = []
    top = (height + 1) // 2
    bottom = height // 2

    for i in range(top):
        lines.append(make_line(i))
    for i in range(bottom - 1, -1, -1):
        lines.append(make_line(i))

    return "\n".join(lines)
