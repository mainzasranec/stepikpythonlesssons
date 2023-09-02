numbers = sorted([int(i) for i in input().split()])
newnumbers = []
temp = []
for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1]:
        newnumbers.append(numbers[i + 1])
for x in newnumbers:
    if x not in temp:
        temp.append(x)
print(*temp)