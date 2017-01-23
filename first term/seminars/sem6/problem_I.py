n, k = map(int,input().split())
d = {}
buntday = set()
weekend = set()
for i in range(1, k+1):
    st, per = map(int,input().split())
    d[i] = (st, per)
for i in d.keys():
        buntday.update({x for x in range((d[i][0]), n + 1, d[i][1])})
for i in range(n+1):
    if (i + 1) % 7 == 0 or i % 7 == 0:
        weekend.add(i)
buntday.difference_update(weekend)
print(len(list(buntday)))
