from collections import Counter
import html
import re

text = """
Я к вам пишу – чего же боле?
Что я могу еще сказать?
Теперь, я знаю, в вашей воле
Меня презреньем наказать.
Но вы, к моей несчастной доле
"""

ch_pure_text = []
text = text.splitlines()
print(text)
for j in range(len(text)):

    pure_text = text[j].split()

    if len(pure_text)  == 0:
        continue
    else:

        ch_pure_text += pure_text


print(ch_pure_text)
text = ch_pure_text


reg = re.compile('[^a-zA-Zа-яА-Я]') # регулярка для удаления всех символов, кроме букв

dict_text = dict()

for i in range(len(text)):

    key = str(text[i]).lower()
    key = reg.sub('',key)
    if key in dict_text:
        dict_text[key] = dict_text[key] + 1
    else:
        dict_text[key] = 1

print(dict_text)
print(len(dict_text))
c = Counter(dict_text).most_common(10)

print(c)





#for key, values in dict_text.items():
#    print(key + ' : ' + str(values))
