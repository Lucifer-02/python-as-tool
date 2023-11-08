def merge(left, right, compare):
    """Assumes left and right are sorted list and compare defines an ordering on the elements.
    Returns a new sorted (by compare) list containing the same elements as (left + right) would contain.
    """

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append((left[i]))
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def test_merge():
    l1 = [1, 2, 5, 6]
    l2 = [2, 6, 8, 9, 11, 12]
    l = l1 + l2
    merged = merge(l1, l2, lambda a, b: a < b)
    l.sort()
    assert merged == l


def merge_sort(L, compare=lambda x, y: x < y):
    """Assumes L is a list, compare defines an ordering on elements of L
    Return a new sorted list with the same elements as L"""

    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def sum_tuple(t: tuple[int]) -> int:
    """Return sum of elements in tuple"""
    sum = 0
    for e in t:
        sum += e
    return sum


l = [(1, 2, 5), (5, 6), (4, 8, 5), (0, 8), (5, 4, 8, 9, 6)]
print(merge_sort(l, lambda x, y: sum_tuple(x) < sum_tuple(y)))
