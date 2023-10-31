class Int_set(object):
    """An Int_set is a set of integers"""

    # Information about the implementation (not the abstraction):
    # Value of a set is represented by a list of ints, self._vals.
    # Each int in a set occurs in self._vals exactly once.

    def __init__(self):
        """Create an empty set of integers"""
        self._vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(e)

    def union(self, other):
        """other is an Int_set
        mutates self so that it contains exactly the elemnts in self
        plus the elements in other."""

        for e in other._vals:
            if e not in self._vals:
                self.insert(e)

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return "{}"
        self._vals.sort()
        result = ""
        for e in self._vals:
            result = result + str(e) + ","
        return f"{{{result[:-1]}}}"


def test():
    set1 = Int_set()
    set2 = Int_set()

    set1.insert(1)
    set1.insert(2)
    set1.insert(3)

    set2.insert(3)
    set2.insert(5)
    set2.insert(9)

    set1.union(set2)

    print(set1)


test()
