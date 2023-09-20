x = int(input("Enter an integer greater than 2: "))
smallest_divisor = None
for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
        break

if smallest_divisor != None:
    print("largest divisor of", x, "is", x // smallest_divisor)
else:
    print(x, "is prime number")
