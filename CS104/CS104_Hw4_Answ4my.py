knight = list(input("Enter the knight's location(if you want to write 1,3 write 13): "))
for i in range(len(knight)):
    knight[i] = int(knight[i])
a = []
b = []
a2 = []
b2 = []
list_moves = []
list_xy = [-2, -1, 1, 2]
for i in list_xy:
    a.append(knight[0] + i)
for i in list_xy:
    b.append(knight[1] + i)

for i in a:
    if 0 <= i <= 7:
        a2.append(i)
for i in b:
    if 0 <= i <= 7:
        b2.append(i)

for i in a2:
        if len(a2) == 4 and len(b2) == 4:
            if (i == a2[1]) and (i == a2[2]):
                list_moves.append([i, b2[0]])
                list_moves.append([i, b2[3]])
            else:
                list_moves.append([i, b2[1]])
                list_moves.append([i, b2[2]])
        elif len(a2) == 4 and len(b2) == 3:
            if (i == a2[1]) or (i == a2[2]):
                list_moves.append([i, b2[2]])
            else:
                list_moves.append([i, b2[0]])
                list_moves.append([i, b2[1]])
        elif len(a2) == 3 and len(b2) == 4:
            if i == a2[2]:
                list_moves.append([i, b2[1]])
                list_moves.append([i, b2[2]])
            else:
                list_moves.append([i, b2[0]])
                list_moves.append([i, b2[3]])
        elif len(a2) == 3 and len(b2) == 3:
            if (i == a2[0]) or (i == a2[1]):
                list_moves.append([i, b2[2]])
            else:
                list_moves.append([i, b2[0]])
                list_moves.append([i, b2[1]])
        elif len(a2) == 3 and len(b2) == 2:
            if i == a2[0] or i == a2[1]:
                list_moves.append([i, b2[1]])
            else:
                list_moves.append([i, b2[0]])
        elif len(a2) == 2 and len(b2) == 3:
            if i == a2[0]:
                list_moves.append([i, b2[2]])
            else:
                list_moves.append([i, b2[0]])
                list_moves.append([i, b2[1]])
        elif len(a2) == 2 and len(b2) == 2:
            if i == a2[0]:
                list_moves.append([i, b2[1]])
            else:
                list_moves.append([i, b2[0]])

print(a2)
print(b2)
print(list_moves)