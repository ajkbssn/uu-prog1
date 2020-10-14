import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


import matplotlib.patches as mpatches
import random


SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2
NON_HUMAN = 3


label_list = ["SUSCEPTIBLE", "INFECTED", "RECOVERED", "NON_HUMAN"]


def SIRcmap(nc=-1):
    """ Create a discrete color map for the 2D SIR
    Parameters
    ----------
    nc : int
        number of colors to use
    Returns
    -------
    SIRcmap : matplotlib.colors.ListedColormap
        Contains 4 colors: 0-SUSCEPTIBLE, 1-INFECTED, 2-RECOVERED,
            3-NON_HUMAN
    """

    """
    newcolors = (
        (0.9490196078431372, 0.9490196078431372, 0.9490196078431372),  # S
        (0.8941176470588236, 0.10196078431372549, 0.10980392156862745),  # I
        (0.21568627450980393, 0.49411764705882355, 0.7215686274509804),  # R
        (0.03515625, 0.27734375, 0.41015625),  # no human
    )
    """
    newcolors = (
        (0.9, 0.9, 0.9),  # S
        (0.9, 0.1, 0.1),  # I
        (0.1, 0.9, 0.1),  # R
        (0.1, 0.1, 0.9),  # no human
    )
    return ListedColormap(newcolors[:nc], name="SIR")


def createSIR2D(rows, columns, boundary=False):
    if boundary:
        new_grid = np.ones((rows + 2, columns + 2)) * SUSCEPTIBLE
        for i in range(rows + 2):
            new_grid[i, 0] = NON_HUMAN
            new_grid[i, columns + 1] = NON_HUMAN
        for i in range(1, columns + 1):
            new_grid[0, i] = NON_HUMAN
            new_grid[rows + 1, i] = NON_HUMAN
    else:
        new_grid = np.ones((rows, columns), dtype=int) * SUSCEPTIBLE
    return new_grid


def find_neighbors(grid, i, j):
    rows = grid.shape[0]
    columns = grid.shape[1]
    neighbors = []
    if i >= rows or j >= columns or i < 0 or j < 0:
        raise ValueError(f"Cell number ({i}, {j}) is not in grid")
    for k in range(-1, 2, 2):
        edgerow = i + k < 0 or i + k >= rows
        edgecol = j + k < 0 or j + k >= columns
        if not edgerow:
            if grid[i + k, j] == SUSCEPTIBLE:
                neighbors.append((i + k, j))
        if not edgecol:
            if grid[i, j + k] == SUSCEPTIBLE:
                neighbors.append((i, j + k))
    return neighbors


def infect(grid, i, j, alpha):
    rows = grid.shape[0]
    columns = grid.shape[1]
    if i >= rows or j >= columns or i < 0 or j < 0:
        raise ValueError(f"Cell number ({i}, {j}) is not in grid")
    is_susceptible = grid[i, j] == SUSCEPTIBLE
    return is_susceptible and random.random() < alpha


def recover(grid, i, j, beta):
    rows = grid.shape[0]
    columns = grid.shape[1]
    if i >= rows or j >= columns or i < 0 or j < 0:
        raise ValueError(f"Cell number ({i}, {j}) is not in grid")
    is_infected = grid[i, j] == INFECTED
    return is_infected and random.random() < beta


def plot2D_SIR(grid, title=None, do_show=False):
    im = plt.imshow(grid, aspect="equal",)  # cmap=SIRcmap())
    colors = [im.cmap(im.norm(value)) for value in range(len(label_list))]
    patches = [
        mpatches.Patch(color=colors[i], label=label_list[i])
        for i in range(len(label_list))
    ]
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2)
    plt.title(title)
    if do_show:
        plt.show()


def time_step(current_grid, alpha, beta):
    rows = current_grid.shape[0]
    columns = current_grid.shape[1]
    infected = []
    infecteds_neighbors = []
    for r in range(rows):
        for c in range(columns):
            if current_grid[r, c] == INFECTED:
                infected.append((r, c))
                infecteds_neighbors.extend(find_neighbors(current_grid, r, c))
    new_grid = current_grid.copy()
    for n in infected:
        if recover(current_grid, n[0], n[1], beta):
            new_grid[n[0], n[1]] = RECOVERED
    for n in infecteds_neighbors:
        if infect(current_grid, n[0], n[1], alpha):
            new_grid[n[0], n[1]] = INFECTED
    return new_grid


def main():
    T = 50
    M = 8
    N = 6
    alpha = 0.2
    beta = 0.15

    # Initialize the grid
    grid = createSIR2D(rows=M, columns=N, boundary=True)
    grid[4, 3] = INFECTED
    grids = []
    grids.append(grid)

    # Run the simulation
    for n in range(T):
        grid = time_step(grid, alpha, beta)
        grids.append(grid)

    # Plot the results
    [plot2D_SIR(grids[t], title=f"week {t}") for t in np.arange(0, T + 1, T // 5)]
    plt.show()


if __name__ == "__main__":
    main()
