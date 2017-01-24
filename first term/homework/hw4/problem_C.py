s = input()
print(s[:s.rfind('h'):] + s[s.find('h') + 1:s.rfind('h')] + s[s.rfind('h')::])
