import random
import types

# Our friend bubble sort is back


def less(x, y):
    return x < y


def bubble_sort(lst, cmp=less):
    lst = lst.copy()
    n = len(lst) - 1
    for n in range(n, 0, -1):
        for i in range(n):
            if cmp(lst[i + 1], lst[i]):
                lst[i + 1], lst[i] = lst[i], lst[i + 1]
    return lst


# is_sorted tests if a list of elements are sorted (based on the 'less' comparator)
def is_sorted(a, a_orig):
    # If the lists are of different length, we have already failed the test
    if len(a) != len(a_orig):
        return False

    # Test that all elements in the original list exists in sorted list
    # and that all the elements in the sorted list exists in the original list
    for a_orig_elem in a_orig:
        if a_orig_elem not in a:
            return False
    for a_elem in a:
        if a_elem not in a_orig:
            return False

    if len(a) < 2:
        return True

    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False

    return True


# tests a sorting method by random generation of sequences of integers that are then being sorted
def test_sort(sort_method, n, sz):
    if (
        type(sort_method) != types.FunctionType
        and type(sort_method) != types.BuiltinFunctionType
    ):
        raise ValueError("The first argument must be a function.")

    # test that is_sorted can detect a non-sorted sequence, and a sorted sequence
    assert is_sorted([1, 3, 2], [1, 3, 2]) == False
    assert is_sorted([-4, 0, 4], [4, 0, -4])

    for _ in range(n):
        sz_i = random.randint(1, sz)
        a = [random.randint(-10000, 10000) for _ in range(sz_i)]

        b = sort_method(a)
        if not is_sorted(b, a):
            print(a)
            print(b)
            return False
    return True


# Program

if __name__ == "__main__":
    for i in range(100):
        assert test_sort(sorted, 20, 500), "sorted does not sort"
        assert test_sort(bubble_sort, 20, 500), "bubble_sort does not sort"

    # test_sort(5, 20, 500)

