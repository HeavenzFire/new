import numpy as np
import matplotlib.pyplot as plt

def flower_of_life(radius=1, num_circles=19):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    for i in range(num_circles):
        angle = i * (2 * np.pi / num_circles)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        circle = plt.Circle((x, y), radius, fill=False)
        ax.add_artist(circle)

    plt.title('Flower of Life')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    flower_of_life()
