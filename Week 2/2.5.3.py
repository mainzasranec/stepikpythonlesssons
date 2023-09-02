'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''
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