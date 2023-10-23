def harmonic_sum(n: int) -> float:
    """Return n!"""
    assert n > 0
    if n == 1:
        return 1

    return 1 / n + harmonic_sum(n - 1)


n = 3
print(f"Result with n={n}: {harmonic_sum(n)}")
