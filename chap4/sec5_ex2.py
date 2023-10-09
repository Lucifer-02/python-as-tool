def find_last(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""

    index = s.rfind(sub)

    return None if index == -1 else index


print(find_last("abcdkajdlfc", "c"))
print(find_last("abcdkajdlfc", "x"))
