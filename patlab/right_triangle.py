def right_triangle(n, char="*"):
    if n <= 0:
        raise ValueError("n must be positive")
    return "\n".join([char * i for i in range(1, n + 1)])

