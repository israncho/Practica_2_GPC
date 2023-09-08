#!/usr/bin/python3
import cgi

# Encabezado HTTP que indica que se va a generar contenido HTML
print("Content-type: text/html\n")

# HTML generado por el script
print("<html>")
print("<head>")
print('<link rel="stylesheet" href="/css/style.css">')
print("</head>")
print("<body>")
print("<h1>Hola Mundo</h1>")

# Accede a los datos enviados por el formulario
form = cgi.FieldStorage()
user = form["user"].value
password = form["pass"].value

# Imprime los datos en un formato HTML
print("<p>User:", user, "</p>")
print("<p>Pass:", password, "</p>")

print("</body>")
print("</html>")

