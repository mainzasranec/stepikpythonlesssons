'''
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.

Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям).

После получения файла вы можете проверить результат, обратившись к полю text.
'''
import requests
with open(r"c:\Users\kosoy\Downloads\dataset_3378_2.txt") as info:
    dataset1 = info.readline().strip()
    response = requests.get(dataset1)
with open('dataset2', 'wb') as file:
        file.write(response.content)
with open('dataset2') as info:
    line = len(info.readlines())
    print(line)