x = -8

epsilon = 0.1
num_guesses = 0
low = x if x < 0 else 0
high = x if x > 0 else 0
ans = (high + low) / 2

while abs(ans**3 - x) >= epsilon:
    print("low = ", low, "high = ", high, "ans = ", ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans

    ans = (high + low) / 2

print("number of guesses = ", num_guesses)
print(ans, "is close to square root of", x)
