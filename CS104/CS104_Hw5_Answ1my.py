A = [2, 3, 4, 5, 6, 7, 8]
B = [7, 8, 9, 10]

def func1(x):
    n = ""
    e = 0
    f = 0
    for i in A:
        if i == x:
            n += "1"
        else:
           n += "0"
    for i in B:
        if i == x:
            n += "2"
        else:
            n += "3"
    for i in n:
        if i == "1":
            e += 1
    for i in n:
        if i == "2":
            f += 2
    if e == 1 and f == 2:
        return True

def func2(x):
    n = ""
    e = 0
    f = 0
    for i in A:
        if i == x:
            n += "1"
        else:
           n += "0"
    for i in B:
        if i == x:
            n += "2"
        else:
            n += "3"
    for i in n:
        if i == "1":
            e += 1
    for i in n:
        if i == "2":
            f += 2
    if e == 1 and f != 2:
        return True
    elif e != 1 and f == 2:
        return True

def func3(x):
    n = ""
    e = 0
    f = 0
    for i in A:
        if i == x:
            n += "1"
        else:
           n += "0"
    for i in B:
        if i == x:
            n += "2"
        else:
            n += "3"
    for i in n:
        if i == "1":
            e += 1
    for i in n:
        if i == "2":
            f += 2
    if e == 1 and f != 2:
        return True


def func4(x):
    n = ""
    e = 0
    f = 0
    for i in A:
        if i == x:
            n += "1"
        else:
           n += "0"
    for i in B:
        if i == x:
            n += "2"
        else:
            n += "3"
    for i in n:
        if i == "1":
            e += 1
    for i in n:
        if i == "2":
            f += 2
    if e == 1 and f != 2:
        return True
    elif e != 1 and f != 2:
        return True