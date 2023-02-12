# non-recursive method
def is_palindrome(n):
    a = str(n)
    if str(n) == a[::-1]:
        print(True)
    else:
        print(False)


is_palindrome(121)


# recursive method

def counter(n):
    if n == 0:
        return 0
    else:
        return counter(n - 1)


def is_pal(n):
    a = []
    b = []
    t = -1
    m = str(n)
    x = len(m)
    if n <= 1:
        return True
    elif x % 2 == 0:
        for i in m:
            if i == m[t]:
                a.append(1)
            t = t - 1
        if len(a) == x:
            return True
        else:
            return False
    elif x % 2 == 1:
        for i in range(x-1):
            if m[i] == m[t]:
                b.append(1)
            t = t - 1
        if len(b) == x-1:
            return True
        else:
            return False
