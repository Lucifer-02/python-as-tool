def is_prime(num: int):
    """Assume: num > 0
    Return True if num is prime number, False if not"""

    for i in range(2, num // 2):
        if num % i == 0:
            return False

    return True

print([i for i in range(2,101) if is_prime(i)])
