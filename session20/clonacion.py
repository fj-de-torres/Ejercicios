import copy

class Taco:
    
    def __init__(self, ingredientes) -> None:
        self.ingredientes = ingredientes
    def add_souce(self, sauce):
        self.ingredientes.apppend(sauce)

taco = Taco(['carne','cebolla','clilantro','salsa'])

otro_taco = copy.copy(taco) #Copia que es otra referencia al mismo objeto de memoria
taco.ingredientes[-1] = 'guacamole'

print(taco.ingredientes)
print(otro_taco.ingredientes)

otro_taco = copy.deepcopy(taco) # ahora cambiar *otro_taco* no afecta a *taco*

taco.ingredientes[-1] = 'salsa brava'

print(taco.ingredientes)
print(otro_taco.ingredientes)

# ¿Como crear una clonación para hacer cambios en una de ellas sin que afecte a la segunda?
