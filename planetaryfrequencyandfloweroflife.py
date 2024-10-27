import numpy as np
import matplotlib.pyplot as plt

# Constants
phi = (1 + np.sqrt(5)) / 2  # Golden Ratio
base = 369

# Fibonacci sequence
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return np.array(fib_seq)

# Generate the Fibonacci sequence
n_terms = 10
fib_seq = fibonacci(n_terms)

# Generate the coordinates using base 369 and Golden Ratio
x_coords = (fib_seq % base) * phi
y_coords = (fib_seq % base) * phi

# Plotting the Flower of Life
plt.figure(figsize=(10, 10))
for i in range(len(x_coords)):
    circle = plt.Circle((x_coords[i], y_coords[i]), 1, fill=False)
    plt.gca().add_patch(circle)

# Adding planetary frequencies (example values)
planetary_frequencies = {
    'Mercury': 141.27,
    'Venus': 221.23,
    'Earth': 194.18,
    'Mars': 144.72,
    'Jupiter': 183.58,
    'Saturn': 147.85,
    'Uranus': 207.36,
    'Neptune': 211.44,
    'Pluto': 140.25
}

# Plotting planetary frequencies
for planet, freq in planetary_frequencies.items():
    plt.plot(x_coords * freq, y_coords * freq, 'o-', label=f'{planet} Frequency')

plt.title('Flower of Life with Planetary Frequencies')
plt.xlabel('X Coordinates')
plt.ylabel('Y Coordinates')
plt.legend()
plt.grid(True)
plt.show()
