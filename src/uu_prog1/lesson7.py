# src/uu_prog1/lesson7.py

import functools


def debug(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


text = """Kvällens gullmoln fästet kransa.
Älvorna på ängen dansa,
och den bladbekrönta näcken
gigan rör i silverbäcken."""
test_text = "aVcdåäöÅÄÖüéáèîçÇôÜÁxyZX"
transtab = {"å": "aa", "ä": "ae", "ö": "oe", "Å": "Aa", "Ä": "Ae", "Ö": "Oe"}


@debug
def count_letters(text):
    n = 0
    for c in text:
        if c.isalpha():
            n += 1
    return f"Number of letters: {n}"


@debug
def count_swe_letters(text):
    n = 0
    for c in text:
        if c.lower() in "åäö":  # or if c in 'åäöÅÄÖ':
            n += 1
    return f"Number of Swedish letters: {n}"


@debug
def count_int_letters(text):
    int_letters = 0
    letters = 0
    for c in text:
        if c.isalpha():
            letters += 1
        if c.lower() in "abcdefghijklmnopqrstuvw":
            int_letters += 1
    return f"Number of national letters: {letters - int_letters}"


@debug
def replace_swe_letters(text):
    txt = ""
    for c in text:
        if c in transtab:
            txt += transtab[c]
        else:
            txt += c
    return txt


@debug
def letter_freq(text):
    freq = {}
    for c in text:
        if c.isalpha():
            c = c.lower()
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
    return freq


@debug
def sorted_dict(text):
    lista = list(letter_freq(text).items())
    return lista.sort()

