read_txt = open("../less_07_esy_calc/esy_calc.txt", "r")
x = 0
y = 0
q = 0
n = 0
list1 = []

for line in read_txt:
    x += 1
    list1.append(line)
    for z in line:
        if z == "\n" or z == " ":
            y += 0
        else:
            y += 1


for b in read_txt:
    for k in b:
        if k == "\n" or k == " ":
            n += 1
        else:
            n += 0
    if b == " ":
        n += 1


for f in list1:
    for z in f:
        if z == "\n" or z == " ":
            q += 0
        else:
            q += 1
    if f == " ":
        q += 0


print(y)
print(n)
print(q)
