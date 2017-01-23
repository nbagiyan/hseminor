s1, e1, s2, e2 = map(int, input().split())
if s1 > e1:
    s1, e1 = e1,s1
if s2 > e2:
    s2, e2 = e2, s2
path1 = [x for x in range(s1, e1 + 1)]
path2 = [x for x in range(s2, e2 + 1)]
path1 = set(path1)
path2 = set(path2).py
path1.intersection_update(path2)
print(len(path1))
