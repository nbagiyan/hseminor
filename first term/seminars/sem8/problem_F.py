file = open('input.txt', 'r')
a = int(file.readline())
b = int(file.readline())
c = int(file.readline())
d = int(file.readline())
e = int(file.readline())
file.close()
cnt = 0
for x in range(1001):
    if (x - e) != 0 and (a*(x**3) + b*(x**2) + c*x + d) == 0:
        cnt+=1
out = open('output.txt','w')
out.write(str(cnt))
out.close()
