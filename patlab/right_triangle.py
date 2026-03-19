from typing import Literal
import inspect

def classic(n: int, char: str = "*", hollow: bool = False, numeric: bool = False) -> str:
    """
    Generate a right-angled triangle of height `n`.

    Parameters
    ----------
    n : int
        The height of the triangle. Must be a positive integer.
    char : str, optional
        The character used to draw the triangle (default is '*').
    hollow : bool, optional
        If True, generate a hollow triangle (default is False).
    numeric : bool, optional
        If True, print numbers instead of characters (default is False).

    Returns
    -------
    str
        A string representation of the right-angled triangle.

    Raises
    ------
    ValueError
        If `n` is not positive or if `char` is passed while numeric=True.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    # Disallow any explicit char when numeric=True
    caller_args = inspect.currentframe().f_locals
    if numeric and caller_args.get("char", "*") != "*":
        raise ValueError("Cannot specify 'char' when numeric=True")
    
    lines = []
    for i in range(1, n + 1):
        if numeric:
            if not hollow:
                line = "".join(str(x) for x in range(1, i + 1))
            else:
                if i == 1:
                    line = "1"
                elif i == n:
                    line = "".join(str(x) for x in range(1, n + 1))
                else:
                    line = "1" + " " * (i - 2) + str(i)
        else:
            if not hollow:
                line = char * i
            else:
                if i == 1:
                    line = char
                elif i == n:
                    line = char * n
                else:
                    line = char + " " * (i - 2) + char
        lines.append(line)
    return "\n".join(lines)


def inverted(n: int, char: str = "*", hollow: bool = False, numeric: bool = False) -> str:
    """
    Generate an inverted right-angled triangle of height `n`.

    Parameters
    ----------
    n : int
        The height of the triangle. Must be a positive integer.
    char : str, optional
        The character used to draw the triangle (default is '*').
    hollow : bool, optional
        If True, generate a hollow triangle (default is False).

    Returns
    -------
    str
        A string representation of the inverted right-angled triangle.

    Raises
    ------
    ValueError
        If `n` is not positive or if `char` is passed while numeric=True.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    # Disallow any explicit char when numeric=True
    caller_args = inspect.currentframe().f_locals
    if numeric and caller_args.get("char", "*") != "*":
        raise ValueError("Cannot specify 'char' when numeric=True")
    
    lines = []
    for i in range(n, 0, -1):
        if numeric:
            if not hollow:
                line = "".join(str(x) for x in range(1, i + 1))
            else:
                if i == 1:
                    line = "1"
                elif i == n:
                    line = "".join(str(x) for x in range(1, n + 1))
                else:
                    line = "1" + " " * (i - 2) + str(i)
        else:
            if not hollow:
                line = char * i
            else:
                if i == 1:
                    line = char
                elif i == n:
                    line = char * n
                else:
                    line = char + " " * (i - 2) + char
        lines.append(line)
    return "\n".join(lines)


def make(n: int, variant: Literal["classic","inverted"] = "classic", char: str = "*") -> str:
    """
    Factory function to create a right-angled triangle of a specified variant.

    Parameters
    ----------
    n : int
        The height of the triangle. Must be positive.
    variant : str, optional
        The triangle variant. Options are:
        - "classic": normal right-angled triangle (default)
        - "inverted": inverted right-angled triangle
    char : str, optional
        The character used to draw the triangle (default is '*').

    Returns
    -------
    str
        A string representation of the chosen triangle variant.

    Raises
    ------
    ValueError
        If `variant` is not recognized.

    Examples
    --------
    >>> print(make(4, variant="classic"))
    *
    **
    ***
    ****

    >>> print(make(4, variant="inverted"))
    ****
    ***
    **
    *
    """
    variants = {
        "classic": classic,
        "inverted": inverted
    }

    if variant not in variants:
        raise ValueError(
            f"Unknown right-triangle variant: {variant}. Available: {list(variants.keys())}"
        )

    return variants[variant](n, char)