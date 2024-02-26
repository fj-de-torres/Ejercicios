from libro import Libro

class Libreria:

    def __init__(self, *libros: tuple) -> None:
        self.__libros = list(libros)
    
    def anyadir_libro(self, libro: Libro):
        self.__libros.append(libro)

    def __len__(self): ##Método mágico
        return len(self.__libros)
    
    def __getitem__(self, pos: int):
        return self.__libros[pos]
