import unittest

def procesar(a: int): #Como a: int es orientativo, python, no obliga, podemos hacer:
    assert isinstance(a,int), "El argumento debe ser un entero"


class IndentityTests(unittest.TestCase):
    def setUp(self) -> None:
        """Este método se ejecuta antes de cada test"""
        #return super().setUp()
        pass

    def tearDown(self) -> None:
        """Este método se ejecuta después de cada test"""
        #return super().tearDown()
        pass

    def test_identity(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]

        #self.assertEqual(a, b)
        #self.assertEqual(a, c)

        self.assertIs(a, b)
        self.assertIsNot(a, c)
        self.assertIsNot(b, c)

    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(1.0, float)
        self.assertIsInstance("Hola", str)
        self.assertIsInstance([1,2,3], list)
        self.assertIsInstance((1,2,3), tuple)
        self.assertIsInstance({1,2,3}, set)
        self.assertIsInstance({"a":1, "b":2}, dict)
        self.assertIsInstance(range(10), range)

if __name__ == "__main__":
    unittest.main()

