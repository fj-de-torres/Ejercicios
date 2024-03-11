from session16.abstractas.figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):

    """Creates an object like: object = FiguraGeometrica("nombre_figura","lado")
    where \"nombre figura\" is the proper name of a geometric figura and \"lado\" is one of its sides """

    @property
    def lado(self):
        return self.__lado
    
    def __init__(self, nombre_figura:str,lado:float) -> None:
        super().__init__(self.nombre_figura)
        self.__lado = lado
    
    def calcular_area(self) -> float:
        area = self.lado ** 2
        return area
    
    def calcular_perimetro(self) -> float:
        perimetro = 2 * self.lado
        return perimetro
    
    Cuadrado.help()