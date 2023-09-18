'''
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.
'''
f=open(r'c:\Users\kosoy\Downloads\dataset_3363_3.txt','r') 
line=f.readline().lower()
while line:
    line=line.split()    
    s={}
    i1=0
    i2=''
    q=0
    t=[]
    min1=0
    for i in line: 
        if i not in s: 
            s[i]=1
        else:
            s[i]+=1
    for values in s.values(): 
        if values>i1:
            i1=values
    for keys , values in s.items():
        if values==i1:
            min1=keys
    for keys , values in s.items():
        if values==i1:              
            if min1>keys:
                min1=keys
    print(min1,i1)
    line=f.readline().lower()
f.close()