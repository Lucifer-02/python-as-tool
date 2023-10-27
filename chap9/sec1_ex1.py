def sum_digits(s: str) -> int:
    """Assumes s is a string
       Returns the sum of the decimal digits in s
          For example, if s is 'a2b3c' it returns 5"""

    sum = 0
    for c in s:
        try:
            sum += int(c)
        except ValueError:
            pass

    return sum

s = input("Enter something: ")
print(sum_digits(s))
