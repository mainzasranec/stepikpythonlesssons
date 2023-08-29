'''
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки. 
'''

numbers = [int(i) for i in input().split()]
total = 0
for number in numbers:
    total += number
print(total)