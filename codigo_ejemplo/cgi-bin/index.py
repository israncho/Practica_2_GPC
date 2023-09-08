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
print('<div class="response-box">')
print("<h1>Respuesta del formulario</h1>")

# Accede a los datos enviados por el formulario
form = cgi.FieldStorage()
user = form["user"].value
password = form["pass"].value

# Muestra los datos en una caja de estilo
print('<div class="response-item">')
print("<p><strong>User:</strong>", user, "</p>")
print("</div>")

print('<div class="response-item">')
print("<p><strong>Pass:</strong>", password, "</p>")
print("</div>")

print('</div>')  # Cierra la caja de estilo
print("</body>")
print("</html>")

