def pairwise_product(lst):
    maxind1 = lst.index(max(lst))
    maxind2 = 0
    minind1 = lst.index(min(lst))
    minind2 = 0
    for i in range(len(lst)):
        if lst[maxind2] < lst[i] and maxind1 != i:
            maxind2 = i
        if lst[minind2] > lst[i] and i != minind1:
            minind2 = i
    maxarr = list([lst[maxind1], lst[maxind2]])
    minarr = list([lst[minind1], lst[minind2]])
    maxarr.sort()
    minarr.sort()
    print(' '.join(str(x) for x in maxarr)) if maxarr[0] * maxarr[1] > minarr[0] * minarr[1] else print(' '.join(str(x) for x in minarr))


lst = [int(x) for x in input().split()]
pairwise_product(lst)
