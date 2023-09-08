matrix = []
inp = []
while True:
    inp = str(input())
    if inp != "end":
        inp = inp.split()
        inp = [int(i) for i in inp]
        matrix.append(inp)
    else:
        break
print(matrix)