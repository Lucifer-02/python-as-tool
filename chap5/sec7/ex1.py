def get_min(d: dict):
    """d a dict mapping letters to ints
    returns the value in d with the key that occurs first in the
    alphabet. E.g., if d = {x = 11, b = 12}, get_min returns 12."""

    key_min = min(d.keys())

    return d[key_min]


d = {"x": 1, "o": 15, "z": 100, "c": 23}

print(get_min(d))
