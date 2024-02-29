from os import system
import dataclasses

@dataclasses.dataclass
class Operaciones:
    sumar = "+"
    restar = "-"
    multiplicar = "*"
    dividir = "/"
    
class ListaNumeros:
    def __init__(self,lista:list) -> None:
        self.lista = lista
        self.suma = 0
    
    def sumar_elemtos(self)->float:
        for numero in self.lista:
            self.suma += numero
class ListaOperaciones(ListaNumeros):
    def __init__(self, lista: list,operacion:Operaciones) -> None:
        super().__init__(lista)
        self.operacion = operacion
    def operacion(self,operacion):
        op_string=""
        for pos in range(1,len(self.lista)):
            op_string += str(self.listalista[pos])+operacion+str(self.lista[pos-1])
        return int(op_string)
        


