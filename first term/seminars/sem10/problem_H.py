res9 = []
res10 = []
res11 = []
f = open('input.txt', 'r', encoding='utf-8')
while 1:
    i = f.readline()
    if len(i) != 0:
        temp = [x for x in i.split()]
        if int(temp[2]) == 9:
            res9.append(int(temp[3]))
        elif int(temp[2]) == 10:
            res10.append(int(temp[3]))
        elif int(temp[2]) == 11:
            res11.append(int(temp[3]))
    else:
        break

res9.sort()
res10.sort()
res11.sort()
print(res9[len(res9) - 1], res10[len(res10) - 1], res11[len(res11) - 1])
