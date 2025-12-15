import math
import random
from collections import Counter

import matplotlib.pyplot as plt

N = 100_000
lambd = 0.01
data = [random.expovariate(lambd) for _ in range(N)] # exponential distribution: lambda = 0.01

def first_digit(x):
    x = abs(x)
    while x >= 10:
        x //= 10
    while x < 1:
        x *= 10
    return int(x)

digits = [first_digit(x) for x in data if x > 0]

count = Counter(digits)
total = sum(count.values())

observed = {d: count[d] / total for d in range(1, 10)}

benford = {d: math.log10(1 + 1 / d) for d in range(1, 10)} # Benford's Law: P(b, d) = log(1 + 1/d) / log(b)

print("Digit | Observed | Benford")
print("-" * 28)
for d in range(1, 10):
    print(f"{d:5d} | {observed[d]:8.4f} | {benford[d]:7.4f}")

plt.bar(observed.keys(), observed.values(), label = "Observed", alpha = 0.7)
plt.plot(benford.keys(), benford.values(), marker = "o", color = "red", label = "Benford")
plt.xlabel("First Digit")
plt.ylabel("Probability")
plt.title("Benford's Law Verification")
plt.legend()
plt.show()
