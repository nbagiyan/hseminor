lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]
C = set(lst1).intersection(set(lst2))
p = list(C)
p.sort()
print(' '.join(str(x) for x in p))
