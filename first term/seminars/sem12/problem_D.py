n, s = input().split()
n = int(n)
s = int(s)
lst =[]
for i in range(1, n + 1):
    lst_temp = [int(x) for x in input().split()]
    lst.append(lst_temp)


vist = [0] * n

def DFS(s):
    vist[s] = 1
    for i in range(n):
        if lst[s][i] == 1 and vist[i] == 0:
            DFS(i)


DFS(s - 1)
print(sum(vist))
