def is_in(str1, str2):
    if (str1 in str2) or (str2 in str1):
        return True
    else:
        return False


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print(is_in(str1, str2))
