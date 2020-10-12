import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches


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


def createSIR2D(rows=None, columns=None):
    pass
    return False


def plot2D_SIR():
    pass
    return False
