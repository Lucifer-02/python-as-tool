x = int(input("Enter an integer: "))

root = None
pwr = None

for guess_root in range(0, abs(x) + 1):
    check = False
    guess_root = -guess_root if x < 0 else guess_root
    for guess_pwr in range(2, 6):
        if guess_root**guess_pwr == x:
            root = guess_root
            pwr = guess_pwr
            check = True
            break
    if check:
        break


if root != None and pwr != None:
    print(f"root: {root}, pwr: {pwr}")
else:
    print("root and pwr not exist")
