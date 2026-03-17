from random import shuffle
import matplotlib.pyplot as plt
import math
import numpy as np

def bogosort(arr):
    count = 0
    target = sorted(arr)
    while arr != target:
        shuffle(arr)
        count += 1
    return count

n = int(input("Enter input size: "))
t = int(input("Enter number of trials: "))

fact = math.factorial(n)
normalized_counts = []
samples = []

for _ in range(t):
    arr = list(range(n))
    shuffle(arr)
    samples.append(bogosort(arr) / fact)

plt.figure(figsize=(8, 5))
plt.hist(
    samples,
    bins=30,
    density=True,         
    alpha=0.6,
    edgecolor="black",
    label="Empirical"
)

x = np.linspace(0, max(samples), 500)
plt.plot(
    x,
    np.exp(-x),
    'r',
    linewidth=2,
    label=r"Theoretical $e^{-y}$"
)

plt.xlabel(r"$y = \frac{\text{attempts}}{n!}$")
plt.ylabel("Probability density")
plt.title(f"BogoSort Attempts Distribution (n={n}, trials={t})")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
