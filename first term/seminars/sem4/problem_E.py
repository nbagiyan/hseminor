s = input()
first = s.find('h')
last = s.rfind('h')
print(s[:last:] + s[first+1:last:1] + s[last::])
