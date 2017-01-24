stack = []
command = input().strip()
while command != 'exit':
	s = command.split()
	if s[0] == 'push':
		stack.append(int(s[1]))
		print('ok')
	if s[0] == 'pop': 
		print(stack.pop())
	if s[0] == 'size':
		print(len(stack))
	if s[0] == 'clear':
		stack.clear()
		print('ok')
	if s[0] == 'back':
		print(stack[-1])
	command = input()
print('bye')
