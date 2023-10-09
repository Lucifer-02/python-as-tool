def is_in(str1, str2):
    if (str1 in str2) or (str2 in str1):
        return True
    else:
        return False


def test_is_in(str1s, str2s):
    for str1 in str1s:
        for str2 in str2s:
            result = is_in(str1, str2)
            print(f"String 1: {str1}, String 2: {str2}, Result: {result}")


str1s = ("hoang", "a", "hskljdf")
str2s = ("hang", "abc", "inie")

test_is_in(str1s, str2s)
