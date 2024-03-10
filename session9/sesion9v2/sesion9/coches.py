import json

coches = None

def leer_json(path: str):
    coches = None
    with open(path, 'r', encoding="utf-8") as f:
        coches = json.load(f)
    return coches

def escribir_json(path: str, data) -> bool:
    assert data is not None, "Data ni puede ser nula!!"
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


#print(coches)

cadena_json = '[{"marca": "Seat", "modelo": "Arkana"}, {"marca": "Seat", "modelo": "Leon"}, {"marca": "Citroen", "modelo": "Berlingo"}, {"marca": "Toyota", "modelo": "Prius"}]'
coches_api = json.loads(cadena_json)
#print(coches_api)

#dump json cadena
print(json.dumps(coches_api))
print(type(json.dumps(coches_api)))



