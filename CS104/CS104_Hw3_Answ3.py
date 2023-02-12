def pyramid(h):
    for i in range(1, h+1):
        for j in range(1, h-i+1):
            print(end=" ")
        for j in range(1, i+1, 1):
            print(j, end="")
        for j in range(i+1, 2, -1):
            print(j - 2, end="")
        print()
    print(" "*15,"height =",h)
    get_row(h)
    return(h**2)


def get_row(h):
    if h == 1:
        print("1")
    else:
        m = 1
        s = []
        while True:
            s.append(m)
            m += 1
            if m == h:
                break
        m = h
        while True:
            s.append(m)
            m -= 1
            if m == 0:
                break
        strs = [str(ints) for ints in s]
        str_a = "".join(strs)
        fin = int(str_a)
        return(fin)

pyramid(4)
print("\n")
pyramid(2)
print("\n")
pyramid(7)