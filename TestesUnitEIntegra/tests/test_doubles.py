import unittest
from unittest.mock import MagicMock
from src.calculadora import Calculadora

class TestComStub(unittest.TestCase):

    def setUp(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    def test_soma_com_stub(self):
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_stub_total(self):
        self.stub_repo.total.return_value = 0

        resultado = self.calc.multiplicar(3, 7)

        self.assertEqual(resultado, 21)    


class TestComMock(unittest.TestCase):

    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_salvar_chamado(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once() 

    def test_salvar_argumento(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_nao_chama_em_erro(self):
        with self.assertRaises(TypeError):
            self.calc.somar("x", 1)

        self.mock_repo.salvar.assert_not_called() 

    def test_mock_potencia(self):
        self.calc.potencia(2, 3)

        self.mock_repo.salvar.assert_called_once_with("2 ** 3 = 8")   

    def test_mock_somar(self):
        self.calc.somar(5, 7)
        self.mock_repo.salvar.assert_called_with("5 + 7 = 12")    

    def test_mock_subtrair(self):
        self.calc.subtrair(5, 3)
        self.mock_repo.salvar.assert_called_with("5 - 3 = 2")

    def test_mock_multiplicar(self):
        self.calc.multiplicar(4, 2)
        self.mock_repo.salvar.assert_called_with("4 * 2 = 8")

    def test_mock_dividir(self):
        self.calc.dividir(10, 2)
        self.mock_repo.salvar.assert_called_with("10 / 2 = 5.0")                                