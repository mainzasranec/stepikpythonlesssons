'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepik.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''
import requests
ct = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open(r'c:\Users\kosoy\Downloads\dataset_3378_3.txt', 'r', encoding='utf-8') as file:
    fs = file.readline().strip()
print(fs)
ss = requests.get(fs)
fs = ss.text
n = 1
while True:
    adr = ct + fs
    try:
        ss = requests.get(adr)
    except Exception:
        print('error Timeout')
        continue
    print(ss.status_code, n)
    if not ss.text.startswith('We'):
        fs = ss.text
        print(fs)
        n += 1
        continue
    else:
        print(ss.text)
        break