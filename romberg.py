import numpy as np

exact = 0.0887553
n = 5
a = 0.0
b = 3.1416 / 4

rom = np.zeros((n, n), dtype=float)

for i in range(1, n + 1):
    l = 2 ** (i - 1)
    h = (b - a) / l
    x = np.linspace(0, b, l + 1)
    y = x ** 2 * np.sin(x)
    tr = np.sum(y[1:-1])
    rom[i - 1, 0] = h * (y[0] + 2 * tr + y[-1]) / 2

for j in range(1, n):
    for i in range(j, n):
        rom[i, j] = rom[i, j - 1] + (rom[i, j - 1] - rom[i - 1, j - 1]) / (4 ** (j - 1) - 1)

print("Extrapolation table are shown below:")
print("   O(h2)       O(h4)       O(h6)       O(h8)       O(h10)      ")
print(" --------    --------    --------    --------    ---------  ")

for i in range(n):
    print(" ".join([f"{val:.8f}" for val in rom[i, :i + 1]]))

print("\nExact result is: ", exact)
print("Result by Romberg's Integration method is: ", rom[n - 1, n - 1])
print("Absolute Error is: ", abs(exact - rom[n - 1, n - 1]))
