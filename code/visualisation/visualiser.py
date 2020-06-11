import IPython
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from helpers import *

def visualizer(grid, gates, paths):
    """ Create a plot, showing the grid with placed gates and formed paths.
    """
    x_dim, y_dim, z_dim = [grid.x_dim, grid.y_dim, grid.z_dim]

    # Plot 3D axes
    fig = plt.figure(figsize=(x_dim, z_dim))
    ax = mplot3d.Axes3D(fig)
    ax.set_zlim(0, z_dim)
    plt.axis('off')

    # Create and plot grid structure
    x = np.arange(0, x_dim, 1)
    y = np.arange(0, x_dim, 1)
    xx, yy = np.meshgrid(x, y, sparse=False)
    for z in np.arange(start=0, stop=z_dim):
        plt.plot(xx, yy, z, 'gray')
        plt.plot(yy, xx, z, 'gray')

    # Place gates
    x_scat, y_scat, z_scat = [[], [], []]
    for gate in gates:
        x_scat.append(gate.x)
        y_scat.append(gate.y)
        z_scat.append(gate.z)
    ax.scatter3D(x_scat, y_scat, z_scat, s=100, marker='s', c='red', alpha=1)

    # Place paths
    for path in paths:
        x_val = [xy[0] for xy in path]
        y_val = [xy[1] for xy in path]
        plt.plot(x_val, y_val, 'blue')

    # # Rotate axis and update
    # for angle in range(0, 360):
    #     ax.view_init(30, angle)
    #     plt.draw()
    #     plt.pause(0.05)
    ax.view_init(20, 30)
    plt.show()

if __name__ == '__main__':
    visualizer(grid, gates, paths)

# %%