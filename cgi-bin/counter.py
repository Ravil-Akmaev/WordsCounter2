#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
textarea = form.getfirst("send_textarea", "не задано")
textarea = html.escape(textarea)

dict_textarea = dict()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXTAREA: {}</p>".format(textarea))

print("""</body>
        </html>""")