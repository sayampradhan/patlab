from typing import Literal

def square(
        n: int, 
        char: str="*",
        numeric: bool=False,
        increment: bool=False,
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
    >>> print(square(3, space=True))
    * * *
    * * *
    * * *

    >>> print(square(4, "#", space=True))
    # # # #
    # # # #
    # # # #
    # # # #

    >>> print(square(5, numeric=True, space=True))
    1 1 1 1 1
    2 2 2 2 2 
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    if len(char) != 1:
        raise ValueError("char must be a single character")
    
    if numeric and char != "*":
        raise ValueError("Cannot specify 'char' when numeric=True")
    
    if increment and not numeric:
        raise ValueError("increment can only be True when numeric=True")

    lines = []

    for i in range(1, n + 1):
        if numeric:
            if increment:
                row = [str(j) for j in range(1, n + 1)]
            else:
                row = [str(i)] * n
        else:
            row = [char] * n

        if space:
            content = " ".join(row)
        else:
            content = "".join(row)

        lines.append(content)

    return "\n".join(lines)