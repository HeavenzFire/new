import numpy as np
import random

# Fibonacci sequence generation
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])
    return fib[n]

# Define the size of the 2D base
size = 10

# Generate the 2D dataset
data_2d = np.zeros((size, size))

# Populate the dataset with Fibonacci numbers and random variations
for i in range(size):
    for j in range(size):
        # Calculate the Fibonacci number
        fib_num = fibonacci(i + j)
        # Introduce random variation
        variation = random.uniform(-0.1, 0.1)
        data_2d[i, j] = fib_num + variation

# Display the 2D dataset
print(data_2d)
