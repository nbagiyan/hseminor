def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1

x = float(input())
y = float(input())
if int(IsPointInSquare(x, y)) == 1:
     print("YES")
else:
    print("NO")
