import json
coches = None 
#Lo hago fuera del bloque with porque las variables que declare ahí, no se ven fuera del bloque with
with open('coches.json') as f:
     #Si no especifico el modo, se entiend que es modo lecura.
    coches = json.load(f)
    print(coches)