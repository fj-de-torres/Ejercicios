from libro import Libro
from libreria import Libreria
from os import system


if __name__ == "__main__":
    system("cls || clear")
    quijote = Libro("Don Quijote de la Mancha", "M. Cervantes", "1575")
    historia_interminable = Libro("Historia Interminable", "M. Ende", "1984")

    libreria = Libreria(quijote, historia_interminable)

    print(len(libreria))

    libreria.anyadir_libro(Libro("El mundo azul", "J. Perez", "1991"))
    
    print(len(libreria))

    libreria.anyadir_libro(quijote + historia_interminable)

    print(len(libreria))

    libreria.listar_libros()

    ultimo_libro_entrado = libreria[-1]
    print("-"*20)
    print(ultimo_libro_entrado.titulo)