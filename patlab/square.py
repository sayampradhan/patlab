from typing import Literal

def square(
        n: int, 
        char: str="*"
) -> str:
    """
    Generate a square pattern of size `n` using the specified character.

    Parameters:
    -----------
    n : int
        The size of the square (number of rows and columns). Must be positive.
    char : str, optional
        The character to use for building the square. Default is '*'.
        Should be a single character.

    Returns:
    --------
    str
        A string representing the square pattern, with each row separated by a newline.

    Raises:
    -------
    ValueError
        If `n` is not a positive integer.

    Examples:
    ---------
    >>> print(square(3))
    ***
    ***
    ***

    >>> print(square(4, "#"))
    ####
    ####
    ####
    ####
    """
    if n <= 0:
        raise ValueError("n must be positive")
    return "\n".join([char * n for _ in range(n)])