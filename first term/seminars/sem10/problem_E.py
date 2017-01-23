lent = input()
lst = [int(x) for x in input().split()]
lst.sort()
print(' '.join(str(x) for x in lst))
