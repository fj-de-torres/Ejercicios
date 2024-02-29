from figura_geometrica import Figura_Geometrica

class Triangulo(Figura_Geometrica):
    def __init__(self, lado1, lado2, lado3, altura):
        """Inicializa el estado del objeto"""
        super().__init__(lado1, lado2)
        self.altura = altura
        self.lado3 = lado3

        
    def calcular_area(self):
         """calcyula y devuleve el area de esta figura """
         super().calcular_area()
         area = self.lado2 * self.altura * 0.5
         return area
