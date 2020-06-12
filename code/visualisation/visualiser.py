import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from code.helpers import  get_paths

# TODO implement paths as csv and list
def visualiser(grid, gates, paths):
    """ Create a plot, showing the grid with placed gates and formed paths.
    """
    x_dim, y_dim, z_dim = [grid.x_dim, grid.y_dim, grid.z_dim]

    # If input was file as string, make paths list
    if isinstance(paths, str):
        paths = get_paths(paths)

    # Plot 3D axes
    fig = plt.figure(figsize=(x_dim, z_dim))
    ax = mplot3d.Axes3D(fig)
    ax.set_zlim(0, z_dim*0.5)
    plt.axis('off')
    
    # Create and plot grid structure  ##TODO Wel of geen Grid?
    x = np.arange(0, x_dim+1, 1)
    y = np.arange(0, y_dim+2, 1)
    xx, yy = np.meshgrid(x, y)
    for z in np.arange(start=0, stop=z_dim):
        plt.plot(xx, yy, z, 'gray')
        plt.plot(yy, xx, z, 'gray')

    # Place gates
    x_scat, y_scat, z_scat = [[], [], []]
    for gate in gates:
        x_scat.append(gate.x)
        y_scat.append(gate.y)
        z_scat.append(gate.z)
    ax.scatter3D(x_scat, y_scat, z_scat, s=100, marker='s', c='red')

    # Place paths
    for path in paths:
        x_val = [xyz[0] for xyz in path]
        y_val = [xyz[1] for xyz in path]
        z_val = [xyz[2] for xyz in path]
        plt.plot(x_val, y_val, z_val)

    plt.show()    