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
            # Build numeric pattern
            left = "".join(str(x) for x in range(1, i + 1))

            if alignment == "center":
                # Palindromic pyramid: 12321
                content = left + left[-2::-1]
            else:
                # Simple numeric: 123
                content = left

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

def make(
    n: int,
    variant: Variant = "centered",
    char: str = "*",
    alignment: Alignment | None = None,
    hollow: bool = False,
) -> str:
    """
    Create a pyramid of a specified variant.

    This is a convenience factory function that wraps `pyramid()` and
    `numeric_pyramid()` to simplify common use cases by automatically
    selecting the appropriate configuration.

    Parameters
    ----------
    n : int
        Height of the pyramid. Must be a positive integer.
    variant : {'centered', 'left', 'right', 'inverted', 'numeric'}, optional
        Type of pyramid to generate:
        - 'centered' : standard centered pyramid (default)
        - 'left'     : left-aligned pyramid
        - 'right'    : right-aligned pyramid
        - 'inverted' : inverted centered pyramid
        - 'numeric'  : numeric pyramid
    char : str, optional
        Character used for drawing the pyramid (default is '*').
        Ignored when `variant='numeric'`.
    alignment : {'center', 'left', 'right'}, optional
        Overrides the default alignment for the selected variant.
        If not provided, a sensible default is used.
    hollow : bool, optional
        If True, generates a hollow pyramid (default is False).

    Returns
    -------
    str
        A string representation of the generated pyramid.

    Raises
    ------
    ValueError
        If an unknown `variant` is provided.
    """
    valid_variants = {"centered", "left", "right", "inverted", "numeric"}
    if variant not in valid_variants:
        raise ValueError(
            f"Unknown pyramid variant: {variant}. Available: {list(valid_variants)}"
        )

    # Default alignment per variant
    default_alignment = {
        "centered": "center",
        "left": "left",
        "right": "right",
        "inverted": "center",
        "numeric": "center",
    }

    final_alignment = alignment if alignment is not None else default_alignment[variant]

    if variant == "numeric":
        return numeric_pyramid(
            n,
            alignment=final_alignment,
            hollow=hollow,
        )

    return pyramid(
        n=n,
        char=char,
        alignment=final_alignment,
        inversion=(variant == "inverted"),
        hollow=hollow,
    )