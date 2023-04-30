#generar html tabla de multiplicar del 6

inicio = """
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>
<table id="customers">
"""
fin = """
</table>
</body>
</html>
"""

f = open("tabla.html", "w")
f.write(inicio)

for x in range(10):
    fila = """<tr>
        <td>{}</td>
        <td>x 6 =</td>
        <td>{}</td>
        </tr>""".format(x, x * 6)
    f.write(fila)

f.write(fin)
f.close()