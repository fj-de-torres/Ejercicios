class Libro:    

    #getters y setters

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def anio_publicacion(self):
        return self.__anio_publicacion
    
    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor

    @autor.setter
    def autor(self, valor):
        self.__autor = valor

    @anio_publicacion.setter
    def anio_publicacion(self, valor):
        self.__anio_publicacion = valor
    

    def __init__(self, titulo: str, autor: str, anio_publicacion: str ) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion

    def detalles_libro(self):
        return f"{self.titulo} - {self.autor} - {self.anio_publicacion}"
    ### Los métodos mágicos se invocan con conversión a cadena
    def __add__(self,otro_libro):
        #Ḿégodo mágico que se activa cuando uso el +:
        return Libro(f" {self.__titulo} | {otro_libro.titulo}", "Desconocido","2024")
    #devuelvo un libro + otro
    def __str__(self):
        return self.__titulo
