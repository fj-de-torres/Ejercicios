
# Clase Libro (II):

```
class Libro:
    @property
    def titulo(self):
        return self._titulo

    def __init__(self,titulo:str):
        self.__titulo = titulo
    #Responsabilidades:

```
```
class Documento:
#Atributos de clase:
    numero_documentos = 0
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo: str):
    #atributos privados
        self.__titulo = nuevo_titulo

    @property
    def autor(self):
        return self.__autor
        
    
    def __init__(self, titulo:str, autor: str):
        self.__titulo = titulo
        self.__autor = autor
        Documento.numero_documentos += 1 

    def imprimir(self):
        pass

    @classmethod
    def obtener_documento_informado(cls, autor: str):
        return cls("Titulo Dummy", autor)
```
## Método de clase:
### Patrones de diseño (GoF).

Patrones de software que sirven para lidiar con ciertos problemas y que ya han sido resueltos.

#### Patrón factoría:
Le diré al objeto que creé instancias de sí mismo. Se hace con este _método especial de clase_
```
    @classmethod
    def obtener_documento_iformado(cls,autor:str):
        return cls("Título Dummy", autor)
```
**cls:** Class Method: Palabra reservada que 
Imaginemos
Instanciamos:
#### Método estático:
No puede acceder a ninguna parte de la instancia.
```
@staticmethod
    def metodo_estatico(resenya: str):
        print("Reseña documento:" ,resenya)
```
#### Atributos de clase:
Se accede a él a través de la clases como con los métodos estáticos.
quijote = Libro("Don Quijote de la Mancha")

print(quijote.titulo)
```
documento.word = Documento.obtener_documento_informado('Pedro Pérez')
```
```
Documento.metodo_estatico('Documento validado')
```
Accedo a través de la clasea, no de una instancia
```
print(Documento.numero_documentos)
```
Puedo acceder también a través de una instancia:
```
print(documento_word.numero_documentos)
```
> 0

Es decir, es un valor que comparten todas las instancias.
Cuando una instancia cambia el atributo de clase, se convierte en atributo de instancia, y no modifica el común de la clase. Cuando se cambia el atributo desde la clase, se cambia en todas las instancias. Si lo cambia una instancia, ya se convierte en privado para esa instancia.
```
documento1 = Documento('Valores bursatiles', 'Joshua')
print(Documento.numero_documentos)
documento2 = Documento('Parrila TV', 'Pedro')
print(Documento.numero_documentos)
documento3 = Documento.obtener_documento_informado('Juan')
print(Documento.numero_documentos)
```
Resultado:

> y
> 1
> 2
> 3

