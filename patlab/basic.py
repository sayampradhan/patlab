# basic.py

def square(n, char="*"):
    if n <= 0:
        raise ValueError("n must be positive")
    return "\n".join([char * n for _ in range(n)])