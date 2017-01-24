n = int(input())
lst =[]
for i in range(1, n + 1):
    lst_temp = [int(x) for x in input().split()]
    lst.append(lst_temp)


def graph(lst, n):
    temp = []
    for i in range(0, n):
        for j in range(0 + i, n):
            if lst[i][j] == 1:
                temp.append([i + 1, j + 1])
    return temp

verges = graph(lst, n)
for i in range(len(verges)):
    print(verges[i][0], verges[i][1])
