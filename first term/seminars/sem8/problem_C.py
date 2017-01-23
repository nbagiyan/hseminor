file = open('input.txt', 'r')
lst1 = [int(x) for x in file.readline().split()]
lst2 = [int(x) for x in file.readline().split()]
file.close()
C = set(lst1).intersection(set(lst2))
p = list(C)
p.sort()
file = open('output.txt', 'w')
file.write(' '.join(str(x) for x in p))
file.close()
