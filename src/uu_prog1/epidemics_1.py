# src/uu_prog1/epidemics.py

import numpy as np

SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2


def SIR(S0, I0, R0, a, b, T=100):
    """
    SIR model function for back seat epidemiologists.
    Takes initial susceptibles, infected, recovered, the rate of a susceptible becoming infected,
    the recovery rate, and optionally how many periods the simulation shall run.
    Returns four time series numpy arrays (susceptibles, infected, recovered, and time)
    """
    S = np.zeros(T + 1, dtype="float64")
    I = np.zeros(T + 1, dtype="float64")
    R = np.zeros(T + 1, dtype="float64")
    t = np.arange(T + 1, dtype="int64")

    S[0] = S0
    I[0] = I0
    R[0] = R0

    for n in range(1, T + 1):
        S[n] = S[n - 1] - a * S[n - 1] * I[n - 1]
        I[n] = I[n - 1] + a * S[n - 1] * I[n - 1] - b * I[n - 1]
        R[n] = R[n - 1] + b * I[n - 1]
    return S, I, R, t


def createSIR2D(rows=None, columns=None):
    pass
    return False


def plot2D_SIR():
    pass
    return False
