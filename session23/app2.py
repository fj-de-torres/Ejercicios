# Librearía para testear un proyecto cuando sí que nos lo piden:
import unittest

def copy_and_add_element(values,element):
    copy = values
    copy.append(element)
    return copy

class TestInequality(unittest.TestCase):
    def test_inequality(self):
        self.assertNotEqual(1,2)
        self.assertNotEqual(True,False)
        self.assertNotEqual("Hola","hola")
        self.assertNotEqual([1,2],[2,1])
    
    def test_copy_and_add_element(self):
        #AAA
        #Los tests siguen una estrategia de tripe A:
        #Arrange: preparación
        #Act: ejecuión (de la función, etc)
        #Assert: verifiación de los resultados (qué me devuelve en la fase *Act* y qué estaba esperando)
        values = [1,2,3] #(arrange)
        element = 4
        expected = [1,2,3,4]
        #Act
        result = copy_and_add_element(values,element)
        #Assert
        self.assertEqual(result,expected)
        self.assertNotEqual(values,expected,"La lista original no debe ser modificada") #Explicación de por qué espero el fallo. Saldrá en el resultado del test
        
if __name__ == "__main__":
    unittest.main()
