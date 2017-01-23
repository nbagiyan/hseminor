s = input()
first = s.find('f')
last = s.rfind('f')
if first != -1:
    print(first, end = ' ')
if last != -1 and last!=first:
    print(last)
elif last == -1 and first == -1:
    print()
