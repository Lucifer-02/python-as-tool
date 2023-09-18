i = 0
max_odd = -1
while i < 10:
    num = int(input(f"Enter {i+1}th number: "))

    if num % 2 == 0:
        print("Please enter an even number")
        break
    elif max_odd < num:
        max_odd = num

    i += 1

if max_odd != -1:
    print(f"max odd number is: {max_odd}")
