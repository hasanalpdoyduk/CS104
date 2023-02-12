a = []


def recaman_sequence(n):
    for i in range(n + 1):
        if i == 0:
            a.append(i)
        elif a[i - 1] - i > 0:
            x = a[i - 1] - i
            a.append(x)
        else:
            y = a[i - 1] + i
            a.append(y)
    print(a)


recaman_sequence(12)
