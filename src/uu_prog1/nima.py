import numpy as np
from epidemics import *
from matplotlib import colors
import copy

# Create function:
def createSIR2D(rows, columns, boundary=True):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2
    NON_HUMAN = 3

    # Related to the ghost element
    Newgrid = np.zeros((rows + 2, columns + 2))

    if boundary:  # if boundary is true

        for a in range(rows + 2):
            Newgrid[a, 0] = NON_HUMAN
            Newgrid[a, columns + 1] = NON_HUMAN

        for a in range(columns + 2):
            Newgrid[0, a] = NON_HUMAN
            Newgrid[rows + 1, a] = NON_HUMAN

    return Newgrid

    S = np.ndarray(shape=(rows + 2, columns + 2), dtype=float)

    for i in range(1, rows + 1):

        for j in range(1, columns + 1):
            S[i, j] = SUSCEPTIBLE

    for i in S:
        for j in S:
            if S[i, j] not in S1:
                S[i, j] = NON_HUMAN

    return S


def nimas_stuff():
    grid = createSIR2D(rows=8, columns=6, boundary=True)
    grid[5, 4] = INFECTED
    grid[4, 4] = RECOVERED
    print(grid)


def findNeighbors(grid, i, j):

    res = [grid[i - 1, j], grid[i + 1, j], grid[i, j - 1], grid[i, j + 1]]
    res2 = []
    for i in res:
        if i == SUSCEPTIBLE:
            res2.append(i)
    return res2


# print("neighbors=",findNeighbors(grid, 4, 3))
def infect(grid, i, j, alpha):

    x = np.random.rand()
    if x < alpha:
        grid[i, j] = INFECTED
        return True
    else:
        return False


# print("infected",infect(grid, 3, 4, 0.2))


def recover(grid, i, j, beta):
    x = np.random.rand()

    if grid[i, j] != INFECTED:
        return False
    else:

        if x < beta:
            grid[i, j] = RECOVERED
            return True
        else:
            return False


# print("recovered",recover(grid, 3, 4, 0.15))
def plot2D_SIR(grid):
    fig, (ax) = plt.subplots()
    plt.imshow(grid, SIRcmap(nc=4))

    # Color matching:
    SUSCEPTIBLE_patch = mpatches.Patch(
        color=(0.9490196078431372, 0.9490196078431372, 0.9490196078431372),
        label="SUSCEPTIBLE",
    )
    INFECTED_patch = mpatches.Patch(
        color=(0.8941176470588236, 0.10196078431372549, 0.10980392156862745),
        label="INFECTED",
    )
    RECOVERED_patch = mpatches.Patch(
        color=(0.21568627450980393, 0.49411764705882355, 0.7215686274509804),
        label="RECOVERED",
    )
    NON_HUMAN_patch = mpatches.Patch(
        color=(0.03515625, 0.27734375, 0.41015625), label="NON_HUMAN"
    )

    # Creating legend
    plt.legend(
        handles=[SUSCEPTIBLE_patch, INFECTED_patch, RECOVERED_patch, NON_HUMAN_patch],
        loc="upper right",
        bbox_to_anchor=(1.55, 1),
    )
    fig.savefig
    plt.show()


def nimas_testing_of_plot():
    plot2D_SIR(grid)
    # print("Grid:" , grid)


# Plotting for part C- exercise 2:

# task C
def time_step(current_grid, alpha, beta):
    new_grid = current_grid.copy()

    # find all infected in current grid
    for j in current_grid:
        for i in j:
            if i == INFECTED:
                coordinate = ()
                # how do you get the coordinates of j?
                # how did you solve the row numbers in the assignment with the python code symbols?
                print(coordinate)
                findNeighbors(new_grid, i, j)
                # why check neighbors in the new_grid? and how do you store them?
                infect(f, i, j, alpha)
                # so with the coordinates of the neighbors you should try to infect them
                # who are you infecting here? where do you save that they have/have not been infected?
                recover(f, i, j, beta)
                # and who are you trying to recover? where do you store the result?
                # should all this be within the if statement? Or where should that end?
    return current_grid  # shouldn't you return the new_grid instead?


def main():
    # Settings
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


if __name__ == "__main__":
    main()
