'''
Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, которая выводит все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
'''
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