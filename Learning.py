n = int(input())
x = 0
y = 0
dx = 1
dy = 0
a = [None] * n
for i in range(n):
    a[i] = [None] * n
for i in range (n * n):
    a[y][x] = i + 1
    if dx:
        test = x + dx
    else:
        test = y + dy
    if test < 0 or test == n or a[y + dy][x + dx] != None:
        dx, dy = -dy, dx
    x += dx
    y += dy
for y in range(n): 
    print(*a[y])