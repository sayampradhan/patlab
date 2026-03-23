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
    palindrome: bool = True,
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
                    content = left  # 123

                else:
                    if i == 1:
                        content = "1"

                    elif i == n:
                        content = left

                    else:
                        # consistent pyramid spacing
                        content = "1" + " " * (2 * i - 3) + str(i)

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
    palindrome: bool = True,
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
    )