
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
    
    def __init__(self, titulo:str):
        self.__titulo = titulo

    def imprimir(self):
        pass
```

Instanciamos:

quijote = Libro("Don Quijote de la Mancha")

print(quijote.titulo)