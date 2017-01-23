s = input() 

i1 = s.find('h') 
i2 = s.rfind('h') 
i = 0 

while i < len(s): 
	if s[i] == 'h' and i != i1 and i != i2: 
		print(s[i].upper(), end = '') 
	else: 
		print(s[i], end = '') 
	i = i + 1
