# Ficheros
#Elemento que nos permite persistencia.

## Creación:
f = open('data/items.txt','w') #f sería el handler. Para referirme al fichero abierto
f.write("Hola Mundo") # Creará el fichero si lo abrimos en modo escritura si no existe.
#Si existe y escribo, sobreescribe lo que había. Para añadir en vez de sobre escribir, lo abro como append:
f.close()
f = open('data/items.txt','a')
f.write("Hola Python")
f.close()

def escribir_data(nombre_fichero: str,*mensajes):
    f = open(f'data/{nombre_fichero}','w')
    for mensaje in mensajes:
        f.write(f"{mensaje}\n")
    f.close()
escribir_data('items.txt','Hola','Adiós')