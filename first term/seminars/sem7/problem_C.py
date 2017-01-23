from math import sqrt

def distance(x1, y1, x2, y2):
    r = sqrt((x1-x2)**2 + (y1-y2)**2)
    return r

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
p = distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) + distance(x1, y1, x3, y3)
print(round(p, 6))
