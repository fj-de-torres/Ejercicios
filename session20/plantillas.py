from string import Template

clientes = {
    'cliente':'Jaime',
}

data = Template('Hola, $nombre')
print(data.substitute(nombre='Jaime'))


for clave, valor in clientes.items():
    print(data.substitute(nombre=valor))


