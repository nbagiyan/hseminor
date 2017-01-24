n = int(input())
lst = []

for i in range(n):
    lst_temp = [int(x) for x in input().split()]
    lst.append(lst_temp)


def graph(lst, n):
    for i in range(n):
        for j in range(n):
            if lst[j][i] != lst[i][j] or lst[i][i] == 1:
                return False
    return True


if graph(lst, n):
    print("YES")
else:
    print("NO")
