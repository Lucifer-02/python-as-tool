def find_an_even(L: list[int]) -> int|Exception:
    """Assumes L is a list of integers
       Returns the first even number in L
       Raises ValueError if L does not contain an even number"""

    for e in L:
        if e % 2 == 0:
            return e

    raise ValueError("Not contain even number")

l = [1,6,3,3,1,7,9]
print(find_an_even(l))
