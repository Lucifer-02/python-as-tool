k = 100
epsilon = 0.01
guess = k / 2

# Newton-Raphson


count_steps = 0

while abs(guess**2 - k) >= epsilon:
    guess = guess - (guess**2 - k) / (2 * guess)
    count_steps += 1

print(f"Square root of {k} is about {guess} with {count_steps} steps to find")


# bisection search

count_steps = 0

high = k  # k > 0
low = 0

guess = (high + low) / 2

while abs(guess**2 - k) >= epsilon:
    if guess**2 > k:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2

    count_steps += 1

print(f"Square root of {k} is about {guess} with {count_steps} steps to find")
