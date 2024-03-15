# 1er reto de la muerte:

friend_emails = {
    "Anne": "anne@example.com",
    "Brent": "brent@example.com",
    "Dan": "dan@example.com",
    "David": "david@example.com",
    "Fox": "fox@example.com",
    "Jane": "jane@example.com",
    "Kevin": "kevin@example.com",
    "Robert": "robert@example.com"
}

"""Preguntar el nombre del amigo para buscar su correo controlando los posibles errores (main errors)
Proceso de búsqueda marcando en una función
Tiempo: 8 minutos"""

def buscar_amigo(amigo:str,diccionario:dict):
    resultado = None
    if amigo in diccionario.keys():
        resultado = diccionario[amigo]
    
    return resultado
        

amigo = input("¿De qué amigo necesitas su email?")
email = buscar_amigo(amigo,friend_emails)
if email != None:
    print(f"El email de {amigo} es: {email}")
else:
    print("Amigo no encontrado")


#Correción del profesor:

def buscar_email(nombre: str) -> str:
    try:
        return friend_emails[nombre]
    except KeyError:
        return "No se encontro el correo del amigo"

if __name__ == "__main__":
    nombre = input("Entre nombre de amigo:")
    email = buscar_email(nombre)
    print(email)