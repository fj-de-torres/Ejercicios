
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
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        self.__titulo = nuevo_titulo

    @property
    def autor(self):
        return self.__autor
        
    
    def __init__(self, titulo:str, autor: str):
        self.__titulo = titulo
        self.__autor = autor

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

quijote = Libro("Don Quijote de la Mancha")

print(quijote.titulo)
```
documento.word = Documento.obtener_documento_informado('Pedro Pérez')
```
```
Documento.metodo_estatico('Documento validado')
```
