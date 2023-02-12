import sys
for sayi in range(0, 72):
    if sayi > 1:
        for i in range(2, sayi):
            if (sayi % i) == 0:
                break
        else:
            print(sayi)