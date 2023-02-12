a = []
b = []
x = int


# non-recursive method

def nr_fibonacci(n):
    for i in range(n + 1):
        if i == 0:
            a.append(1)
        elif i == 1:
            a.append(1)
        else:
            x = a[i - 2] + a[i - 1]
            a.append(x)
    return a


def nr_golden_ratio(n):
    t = float((nr_fibonacci(n)[n])) / float(nr_fibonacci(n)[n - 1])
    print(t)


nr_golden_ratio(45)


# recursive method

def r_fibonacci(n):
    if 0 <= n <= 1:
        return 1
    return r_fibonacci(n - 1) + r_fibonacci(n - 2)


def r_golden_ratio(n):
    t = float((r_fibonacci(n))) / float(r_fibonacci(n - 1))
    print(t)


r_golden_ratio(12)
