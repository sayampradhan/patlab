# basic.py

def square(n, char="*"):
    if n <= 0:
        raise ValueError("n must be positive")
    return "\n".join([char * n for _ in range(n)])


def right_triangle(n, char="*"):
    if n <= 0:
        raise ValueError("n must be positive")
    return "\n".join([char * i for i in range(1, n + 1)])