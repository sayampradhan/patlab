# pyramid.py

def centered(n, char="*"):
    """Classic centered pyramid"""
    if n <= 0:
        raise ValueError("n must be positive")
    lines = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = char * (2 * i - 1)
        lines.append(spaces + stars)
    return "\n".join(lines)


def right_aligned(n, char="*"):
    """Right-aligned pyramid (staircase style)"""
    if n <= 0:
        raise ValueError("n must be positive")
    return "\n".join([char * i for i in range(1, n + 1)])


def hollow(n, char="*"):
    """Hollow pyramid"""
    if n <= 0:
        raise ValueError("n must be positive")
    lines = []
    for i in range(1, n + 1):
        if i == 1:
            line = " " * (n - i) + char
        elif i == n:
            line = char * (2 * i - 1)
        else:
            line = " " * (n - i) + char + " " * (2 * i - 3) + char
        lines.append(line)
    return "\n".join(lines)


def numeric(n):
    """Pyramid with numbers"""
    if n <= 0:
        raise ValueError("n must be positive")
    lines = []
    for i in range(1, n + 1):
        line = " " * (n - i) + "".join(str(x) for x in range(1, i + 1))
        lines.append(line)
    return "\n".join(lines)


def make(n, variant="centered", char="*"):
    """Factory function to choose pyramid variant"""
    variants = {
        "centered": centered,
        "right": right_aligned,
        "hollow": hollow,
        "numeric": numeric,
    }
    if variant not in variants:
        raise ValueError(f"Unknown pyramid variant: {variant}. Available: {list(variants.keys())}")

    # numeric variant ignores char
    return variants[variant](n, char) if variant != "numeric" else variants[variant](n)