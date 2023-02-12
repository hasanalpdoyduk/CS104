r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))

matrix = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(i + j)
    matrix.append(row)

print(matrix)