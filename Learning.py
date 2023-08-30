''' Ну и хуету я сделал'''
numbers = [int(i) for i in input().split()]
new_numbers = []
if len(numbers) == 1:
    print (*numbers)
for j in numbers:
    if j == numbers[0]:
        a = numbers[1] + numbers[-1]
        new_numbers.append(a)
    if j == numbers[1]:
        a = numbers[0] + numbers[2]
        new_numbers.append(a)
    if j == numbers[2]:
        a = numbers[1] + numbers[3]
        new_numbers.append(a)
    if j == numbers[3]:
        a = numbers[2] + numbers[4]
        new_numbers.append(a)
    if j == numbers[4]:
        a = numbers[3] + numbers[0]
        new_numbers.append(a)
print(*new_numbers)