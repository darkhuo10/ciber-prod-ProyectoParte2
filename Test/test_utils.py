import unittest
from utils import calculariva

class TestCalcularIVA(unittest.TestCase):
    def test_iva_de_100(self):
        self.assertEqual(calculariva(100), 21)

if __name__ == '__main__':
    unittest.main()
