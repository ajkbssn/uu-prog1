# tests/test_epidemics.py

import numpy as np
from epidemics import *

grid=createSIR2D(rows=8,columns=6)
grid[4,3]=INFECTED
grid[3,3]=RECOVERED
assert grid == [[0 0 0 0 0 0]
                [0 0 0 0 0 0]
                [0 0 0 0 0 0]
                [0 0 0 2 0 0]
                [0 0 0 1 0 0]
                [0 0 0 0 0 0]
                [0 0 0 0 0 0]
                [0 0 0 0 0 0]]
                