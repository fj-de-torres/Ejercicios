from abc import ABCMeta, abstractmethod

class FiguraGeometrica(metaclass=ABCMeta):

    @property
    def nombre_figura(self):
        return self.nombre_figura
    
    def __init__(self,nombre_figura:str) -> None:
        self.__nombre_figura = nombre_figura
    @abstractmethod
    def calcular_area():
        pass
    @abstractmethod
    def calcular_perimetro():
        pass
