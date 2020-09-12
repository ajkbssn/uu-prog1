# tests/test_lesson7.py

from uu_prog1.lesson7 import *


def test_sorted_dict():

    expected = [
        ("a", 8),
        ("b", 3),
        ("c", 3),
        ("d", 3),
        ("e", 8),
        ("f", 1),
        ("g", 4),
        ("h", 1),
        ("i", 3),
        ("k", 5),
        ("l", 8),
        ("m", 1),
        ("n", 13),
        ("o", 3),
        ("p", 1),
        ("r", 6),
        ("s", 5),
        ("t", 3),
        ("u", 1),
        ("v", 3),
        ("ä", 6),
        ("å", 1),
        ("ö", 2),
    ]

    assert sorted_dict(text) == expected


def test_letter_freq():
    expected = {
        "k": 5,
        "v": 3,
        "ä": 6,
        "l": 8,
        "e": 8,
        "n": 13,
        "s": 5,
        "g": 4,
        "u": 1,
        "m": 1,
        "o": 3,
        "f": 1,
        "t": 3,
        "r": 6,
        "a": 8,
        "p": 1,
        "å": 1,
        "d": 3,
        "c": 3,
        "h": 1,
        "b": 3,
        "ö": 2,
        "i": 3,
    }
    assert letter_freq(text) == expected
