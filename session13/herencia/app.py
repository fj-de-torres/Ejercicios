#herencia simple multinivel
class A:
    
    def __init__(self, valor: int) -> None:
        self._data1 = valor #protected
    
    def __test_a(self):
        print('test_a')
    
    def test_publico(self):
        return "test_publico_a"
    
    def metodo_a(self):
        return 10

class B(A):
    
    def __init__(self, valor: int, valor2: int = 0) -> None:
        super().__init__(valor)
        self.__data2 = valor2
    
    def test_publico(self):
        return "test_publico_b" + super().test_publico()
    
    

class C(B):
    def test_publico(self):
        return "test_publico_c" + super().test_publico()
    
    def metodo_c(self):
        return super().metodo_a()

#b = B(10, 2)
#print(b._data1)
#print(b.test_publico())

#c = C()
#print(c._data1)
#c.test_a() incorrecto porque test_a es privado
#print(c.test_publico())




#herencia multiple

class X:
    def __init__(self, data_x: int) -> None:
        self._data_x = data_x

class Y:
    def __init__(self, data_y: int) -> None:
        self._data_y = data_y

class Z(X,Y):
    def __init__(self, data_x: int, data_y: int) -> None:
        X.__init__(self, data_x)
        Y.__init__(self, data_y)


z = Z(10,20)
#print(z._data_x, z._data_y)

#print(Z.__mro__) #method resolution order


#excepciones -> gesation de errores / situaciones excepcionales

class PapelException(Exception):pass
class InkExcpetion(Exception): pass

class Impresora:

    def imprimir(self, contenido: str, papel: bool = True, ink : bool = True):
        if papel:
            print(contenido)
        elif not ink:
            raise InkExcpetion("¡Falta tinta!")
        else:
            raise PapelException("¡Falta papel!")

epson = Impresora()
try:
    epson.imprimir('Buenos dias', True, False)
except PapelException as pex:
    print(pex)
except InkExcpetion as inx:
    print(inx)

#Profesor:
class PapelException(Exception):pass
class TonerException(Exception):pass

class Impresora:

    def imprimir(self, contenido: str, papel: bool = True, toner: bool = True):
        if papel and toner:
            print(contenido)
        else:
            if not papel:
                raise PapelException("Falta papel!")
            elif not toner:
                raise TonerException("Falta toner!")


epson = Impresora()
try:
    epson.imprimir('Buenos dias', True, False)
except (PapelException, TonerException) as ex:
    print(ex)
except Exception:
    print("Error general")
