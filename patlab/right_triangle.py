def classic(n: int, char: str = "*", hollow: bool = False) -> str:
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

    Returns
    -------
    str
        A string representation of the right-angled triangle.

    Raises
    ------
    ValueError
        If `n` is not positive.

    Examples
    --------
    >>> print(classic(4))
    *
    **
    ***
    ****

    >>> print(classic(4, hollow=True))
    *
    **
    * *
    ****
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    if not hollow:
        return "\n".join([char * i for i in range(1, n + 1)])
    else:
        return "\n".join([
            char if i == 1 else
            char * i if i == n else
            char + ' ' * (i - 2) + char
            for i in range(1, n + 1)
        ])


def inverted(n: int, char: str = "*", hollow: bool = False) -> str:
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
        (Currently, hollow inverted triangles are not implemented.)

    Returns
    -------
    str
        A string representation of the inverted right-angled triangle.

    Raises
    ------
    ValueError
        If `n` is not positive.

    Examples
    --------
    >>> print(inverted(4))
    ****
    ***
    **
    *
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    if not hollow:
        return "\n".join([char * i for i in range(n, 0, -1)])
    else:
        return "\n".join([
            char if i == 1 else
            char * i if i == n else
            char + ' ' * (i - 2) + char
            for i in range(n, 0, -1)
        ])


def make(n: int, variant: str = "classic", char: str = "*") -> str:
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