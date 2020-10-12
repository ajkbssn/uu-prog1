import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import random


SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2
NON_HUMAN = 3


labelList = ["SUSCEPTIBLE", "INFECTED", "RECOVERED", "NON_HUMAN"]


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
    newcolors = (
        (0.9490196078431372, 0.9490196078431372, 0.9490196078431372),  # S
        (0.8941176470588236, 0.10196078431372549, 0.10980392156862745),  # I
        (0.21568627450980393, 0.49411764705882355, 0.7215686274509804),  # R
        (0.03515625, 0.27734375, 0.41015625),  # no human
    )
    return ListedColormap(newcolors[:nc], name="SIR")


def createSIR2D(rows, columns):
    return np.ones((rows, columns), dtype=int) * SUSCEPTIBLE


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


def plot2D_SIR(grid):
    plt.imshow(grid, cmap=SIRcmap())
    plt.colorbar()
    plt.show()


def time_step(current_grid, alpha, beta):
    rows = grid.shape[0]
    columns = grid.shape[1]
    infected = []
    infecteds_neighbors = []
    for r in range(rows):
        for c in range(columns):
            if grid(r, c) == INFECTED:
                infected.append((r, c))
                infecteds_neighbors.append(find_neighbors(current_grid, r, c))
    new_grid = current_grid.copy()
    for n in infected:
        if recover(current_grid, n[0], n[1], beta):
            new_grid[n[0], n[1]] = RECOVERED
    for n in infecteds_neighbors:
        if infect(current_grid, n[0], n[1], alpha):
            new_grid[n[0], n[1]] = INFECTED

    return new_grid


grid = createSIR2D(rows=8, columns=6)
grid[4, 3] = INFECTED
grid[3, 3] = RECOVERED
print(find_neighbors(grid, 4, 3))
plot2D_SIR(grid)
