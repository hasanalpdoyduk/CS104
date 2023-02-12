def is_prime_number(a):
    x = 0
    for i in range(2, a + 1):
        if a % i == 0:
            x += 1
    if x == 1:
        print(bool(1))
    else:
        print(bool(0))
a = int(input("Enter a number: "))
is_prime_number(a)