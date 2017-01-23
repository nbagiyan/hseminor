file = open('input.txt', 'r')
str = file.readline()
file.close()
for i in range(len(str)):
    if i % 3 != 0:
        out = open('output.txt', 'a')
        out.write(str[i])
        out.close()
        
