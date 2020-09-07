
def smooth(a):
    res = []
    res.append(a[0])
    for i in range(1, len(a)-1):
        res.append(sum(a[i-1:i+2])/3)
    res.append(a[-1])
    return res


def mean(m):
    return sum(m) / len(m)


def smooth_b(a, n):
    r = []
    for i in range(len(a)):
        r.append(mean(a[max(0, i - n) : min(len(a), 1 + i + n)]))
    return r


def smooth_a(a, n):
    r = []
    a = [n * a[0]] + a + [n * a[-1]] if a
    r = smooth_b(a, n)
    r = r[n:-n]
    return r
