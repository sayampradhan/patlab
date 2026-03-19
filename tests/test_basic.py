import pytest
from patlab import square

def test_square_default_char():
    result = square(3)
    expected = "***\n***\n***"
    assert result == expected


def test_square_custom_char():
    result = square(4, "#")
    expected = "####\n####\n####\n####"
    assert result == expected


def test_square_size_one():
    assert square(1) == "*"


def test_square_large():
    result = square(2, "@")
    assert result == "@@\n@@"


def test_square_invalid_zero():
    with pytest.raises(ValueError, match="n must be positive"):
        square(0)


def test_square_invalid_negative():
    with pytest.raises(ValueError):
        square(-5)