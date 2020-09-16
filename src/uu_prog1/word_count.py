# src/uu_prog1/word_count.py

import re
import sys


def print_top_n(word_dict, n, type="most"):
    if type == "most":
        top_n = sorted(word_dict.items(), key=lambda x: -x[1])
    elif type == "least":
        top_n = sorted(word_dict.items(), key=lambda x: x[1])
    else:
        print("sort type must be most or least, now items are not sorted")
        # raise exception?
    if len(top_n) > n:
        top_n = top_n[:n]
    for word, freq in top_n:
        print(word.ljust(19), str(freq).rjust(5))


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


def lines_to_list(lines):
    word_list = []
    for line in lines:
        word_list.extend(re.findall(r"[a-zA-ZåäöÅÄÖ]+", line))
        word_list = [word.lower() for word in word_list]
    return word_list


def main():
    most_n_common_words = int(
        input("How many words should be in the list of most common words?")
    )
    least_n_common_words = int(
        input("How many words should be in the list of least common words?")
    )

    with open(sys.argv[1]) as f:
        lines = f.readlines()
    list = lines_to_list(lines)
    tot_no_words = len(list)
    dict = count_words(list)
    unique_words = len(dict)
    print("Total number of words:", tot_no_words)
    print("Number of unique words:", unique_words)
    print("\nList of most common words")
    print_top_n(dict, most_n_common_words, "most")
    print("\nList of least common words")
    print_top_n(dict, least_n_common_words, "least")


if __name__ == "__main__":
    main()
