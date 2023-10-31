from typing import NewType


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

    def __add__(self, other):
        """other is an Int_set
        mutates self so that it contains exactly the elemnts in self
        plus the elements in other."""

        newSet = Int_set()

        for e in self._vals:
            newSet._vals.append(e)

        for e in other._vals:
            if e not in self._vals:
                newSet._vals.append(e)

        return newSet

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return "{}"
        self._vals.sort()
        result = ""
        for e in self._vals:
            result = result + str(e) + ","
        return f"{{{result[:-1]}}}"

    def __hash__(self) -> int:
        return id(self)


def test():
    set1 = Int_set()
    set2 = Int_set()

    set1.insert(1)
    set1.insert(2)
    set1.insert(3)

    set2.insert(3)
    set2.insert(5)
    set2.insert(9)

    set1 = set1 + set2

    print(set1, id(set1))


test()
