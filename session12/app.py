class Libro:

    @property
    def titulo(self):
        return self.__titulo
    
    def __init__(self, titulo:str):
        self.__titulo = titulo


class Documento:

    #atributos de clase
    numero_documentos = 0
    
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
        #atributo (privado)
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

print(Documento.numero_documentos)
print(documento_word.numero_documentos)

documento2 = Documento('Bild', 'Thomas')
print (documento2.numero_documentos)

Documento.numero_documentos = 1
print (documento2.numero_documentos)

documento2.numero_documentos = 10
print (documento2.numero_documentos)

print (documento_word.numero_documentos)




quijote = Libro("Don Quijote de la Mancha")
print(quijote.titulo)
