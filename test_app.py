import unittest
from app import sumar

class TestApp(unittest.TestCase):
    def test_suma_correcta(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(sumar(-1, -1), -2)

    def test_suma_cero(self):
        self.assertEqual(sumar(0, 0), 0)

if __name__ == '__main__':
    unittest.main()