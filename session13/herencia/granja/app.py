from granjero import Granjero
from vaca import Vaca
from cerdo import Cerdo
from gallina import Gallina
from perro import Perro



if __name__ == "__main__":

    granja = [
        Vaca(),
        Vaca(),
        Perro(),
        Gallina(),
        Gallina(),
        Gallina(),
        Cerdo(),
        Cerdo()
    ]
    juan = Granjero(granja)
    juan.dar_de_comer()
    #Esto es el polimorfismo. Un único mensaje a cada clase que sabe qué hacer con ello.

