# Neu sua (mid + 1) -> (mid) thi phep '//' se lap vo han

def search(L, e):
    """Assumes L is a list, the elements of which are in ascending order.
    Returns True if e is in L and False otherwise"""

    def bin_search(L, e, low, high):
        # Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        print(L[mid])
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left search
                return False
            else:
                return bin_search(L, e, low, mid - 1)
        else:
            return bin_search(L, e, mid, high)

    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)


L = [1, 3, 4, 5, 6, 8, 11, 12, 18, 19, 52]
print(search(L, 1))
