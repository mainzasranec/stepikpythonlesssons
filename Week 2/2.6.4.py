'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''
import copy
matrix = []
inp = []
newmatrix = []
while True:
    inp = str(input())
    if inp != "end":
        inp = inp.split()
        inp = [int(i) for i in inp]
        matrix.append(inp)
    else:
        break
newmatrix = copy.deepcopy(matrix)
for i in range (len(matrix)):
    for j in range (len(matrix[i])):
        newmatrix[i][j] = (matrix[i-1][j] + matrix[(i+1) % len(matrix)][j] + matrix[i][j-1] + matrix[i][(j+1)  % len(matrix[i])])
for i in range (len(newmatrix)):
    for j in range (len(newmatrix[i])):
        print(newmatrix[i][j], end= " ")
    print()