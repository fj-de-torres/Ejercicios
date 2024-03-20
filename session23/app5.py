
#Un ejemplo de composición:
#Mirar también la librería pytest: https://docs.pytest.org/en/8.0.x/how-to/index.html
import unittest
def condition():
    pass

class Address():
    def __init__(self, city, state):
        self.city = city
        self.state = state

class Owner():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Restaurant():
    def __init__(self, address, owner) -> None:
        self.address = address
        self.owner = owner

    @property
    def owner_age(self):
        return self.owner.age
    
    def summary(self):
        return f"Este restaurante pertenece a {self.owner.name} y esta ubicado en {self.address.city}"

class TestRestaurant(unittest.TestCase):
    
    #Se ejecuta una sóla vez al principio de todos los tests
    @classmethod 
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    #Se ejecuta al final de *todos* los tests
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    def setUp(self) -> None:
        self.address = Address("Santiago", "RM")
        self.owner = Owner("Juan", 30)
        self.restaurant = Restaurant(self.address, self.owner)
    
    def tearDown(self) -> None:
        print("tearDown")

    def test_owner_age(self):
        self.assertEqual(self.restaurant.owner_age, 30)

    #Cómo dejar un cierto test (como este) temporalmente sin ejección:
    @unittest.skip("No quiero probar este test ahora (el responsable está ausente)")
    def test_summary(self):
        self.assertEqual(self.restaurant.summary(), "Este restaurante pertenece a Juan y esta ubicado en Santiago")
    @unittest.skipIf(condition(),"Skip if platform is Windows")
    def test_para_windows():
        pass

if __name__ == "__main__":
    unittest.main()