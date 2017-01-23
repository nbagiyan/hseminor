s = input()
n = s.find('@')
if n == -1:
    print(s)
else:
    s = s[0:n:1] + s[n+1::1]
    n = s.find('@')
    while n != -1:
        s = s[0:n:1] + s[n+1::1]
        n = s.find('@')
    print(s)
