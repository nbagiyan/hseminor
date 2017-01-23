lent = int(input())
lst = [int(x) for x in input().split()]
x = int(input())
acc = 2001
for i in range(0, lent):
    if acc > abs(lst[i] - x):
        acc = abs(lst[i] - x)
        el = lst[i]
print(el)
