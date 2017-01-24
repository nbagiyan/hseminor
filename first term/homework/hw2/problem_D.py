n = int(input())
lst = []
while n != 0:
    lst.append(n)
    n = int(input())
lst.sort()
print(lst[len(lst)-1])  
