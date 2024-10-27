import numpy as np
import matplotlib.pyplot as plt

# Define the sequence
sequence = [369, 432, 741, 144, 221, 319, 183, 295, 405, 207]

# Generate the toroid
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

x = (3 + np.cos(phi) * np.cos(theta)) * np.cos(sequence[0] * theta)
y = (3 + np.cos(phi) * np.cos(theta)) * np.sin(sequence[0] * theta)
z = np.cos(phi) * np.sin(theta)

# Plot the toroid
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b')
plt.show()
