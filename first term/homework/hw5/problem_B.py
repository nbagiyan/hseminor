def pairwise_product(lst):
    maxind1 = lst.index(max(lst))
    maxind2 = -1
    maxind3 = -1
    minind1 = lst.index(min(lst))
    minind2 = -1
    if len(lst) > 3:
        for i in range(len(lst)):
            if (lst[maxind2] < lst[i] and maxind1 != i) or (maxind2 == -1 and maxind1 != i):
                maxind2 = i
            if (lst[minind2] > lst[i] and minind1 != i) or (minind2 == -1 and minind1 != i):
                minind2 = i
        for i in range(len(lst)):
            if (lst[maxind3] < lst[i] and maxind1 != i and maxind2 != i) or (maxind3 == -1 and maxind1 != i and maxind2 != i):
                maxind3 = i
        print(lst[maxind1], lst[maxind2], lst[maxind3]) if lst[maxind1] * lst[maxind2] * lst[maxind3] >= lst[minind1] * lst[minind2] * lst[maxind1] else print(lst[minind1], lst[minind2], lst[maxind1])
    else:
        print(' '.join(str(x) for x in lst))

lst = [int(x) for x in input().split()]
pairwise_product(lst)
