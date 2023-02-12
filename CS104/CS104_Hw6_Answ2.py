real_list = []

def data(s):
    s = s[:-1]
    list = s.split(" ")
    for j in list:
        if j != "" and j != "-----------------------------------------------------":
            real_list.append(j)

with open("students.txt","r") as file:
    for i in file:
        data(i)

st_number = []
a = 8
for i in range(7):
    st_number.append(real_list[a])
    a += 6
print(st_number)

name = []
a = 9
for i in range(7):
    name.append(real_list[a])
    a += 6
print(name)
surname = []
a = 10
for i in range(7):
    surname.append(real_list[a])
    a += 6
print(surname)
birth_place = []
a = 11
for i in range(7):
    birth_place.append(real_list[a])
    a += 6
print(birth_place)
department = []
a = 12
for i in range(7):
    department.append(real_list[a])
    a += 6
print(department)
gpa = []
a = 13
for i in range(7):
    gpa.append(real_list[a])
    a += 6
print(gpa)

def print_name(student_number):
    index = st_number.index('{}'.format(student_number))
    print(name[index])

def print_surname(student_number):
    index = st_number.index('{}'.format(student_number))
    print(surname[index])

def print_birth_place(student_number):
    index = st_number.index('{}'.format(student_number))
    print(birth_place[index])

def print_department(student_number):
    index = st_number.index('{}'.format(student_number))
    print(department[index])

def print_gpa(student_number):
    index = st_number.index('{}'.format(student_number))
    print(gpa[index])
