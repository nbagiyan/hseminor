queue = []
command = input().strip()
while command != 'exit':
	s = command.split()
	if s[0] == 'push':
		queue.append(int(s[1]))
		print('ok')
	if s[0] == 'pop': 
		print(queue.pop(0))
	if s[0] == 'size':
		print(len(queue))
	if s[0] == 'clear':
		queue.clear()
		print('ok')
	if s[0] == 'front':
		print(queue[0])
	
	command = input()
print('bye')
