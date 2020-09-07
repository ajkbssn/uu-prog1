from uu_prog1.mov_avg import smooth_a
from uu_prog1.mov_avg import smooth_b


def test_smooth():
    x = [1, 2, 6, 4, 5, 0, 1, 2]
    assert smooth_a(x, 1) == [
        1.3333333333333333,
        3.0,
        4.0,
        5.0,
        3.0,
        2.0,
        1.0,
        1.6666666666666667,
    ]
    assert smooth_a(x, 2) == [2.2, 2.8, 3.6, 3.4, 3.2, 2.4, 2.0, 1.4]
    assert smooth_b(x, 1) == [1.5, 3.0, 4.0, 5.0, 3.0, 2.0, 1.0, 1.5]
    assert smooth_b(x, 2) == [3.0, 3.25, 3.6, 3.4, 3.2, 2.4, 2.0, 1.0]
