n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append([0] * n)
for i in range(m):
    v1, v2 = map(int, input().split())
    lst[v1 - 1][v2 - 1] = lst[v2 - 1][v1 - 1] = 1
for i in lst:
    print(' '.join(str(x) for x in i))
