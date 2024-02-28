#herencia simple multinivel
class A:
    
    def __init__(self) -> None:
        self._data1 = 10 #protected
    
    def __test_a(self):
        print('test_a')
    
    def test_publico(self):
        return "test_publico_a"
    
    def metodo_a(self):
        return 10

class B(A):
    def test_publico(self):
        return "test_publico_b" + super().test_publico()

class C(B):
    def test_publico(self):
        return "test_publico_c" + super().test_publico()
    
    def metodo_c(self):
        return super().metodo_a()


b = B()
print(b._data1)
print(b.test_publico())

c = C()
print(c._data1)
#c.test_a() incorrecto porque test_a es privado
print(c.test_publico())




#herencia multiple

class X:
    pass
class Y:
    pass

class Z(X,Y):
    pass