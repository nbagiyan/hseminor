def max_index(lst):
    maxind = 0
    for i in range(len(lst)):
        if lst[i] >= lst[maxind]:
            maxind = i
    return maxind

lst = [int(x) for x in input().split()]
maxind = max_index(lst)
print(lst[maxind], maxind, sep = ' ')
