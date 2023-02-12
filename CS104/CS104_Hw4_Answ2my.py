ISBN = list(input("Enter the numbers: "))
for i in range(len(ISBN)):
    ISBN[i] = int(ISBN[i])
correction_number = 0
for i in range(len(ISBN)):
    a = ISBN[i] * (10 - i)
    correction_number += a

print(correction_number)
if (correction_number % 11 == 0):
    print(True)
else:
    print(False)



