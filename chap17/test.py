import random
import matplotlib.pyplot as plt


random.seed(0)
data = range(0, 101)
vals = []
N = 1_000_000
for _ in range(N):
    num1 = random.choice(data)
    num2 = random.choice(data)
    num3 = random.choice(data)
    vals.append(num1 + num2 + num3)

plt.hist(vals, bins=100)
plt.show()
