n = int(input())
lst = []

for i in range(n):
    lst_temp = [int(x) for x in input().split()]
    lst.append(lst_temp)


def graph(lst, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if lst[j][i] == 1 and lst[i][j] == 1:
                cnt += 1
    return cnt


print(graph(lst,n)//2)
