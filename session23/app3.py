import unittest

""" class TestInclussion(unittest.TestCase):
    def test_inclussion(self):
        
        #act
        result = 1 in [1,2,3]
        #assert
        self.assertIn(result, [1,2,3])
        self.assertIn("a", "Hola")
        self.assertIn(1, (1,2,3))
        self.assertIn(1, {1,2,3})
        self.assertIn("a", {"a":1, "b":2})
        self.assertIn("a", ["a", "b", "c"])
        self.assertIn(50, range(50,55)) """

def explicit_return_sum(a,b):
    return a + b

def implicit_return_sum(a,b):
    print(a + b)

class TestNone(unittest.TestCase):
    def test_sum_functions(self):
        self.assertIsNone(implicit_return_sum(1,2))
        self.assertIsNotNone(explicit_return_sum(1,2))
if __name__ == "__main__":
    unittest.main()