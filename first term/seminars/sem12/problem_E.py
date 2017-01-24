n = input()
n = int(n)
lst =[]
for i in range(1, n + 1):
    lst_temp = [int(x) for x in input().split()]
    lst.append(lst_temp)
s, e = map(int, input().split())

dist = [-1] * n
dist[s-1] = 0
Q = [s-1]
Qstart = 0

while len(Q) > 0:
    x = Q.pop(0)
    Qstart += 1
    for i in range(n):
        if lst[x][i]==1 :
            if dist[i] == -1:
                dist[i] = dist[x] + 1
                Q.append(i)

print(dist[e-1])
