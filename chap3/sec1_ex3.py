sum_prime = 0

for num in range(3, 20, 2):
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_prime += num

print(f"Sum of prime numbers: {sum_prime}")
