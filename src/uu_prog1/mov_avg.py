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
    r = r[n:-n]
    return r


print(smooth_a([1, 2, 3], 1))

