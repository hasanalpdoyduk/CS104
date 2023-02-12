real_list = []
last_lista = []
last_listb = []
last_listc = []
last_listd = []
last_liste = []
last_listf = []
last_listg = []
last_listh = []
last_listi = []
last_listj = []
last_listk = []
last_listl = []
last_listm = []
last_listn = []


def data(s):
    s = s[:-1]
    list = s.split("  ")
    for j in list:
        if j != "":
            real_list.append(j)


with open("quotes.txt", "r") as file:
    for i in file:
        data(i)

for i in real_list[0]:
    if i != " " and i != ".":
        last_lista.append(i)
a = len(last_lista)
for i in real_list[1]:
    if i != " " and i != ".":
        last_listb.append(i)
b = len(last_listb)
for i in real_list[2]:
    if i != " " and i != ".":
        last_listc.append(i)
c = len(last_listc)
for i in real_list[3]:
    if i != " " and i != ".":
        last_listd.append(i)
d = len(last_listd)
for i in real_list[4]:
    if i != " " and i != ".":
        last_liste.append(i)
e = len(last_liste)
for i in real_list[5]:
    if i != " " and i != ".":
        last_listf.append(i)
f = len(last_listf)
for i in real_list[6]:
    if i != " " and i != ".":
        last_listg.append(i)
g = len(last_listg)
for i in real_list[7]:
    if i != " " and i != ".":
        last_listh.append(i)
h = len(last_listh)
for i in real_list[8]:
    if i != " " and i != ".":
        last_listi.append(i)
i = len(last_listi)
for i in real_list[9]:
    if i != " " and i != ".":
        last_listj.append(i)
j = len(last_listj)
for i in real_list[10]:
    if i != " " and i != ".":
        last_listk.append(i)
k = len(last_listk)
for i in real_list[11]:
    if i != " " and i != ".":
        last_listl.append(i)
l = len(last_listl)
for i in real_list[12]:
    if i != " " and i != ".":
        last_listm.append(i)
m = len(last_listm)
for i in real_list[13]:
    if i != " " and i != ".":
        last_listn.append(i)
n = len(last_listn)

with open("quotes_answ.txt", "w") as file:
    file.write("a {}\n".format(a))
    file.write("b {}\n".format(b))
    file.write("c {}\n".format(c))
    file.write("d {}\n".format(d))
    file.write("e {}\n".format(e))
    file.write("f {}\n".format(f))
    file.write("g {}\n".format(g))
    file.write("h {}\n".format(h))
    file.write("i {}\n".format(i))
    file.write("j {}\n".format(j))
    file.write("k {}\n".format(k))
    file.write("l {}\n".format(l))
    file.write("m {}\n".format(m))
    file.write("n {}\n".format(n))
