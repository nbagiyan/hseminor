n = int(input())
d = dict()
for i in range(n):
    A = input().split()
    for j in range(1, len(A)):
        d[A[j]] = A[0]
m = int(input())
for i in range(m):
    s = input()
    print(d[s])
