with open(r'c:\Users\kosoy\Downloads\dataset_3363_2.txt', 'r') as inf:
    dataset = inf.readline().strip()
    result = ''
    alpha =  ''
    digit = 0
    for i in dataset:
        if i.isalpha():
            result += alpha * digit
            alpha = i
            digit = 0
        if i.isdigit():
            digit = int(str(digit) + i) 
    result += alpha * digit
    print(result)