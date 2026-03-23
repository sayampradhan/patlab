from typing import Literal

def square(
        n: int, 
        char: str="*",
        numeric: bool=False,
        space: bool=False
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
    numeric : bool, optional
        If True, generates a numeric square instead of using the specified character.
        Each row will contain the row number repeated `n` times. Default is False.

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
    * * *
    * * *
    * * *

    >>> print(square(4, "#"))
    # # # #
    # # # #
    # # # #
    # # # #

    >>> print(square(5, numeric=True))
    1 1 1 1 1
    2 2 2 2 2 
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if space:
        if numeric:
                return "\n".join([(str(i) + " ") * n for i in range(1, n + 1)])
        else:
                return "\n".join([(char + " ") * n for _ in range(n)])
    else:
        if numeric:
            return "\n".join([str(i) * n for i in range(1, n + 1)])
        else:
            return "\n".join([char * n for _ in range(n)])