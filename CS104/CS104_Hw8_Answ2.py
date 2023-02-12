m = list()

def recursive_counter(n):
    if n == 0:
        return 0
    else:
        print(n)
        return recursive_counter(n-1)


def f(a):
    b = a[::-1]
    print(recursive_counter(5))
f([1,2,3,4])