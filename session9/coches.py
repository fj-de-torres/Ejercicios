import json
coches = None

""" 
#Lo hago fuera del bloque with porque las variables que declare ahí, no se ven fuera del bloque with
with open('./data/coches.json') as f:
     #Si no especifico el modo, se entiend que es modo lecura.
    coches = json.load(f)
    print(coches)
 """
def leer_json(path: str):
    coches = None
    with open(path, 'r', encoding="utf-8") as f:
        coches = json.load(f)
    return coches

def escribir_json(path: str, data) -> bool:
    assert data is not None, "¡Data no puede ser nula!!"
    resultado = None
    try:
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f)
            resultado = True
    except:
        resultado = False
    
    return resultado

coches = leer_json('./data/coches.json')
coches.append({'marca':'Toyota', 'modelo':'Prius'})

if escribir_json('./data/coches.json', coches):
    print("Operacion completada con exito")
else:
    print("Hubo un fallo en la operacion")


print(coches)

cadena_json = '[{"marca": "Seat", "modelo": "Arkana"}, {"marca": "Seat", "modelo": "Leon"}, {"marca": "Citroen", "modelo": "Berlingo"}, {"marca": "Toyota", "modelo": "Prius"}]'
#esto es lo que devuelve una API. Una cadena json.
coches_api = json.loads(cadena_json) # loads == load string. Para cargar una "cadena json"
print(coches_api)

## Dump en formato cadena:
print(json.dumps(coches_api))
print(type(json.dumps(coches_api)))