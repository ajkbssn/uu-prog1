# src/uu_prog1/python_code_ref.py

import functools
import re
import sys
import keyword


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
def lines_to_dict(lines):
    dict = {}
    for row_no, line in enumerate(lines, start=1):
        pre_comment = re.sub(r"#.*$", "", line)
        ref_list = re.findall(r"[a-z\_A-Z]+", pre_comment)
        for ref in ref_list:
            if not ref in keyword.kwlist:
                if ref in dict:
                    dict[ref].append(row_no)
                else:
                    dict[ref] = [row_no]

    return dict


def main():
    