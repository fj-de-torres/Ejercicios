class Libro:

    @property
    def titulo(self):
        return self.__titulo
    
    def __init__(self, titulo:str):
        self.__titulo = titulo


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

    


    

quijote = Libro("Don Quijote de la Mancha")
print(quijote.titulo)
