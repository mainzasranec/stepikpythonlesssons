num = [int(i) for i in input().split()]
dbl = int(input())
newnum = []
for i in range(len(num)):
    if num[i] == dbl:
        newnum.append(i)
    if dbl not in num:
        print("Отсутствует")
        break
print(*newnum)