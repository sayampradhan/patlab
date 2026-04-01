from typing import Literal

def rectangle(
        length: int,
        width: int,
        char: str = "*",
        numeric: bool = False,
        increment: bool = False,
):
    """
    Generate a rectangle pattern of specified length and width.

    Parameters:
    -----------
    length : int
        The number of rows in the rectangle. Must be positive.
    width : int
        The number of columns in the rectangle. Must be positive.
    char : str, optional
        The character to use for building the rectangle. Default is '*'.
        Should be a single character.
    numeric : bool, optional
        If True, generates a numeric rectangle instead of using the specified character.
        Each row will contain the row number repeated `width` times. Default is False.
    increment : bool, optional
        If True and `numeric` is True, each row will contain incrementing numbers from 1 to `width` instead of the row number. Default is False.

    Returns:
    --------
    str
        A string representing the rectangle pattern, with each row separated by a newline.

    Raises:
    -------
    ValueError
        If `length` or `width` is not a positive integer.
    ValueError
        If `char` is not a single character.
    ValueError
        If `char` is specified while `numeric` is True.
    ValueError
        If `increment` is True while `numeric` is False.

    Examples:
    ---------
    >>> print(rectangle(3, 5))
    *****
    *****
    *****

    >>> print(rectangle(4, 6, "#"))
    ######
    ######
    ######
    ######

    >>> print(rectangle(2, 4, numeric=True))
    1111
    2222

    >>> print(rectangle(3, 5, numeric=True, increment=True))
    12345
    12345
    12345
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")
    if numeric and char != "*":
        raise ValueError("Character should not be specified when numeric is True.")
    if increment and not numeric:
        raise ValueError("Increment can only be True when numeric is True.")
    if not numeric and (len(char) != 1):
        raise ValueError("Character must be a single character.")

    pattern = []
    for i in range(1, length + 1):
        if numeric:
            if increment:
                row = ''.join(str(j) for j in range(1, width + 1))
            else:
                row = str(i) * width
        else:
            row = char * width
        pattern.append(row)

    return '\n'.join(pattern)