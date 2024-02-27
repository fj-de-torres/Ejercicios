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
    
    @staticmethod
    def metodo_estatico(resenya: str):
        print("Reseña documento:" ,resenya)



documento_word = Documento.obtener_documento_informado('Pedro Perez')
print(documento_word.autor, documento_word.titulo, sep="--")

Documento.metodo_estatico('Documento validado')



quijote = Libro("Don Quijote de la Mancha")
print(quijote.titulo)
