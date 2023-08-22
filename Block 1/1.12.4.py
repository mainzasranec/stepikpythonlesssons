'''
Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.
'''
figure = str(input())
if figure == ("прямоугольник"):
    a = float(input())
    b = float(input())
    print (a * b)
if figure == ("треугольник"):
    a = float(input())
    b = float(input())
    c = float(input())
    f1 = (a + b + c) / 2
    f2 = ((f1*(f1-a)*(f1-b)*(f1-c)) ** 0.5)
    print (f2)
if figure == ("круг"):
    r = float(input())
    pi = 3.14
    print (pi * r ** 2)