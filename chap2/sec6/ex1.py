sum = 0

for num in range(2, 1000):
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        sum += num

print(sum)
