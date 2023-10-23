def fib(n: int):
    """return nth fibonaci number"""
    assert n > 0

    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def test_fib(nums: int) -> bool:
    assert nums > 0

    fibs = [fib(i) for i in range(1, nums + 1)]
    for i in range(nums - 2):
        if fibs[i + 2] != fibs[i] + fibs[i + 1]:
            return False

    return True


with open("fib_file", "w") as file:
    for i in range(1, 11):
        file.write(str(fib(i)) + "\n")

with open("fib_file", "r") as file:
    for _ in range(10):
        nums = int(file.readline())
        print(nums)
