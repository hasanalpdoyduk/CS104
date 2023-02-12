import sys
a = " "
b = 6
print(a + "O" * 5 + a)
for i in range (1, 8):
    print("O\t  O")
print(a + "O" * 5 + "\n")
print("Z" * 7)
for i in range(1, 8):
    print(a*b +"Z")
    b -= 1
print("Z" * 7 + "\n")
for i in range (1, 8):
    print("U\t  U")
print(a + "U" * 5)