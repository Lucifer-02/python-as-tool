def fib(n: int):
    """return Fibonacci of n"""
    assert n >= 0

    l.append(n)

    if n == 0 or n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def test_fib():
    for i in range(10):
        print(f"Fibonacci of n = {i}: {fib(i)}")


l = []
fib(5)
print(f"Number of times call fib(2) to calculate fib(5) is {l.count(2)}")
