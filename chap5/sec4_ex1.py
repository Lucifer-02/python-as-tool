def f(L1, L2):
    """L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""

    sum = 0
    for e in map(lambda base, power: base**power, L1, L2):
        sum += e

    return sum


print(f([1, 2], [2, 2]))
