# src/uu_prog1/mov_avg.py


def smooth(a):
    res = []
    res.append(a[0])
    for i in range(1, len(a) - 1):
        res.append(sum(a[i - 1 : i + 2]) / 3)
    res.append(a[-1])
    return res


def mean(m):
    return sum(m) / len(m)


def smooth_b(a, n):
    assert type(n) is int
    assert type(a) is list
    r = []
    for i in range(len(a)):
        r.append(mean(a[max(0, i - n) : min(len(a), 1 + i + n)]))
    return r


def smooth_a(a, n):
    assert type(n) is int
    assert type(a) is list
    r = []
    b = n * [a[0]] + a + n * [a[-1]] if a else a
    r = smooth_b(b, n)
    r = r[n:-n] if n > 0 else r
    return r


def round_list(a_list, ndigits):
    """
    returns a new list of the numbers in a_list with numbers rounded up
    to ndigits decimals.
    Example:
    round_list([1.23, 2.23, 6.88, 4, 5, 0, 1, 2], 1)
            == [1.2, 2.3, 6.9, 4.0, 5.0, 0.0, 1.0, 2.0]
    """
    assert type(a_list) is list
    assert type(ndigits) is int
    return [round(x, ndigits) for x in a_list]


def main():
    print(smooth_a([1, 2, 3], 1))
    x = [1, 2, 6, 4, 5, 0, 1, 2]
    print(smooth_a(x, 2))
    print(round_list(smooth_a(x, 1), 2))
    # == [1.33, 3.0, 4.0, 5.0, 3.0, 2.0, 1.0, 1.67]


if __name__ == "__main__":
    main()
