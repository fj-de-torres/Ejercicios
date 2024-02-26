class Libro:
    def __init__(self,titulo:str, autor:str, anio:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio
    
    #Getters:
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def anio_publicacion(self):
        return self.__anio_publicacion
    
    #Getters:

    @titulo.getter
    def titulo(self,nuevo_titulo:str) -> str:
        self.__titulo = nuevo_titulo

    @autor.getter
    def autor(self,nuevo_autor:str) -> str:
        self.__autor = nuevo_autor