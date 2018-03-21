#!/usr/bin/env python3
import cgi
from collections import Counter
import html
import re

form = cgi.FieldStorage()
textarea = form.getfirst("send_textarea", "не задано") # получаем данные из формы
textarea = html.escape(textarea) # режем все знаки препинания и символы

text = str(textarea).splitlines() # разбиваем текст по строкам и запихиваем в список

ch_pure_text = []
for j in range(len(text)): # разбиваем строки на отдельные слова

    pure_text = text[j].split()

    if len(pure_text)  == 0:
        continue
    else:
        ch_pure_text += pure_text

text = ch_pure_text

reg = re.compile('[^a-zA-Zа-яА-Я]') # регулярка для удаления всех символов, кроме букв
dict_text = dict() # словарь для окончательного сбора повторяющихся данных
for i in range(len(text)): # засовываем очищенные слова в словарь

    key = str(text[i]).lower()
    key = reg.sub('', key)
    if key in dict_text:
        dict_text[key] = dict_text[key] + 1
    else:
        dict_text[key] = 1

len_dict_text = len(dict_text) # вычисляем количество уникальных слов

if len_dict_text < 11:
    c = Counter(dict_text).most_common(len_dict_text)
else:
    c = Counter(dict_text).most_common(10)



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>LEN_DICT_TEXT: {}</p>".format(str(len_dict_text)))

print("""</body>
        </html>""")