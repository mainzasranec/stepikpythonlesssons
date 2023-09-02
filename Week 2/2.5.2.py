'''
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''
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