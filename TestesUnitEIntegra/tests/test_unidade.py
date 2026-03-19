import unittest
from unittest.mock import MagicMock
from src.calculadora import Calculadora

class TestUnidadeCalculadora(unittest.TestCase):

    def setUp(self):
        self.repo = MagicMock()  # stub
        self.calc = Calculadora(self.repo)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 5), 5)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 3), 12)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_potencia(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)    

    def test_soma_negativos(self):
        self.assertEqual(self.calc.somar(-2, -3), -5)

    def test_subtrair_negativo(self):
        self.assertEqual(self.calc.subtrair(5, 10), -5)

    def test_multiplicar_por_zero(self):
        self.assertEqual(self.calc.multiplicar(10, 0), 0)

    def test_dividir_float(self):
        self.assertEqual(self.calc.dividir(7, 2), 3.5)                

    def test_soma_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)

    def test_subtrair_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair(5, "7")

    def test_multiplicar_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar("x", 3)

    def test_dividir_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, "y")   

    def test_potencia_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.potencia("base", 2)                             

    def test_dividir_none(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None) 

    def test_bool_como_numero(self):
        self.assertEqual(self.calc.somar(True, 2), 3)

    def test_limite_zero(self):
        self.assertEqual(self.calc.somar(0, 5), 5)

    def test_divisor_muito_pequeno(self):
        self.assertAlmostEqual(self.calc.dividir(1, 1e-10), 1e10)

    def test_potencia_negativa(self):
        self.assertAlmostEqual(self.calc.potencia(2, -1), 0.5)

    def test_potencia_fracionaria(self):
        self.assertAlmostEqual(self.calc.potencia(4, 0.5), 2)  

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)                

    def test_mensagem_divisao_zero(self):
        with self.assertRaisesRegex(ValueError, "Divisao por zero"):
            self.calc.dividir(5, 0)

    def test_mensagem_tipo_invalido(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.somar("x", 1)       

    def test_divisao_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_divisao_erro(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)         

    def test_obter_ultimo_resultado(self):
        self.calc.somar(3, 2)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 5)   

    def test_obter_resultado_inicial(self):
        self.assertEqual(self.calc.obter_ultimo_resultado(), 0)        