file = open('input.txt', 'r')
file = open('input.txt', 'r')
a = int(file.readline())
b = int(file.readline())
file.close()
while a < b:
    for i in range(10):
        if str(a).count(str(i)) == 3:
            out = open('output.txt','a')
            out.write(str(a) + '\n')
            out.close()
    a += 1
