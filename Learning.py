''' Ну и хуету я сделал'''
numbers = [int(i) for i in input().split()]
newnumbers = []
if len(numbers) == 1:
    print(*numbers)
else:
    for i in range(len(numbers) - 1):
        newnumbers.append(numbers[i + 1] + numbers[i - 1])
    else:
        newnumbers.append(numbers[-2] + numbers[0])
print(*newnumbers)