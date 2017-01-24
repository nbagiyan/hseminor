str = input()
str1 = str[len(str)//2 + len(str)%2::] + str[:len(str)//2 + len(str)%2:]
print(str1)
