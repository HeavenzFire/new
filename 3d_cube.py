import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# Define the edges of the cube
edges = [[0, 1], [1, 2], [2, 3], [3, 0],
         [4, 5], [5, 6], [6, 7], [7, 4],
         [0, 4], [1, 5], [2, 6], [3, 7]]

# Plot the edges
for edge in edges:
    ax.plot3D(*zip(*vertices[edge]), color="b")

# Set labels
ax.set_xlabel('X (Space)')
ax.set_ylabel('Y (Space)')
ax.set_zlabel('Z (Time)')

# Save the plot
plt.savefig('3d_cube_space_time.png')

# Show the plot
plt.show()
