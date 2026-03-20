from typing import Literal, Callable


Alignment = Literal["center", "left", "right"]


def pyramid(
    n: int,
    char: str = "*",
    alignment: Alignment = "center",
    inversion: bool = False,
    hollow: bool = False,
    numeric: bool = False,
) -> str:
    """
    Generate a pyramid with configurable style.

    Parameters
    ----------
    n : int
        Height of the pyramid (must be positive).
    char : str
        Character used for drawing (ignored if numeric=True).
    alignment : {'center', 'left', 'right'}
        Alignment of the pyramid.
    inversion : bool
        If True, pyramid is inverted.
    hollow : bool
        If True, pyramid is hollow.
    numeric : bool
        If True, uses numbers instead of characters.

    Returns
    -------
    str
        The generated pyramid.
    """
    if n <= 0:
        raise ValueError("n must be positive")

    lines = []

    levels = range(1, n + 1)
    if inversion:
        levels = reversed(levels)

    for i in levels:
        # --- CONTENT ---
        if numeric:
            content = "".join(str(x) for x in range(1, i + 1))
        else:
            if not hollow:
                if alignment == "center":
                    content = char * (2 * i - 1)
                else:
                    content = char * i
            else:
                if i == 1:
                    content = char
                elif i == n:
                    content = char * (2 * i - 1) if alignment == "center" else char * i
                else:
                    if alignment == "center":
                        content = char + " " * (2 * i - 3) + char
                    else:
                        content = char + " " * (i - 2) + char

        # --- ALIGNMENT ---
        if alignment == "center":
            width = 2 * n - 1
            line = content.center(width)
        elif alignment == "left":
            line = content.ljust(n)
        elif alignment == "right":
            line = content.rjust(n)
        else:
            raise ValueError("Invalid alignment")

        lines.append(line)

    return "\n".join(lines)