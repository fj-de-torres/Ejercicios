from figura_geometrica import FiguraGeometrica


class Triangulo(FiguraGeometrica):

    # @property
    # def lado1(self):
    #     return self.__lado1
    @property
    def base(self):
        return self.__base
    
    @property
    def lado2(self):
        return self.__lado2
    
    @property
    def lado3(self):
        return self.__lado3
    
    @property
    def altura(self):
        return self.__altura
    
    def __init__(self, nombre_figura: str, altura:float, base:float,lado2:float,lado3:float) -> None:
        super().__init__(nombre_figura)
        # self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
        self.__base = base
        self.__altura = altura
    
    def calcular_area(self):
        area = self.base * self.altura / 2
        return area

    def calcular_perimetro(self):
        perimetro = self.base + self.lado2 + self.lado3
        return perimetro
    