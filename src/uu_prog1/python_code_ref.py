# src/uu_prog1/python_code_ref.py

import re
import sys
import keyword


def lines_to_dict(lines):
    """
    takes a list of lines and returns a dict
    with symbols as keys and a list of line numbers as values
    """
    dict = {}
    for row_no, line in enumerate(lines, start=1):
        pre_comment = re.sub(r"#.*$", "", line)
        ref_list = re.findall(r"[a-z\_A-Z]+", pre_comment)
        for ref in ref_list:
            if ref not in keyword.kwlist:
                if ref in dict:
                    dict[ref].append(row_no)
                else:
                    dict[ref] = [row_no]
    return dict


def print_output(lines, dict):
    """
    takes a file as a list of lines
    and a dict with symbols as keys and a list of line numbers as values
    to format output to std as stated in assignment
    """
    for idx, line in enumerate(lines):
        print(str(idx).rjust(4), line.strip("\n"))
    print("\n\n")
    sd = sorted(dict.items())
    for symbol in sd:
        print(f"  {symbol[0]:18}    {symbol[1]}")


def main():
    """
    usage:
        python3 file_1 file_2
        where file_1 is this file (python_code_ref.py)
        and file_2 is a python source code file to be analysed python_code_example.txt

    output:
        prints on std output
        file_1 with line numbers and
        a reference table with symbols used in the code and corresponding line numbers

    known limits:
        disregards lines after first # mark, regardless of it being a comment or not
    """
    file_name = sys.argv[1]
    with open(file_name) as file_object:
        lines = file_object.readlines()
    dict = lines_to_dict(lines)
    print_output(lines, dict)


if __name__ == "__main__":
    main()
