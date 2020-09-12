# src/uu_prog1/wordcount.py

import re
import sys
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


@debug
def print_top_n(word_dict, n):
    top_n = sorted(word_dict.items(), key=lambda x: -x[1])
    if len(top_n) > n:
        top_n = top_n[:n]
    for word, freq in top_n:
        print(word.ljust(19), str(freq).rjust(5))


@debug
def count_words(words, stop_words=[]):
    """
    takes list of words and returns dict with words and word count
    except words in optional stop_words list
    """
    word_dict = dict()
    for word in words:
        if word not in stop_words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict


@debug
def lines_to_list(lines):
    list = [re.findall(r"[a-zA-ZåäöÅÄÖ]+", line) for line in lines]
    return [word for word in list]


@debug
def main():
    top_n_common_words = int(
        input("How many words should be in the list of most common words?")
    )

    with open(sys.argv[1]) as f:
        lines = f.readlines()
    list = lines_to_list(lines)
    tot_no_words = len(list)
    dict = count_words(list)
    unique_words = len(dict)
    print("Total number of words:", tot_no_words)
    print("Number of unique words:", unique_words)
    print_top_n(dict, top_n_common_words)


if __name__ == "__main__":
    main()
