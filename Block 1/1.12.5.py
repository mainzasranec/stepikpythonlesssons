'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
'''
a = int(input())
b = int(input())
c = int(input())
if a >= b >= c:
    print (a)
    print (c)
    print (b)
elif a <= b <= c:
    print (c)
    print (a)
    print (b)
elif b >= c >= a:
    print (b)
    print (a)
    print (c)
elif b <= c <= a:
    print (a)
    print (b)
    print (c)
elif c >= a >= b:
    print (c)
    print (b)
    print (a)
elif c <= a <= b:
    print (b)
    print (c)
    print (a)