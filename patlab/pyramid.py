from typing import Literal

Alignment = Literal["center", "left", "right"]
Variant = Literal["centered", "left", "right", "inverted", "numeric"]

def pyramid(
    n: int,
    char: str = "*",
    alignment: Alignment = "center",
    inversion: bool = False,
    hollow: bool = False,
    numeric: bool = False,
    palindrome: bool = False,
) -> str:
    """
    Generate a configurable text-based pyramid pattern.

    This function creates a pyramid of height `n` with flexible styling options,
    including alignment, inversion, hollow structure, numeric output, and
    palindromic formatting.

    Parameters
    ----------
    n : int
        Height of the pyramid. Must be a positive integer.
    char : str, optional
        Character used to draw the pyramid (default is '*').
        Ignored if `numeric=True`.
    alignment : {'center', 'left', 'right'}, optional
        Alignment of the pyramid:
        - 'center' : symmetric pyramid (default)
        - 'left'   : left-aligned pyramid
        - 'right'  : right-aligned pyramid
    inversion : bool, optional
        If True, generates an inverted pyramid (top-down).
        Default is False.
    hollow : bool, optional
        If True, generates a hollow pyramid (only borders are drawn).
        Default is False.
    numeric : bool, optional
        If True, uses numbers instead of characters.
        Default is False.
    palindrome : bool, optional
        If True, generates a palindromic numeric pyramid (e.g., 12321).
        Only applies when `numeric=True`.
        Default is False.

    Returns
    -------
    str
        A string representation of the generated pyramid, with each row
        separated by a newline.

    Raises
    ------
    ValueError
        If `n` is not a positive integer.
    ValueError
        If `alignment` is not one of 'center', 'left', or 'right'.

    Notes
    -----
    - When `numeric=True`:
    - `palindrome=True` produces symmetric patterns (e.g., 12321).
    - `palindrome=False` produces progressive patterns:
        - Center-aligned → odd-length sequences (e.g., 12345)
        - Left/right-aligned → incremental sequences (e.g., 123)
    - When `hollow=True`, only boundary elements are displayed.

    Examples
    --------
    >>> print(pyramid(3))
    *
    ***
    *****

    >>> print(pyramid(3, numeric=True))
    1
    123
    12345

    >>> print(pyramid(4, numeric=True, palindrome=True))
    1
    121
    12321
    1234321

    >>> print(pyramid(4, hollow=True))
    *
    * *
    *   *
    *******
    """
    if n <= 0:
        raise ValueError("n must be positive")

    lines = []

    levels = range(1, n + 1)
    if inversion:
        levels = reversed(list(levels))

    for i in levels:
    # --- CONTENT ---
        if numeric:
            left = "".join(str(x) for x in range(1, i + 1))

            if palindrome:
                if not hollow:
                    content = left + left[-2::-1]

                else:
                    if i == 1:
                        content = "1"

                    elif i == n:
                        content = left + left[-2::-1]

                    else:
                        # same logic for ALL middle rows
                        if alignment == "center":
                            content = "1" + " " * (2 * i - 3) + "1"
                        else:
                            content = "1" + " " * (2 * i - 3) + "1"
            else:
                # ---------------- NON-PALINDROME ----------------
                if not hollow:
                    if alignment == "center":
                        content = "".join(str(x) for x in range(1, 2 * i))
                    else:
                        content = left

                else:
                    if i == 1:
                        content = "1"

                    elif i == n:
                        # full row: 123456789
                        content = "".join(str(x) for x in range(1, 2 * n))

                    else:
                        # key fix here
                        content = "1" + " " * (2 * i - 3) + str(2 * i - 1)

            # --- ALIGNMENT ---
        if alignment == "center":
            width = 2 * n - 1
            line = content.center(width)
        elif alignment == "left":
            width = 2 * n - 1 if numeric else n
            line = content.ljust(width)
        elif alignment == "right":
            width = 2 * n - 1 if numeric else n
            line = content.rjust(width)
        else:
            raise ValueError("Invalid alignment")

        lines.append(line)

    return "\n".join(lines)


def numeric_pyramid(
    n: int,
    alignment: Alignment = "center",
    inversion: bool = False,
    hollow: bool = False,
    palindrome: bool = False,
) -> str:
    """
    Convenience wrapper for numeric pyramids.
    """
    return pyramid(
        n=n,
        alignment=alignment,
        inversion=inversion,
        hollow=hollow,
        numeric=True,
        palindrome=palindrome,
    )