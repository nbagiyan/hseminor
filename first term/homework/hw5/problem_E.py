sz = int(input())
lst = [int(x) for x in input().split()]
x = int(input())
cnt = 0
i = 0
while i < sz:
    if x == lst[i]:
        cnt+=1
    i+=1
print(cnt)
