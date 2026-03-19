def right_triangle(n, char="*"):
    if n <= 0:
        raise ValueError("n must be positive")
    return "\n".join([char * i for i in range(1, n + 1)])

def inverted_right_triangle(m, char="*"):
    pass


def make(n, variant="classic", char="*"):
    """Factory function to choose pyramid variant"""
    variants = {
        "classic": right_triangle,
        "inverted": inverted_right_triangle
    }
    if variant not in variants:
        raise ValueError(f"Unknown right-triangle variant: {variant}. Available: {list(variants.keys())}")

    # numeric variant ignores char
    return variants[variant](n, char) if variant != "numeric" else variants[variant](n)