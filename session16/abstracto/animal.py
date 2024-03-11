from abc import ABCMeta, abstractmethod
""" Alternativa que nos podemos encontrar:
from abc import ABC, abstractclassmethod
class Animal(ABC):
 """
class Animal(metaclass=ABCMeta):
    """Clase que representa un animal"""
    
    def walk(self):
        """Hace que el animal camine"""
        print("El animal camina")
    
    def eat(self):
        """Hace que el animal coma"""
        print("El animal come")

    @abstractmethod
    def num_legs(self):
        """Retorna la cantidad de patas del animal"""
        pass