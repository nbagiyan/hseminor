str = input()
temp = str[str.find('h') + 1: str.rfind('h')]
for i in range(len(temp)):
    if temp[i] == 'h':
       temp = temp[:i:] + 'H' + temp[i+1::]
print(str[:str.find('h')+1:] + temp + str[str.rfind('h')::])
