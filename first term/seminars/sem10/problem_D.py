def CountSort(lst):
    maxel = max(lst) + 1
    res = [0] * maxel
    for i in lst:
        res[i] += 1
    lst = []
    for i in range(maxel):
        lst += [i] * res[i]
    return lst

lst = [int(x) for x in input().split()]
print(' '.join(str(x) for x in CountSort(lst)))
