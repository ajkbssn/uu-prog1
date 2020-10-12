# tests/test_epidemics.py

import numpy as np
from uu_prog1.epidemics import *


def test_createSIR2D():
    
    grid = createSIR2D(12, 4)
    assert type(grid) == numpy.ndarray
    assert grid.all =0