transformar_data = lambda lista : list(map(lambda item : tuple(item.split(',')) ,lista))
#Directamente hago una lista porque sé que, aunque el map es recorrible, no me devuelve una lista.
# Cuando yo tengo una lista y le pongo un * delante, reviento la lista y luego lo pueda recoger como tuplas

