A = (4, 5, 6)
B = (1, 2, 3, 4)
C = (3,)
D = (1, 5, 7)
E = (2, 6, 7)
Q = []

def give_edges(x):
    return (tuple(x))

def give_verticles(x):
    for i in A:
        if i == x:
            Q.append(["A"])
    for i in B:
        if i == x:
            Q.append(["B"])
    for i in C:
        if i == x:
            Q.append(["C"])
    for i in D:
        if i == x:
            Q.append(["D"])
    for i in E:
        if i == x:
            Q.append(["E"])
    return (tuple(Q))


