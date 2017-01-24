n = int(input())
lst =[]
for i in range(1, n + 1):
    lst_temp = [int(x) for x in input().split()]
    lst.append(lst_temp)

for i in range(n):
    cnt = 0
    for j in range(n):
        if lst[i][j] == 1:
            cnt += 1
    print(cnt)
