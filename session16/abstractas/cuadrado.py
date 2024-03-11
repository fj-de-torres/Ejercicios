from session16.abstractas.figuraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):

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
    