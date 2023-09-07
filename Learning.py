a = int(input())
s = []
for i in range (a+1):
    s += [i] * i 
print(*s[:a])