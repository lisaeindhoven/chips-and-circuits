import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from code.helpers import  *

def visualiser(grid, gates, paths):
    """ Create a plot, showing the grid with placed gates and formed paths.
    """
    x_dim, y_dim, z_dim = [grid.x_dim, grid.y_dim, grid.z_dim]

    # Plot 3D axes
    fig = plt.figure(figsize=(x_dim, z_dim))
    ax = mplot3d.Axes3D(fig)
    ax.set_zlim(0, z_dim*0.5)
    plt.axis('off')
    
    #Create and plot grid structure
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
        x_val = [xy[0] for xy in path]
        y_val = [xy[1] for xy in path]
        plt.plot(x_val, y_val, 'blue')

    plt.show()    