def isAscending(lst):
    cnt = 1
    while cnt < len(lst) and lst[cnt] > lst[cnt - 1]:
        cnt += 1
    if cnt == len(lst):
        return 'YES'
    else:
        return 'NO'

lst = [int(x) for x in input().split()]
print(isAscending(lst))
