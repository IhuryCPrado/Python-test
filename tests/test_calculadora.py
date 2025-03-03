try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from calculadora import soma, subtrai

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_10(self):
        self.assertEqual(soma(-5, 5), 0)
    
    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 5, 15),
            (5, 5, 10),
            (5, 30, 35),
            (1.0, 4.0, 5.0),
            (4.4, 4, 8.4),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(4, '33')
            
    def test_subtracao_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(4, '33')

    def test_subtracao_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(4, '33')

if __name__ == '__main__':
    unittest.main(verbosity=2)
