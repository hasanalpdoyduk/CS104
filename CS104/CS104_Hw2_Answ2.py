import sys
a = int(input("Bir sayı giriniz: "))
while a > 0:
    b = int(input("Tekrar bir sayı giriniz: "))
    if b < 0:
        print(a)
        break
    else:
        a = a + b




