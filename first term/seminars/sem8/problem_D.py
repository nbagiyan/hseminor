file = open('input.txt', 'r')
n = int(file.readline())
a = n//1000
b = n % 1000 // 100
c = n % 1000 % 100 // 10
d = n % 1000 % 100 % 10
out = open('output.txt','w')
out.write(str((a * 10 + b) - (d * 10 + c) + 1))
file.close()
out.close()
