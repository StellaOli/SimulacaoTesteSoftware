import unittest
from estoque import Estoque

class TestEstoque(unittest.TestCase):

    # RED → testar adicionar produto
    def test_adicionar_produto(self):
        estoque = Estoque()
        estoque.adicionar_produto("Arroz", 10)
        self.assertEqual(estoque.consultar_quantidade("Arroz"), 10)

    # RED → adicionar produto existente soma quantidade
    def test_adicionar_produto_existente(self):
        estoque = Estoque()
        estoque.adicionar_produto("Arroz", 10)
        estoque.adicionar_produto("Arroz", 5)
        self.assertEqual(estoque.consultar_quantidade("Arroz"), 15)

    # RED → não pode adicionar quantidade <= 0
    def test_adicionar_quantidade_invalida(self):
        estoque = Estoque()
        with self.assertRaises(ValueError):
            estoque.adicionar_produto("Arroz", 0)

    # RED → remover produto
    def test_remover_produto(self):
        estoque = Estoque()
        estoque.adicionar_produto("Feijao", 10)
        estoque.remover_produto("Feijao", 5)
        self.assertEqual(estoque.consultar_quantidade("Feijao"), 5)

    # RED → não pode remover mais do que tem
    def test_remover_quantidade_maior(self):
        estoque = Estoque()
        estoque.adicionar_produto("Feijao", 5)
        with self.assertRaises(ValueError):
            estoque.remover_produto("Feijao", 10)

    # RED → remover quantidade inválida
    def test_remover_quantidade_invalida(self):
        estoque = Estoque()
        with self.assertRaises(ValueError):
            estoque.remover_produto("Feijao", 0)

    # RED → consultar produto inexistente retorna 0
    def test_consultar_produto_inexistente(self):
        estoque = Estoque()
        self.assertEqual(estoque.consultar_quantidade("Macarrao"), 0)

    # RED → listar produtos
    def test_listar_produtos(self):
        estoque = Estoque()
        estoque.adicionar_produto("Arroz", 10)
        estoque.adicionar_produto("Feijao", 5)
        lista = estoque.listar_produtos()
        self.assertIn("Arroz", lista)
        self.assertIn("Feijao", lista)

    # RED → produto mais estocado
    def test_produto_mais_estocado(self):
        estoque = Estoque()
        estoque.adicionar_produto("Arroz", 10)
        estoque.adicionar_produto("Feijao", 20)
        self.assertEqual(estoque.produto_mais_estocado(), "Feijao")

    # RED → estoque vazio
    def test_produto_mais_estocado_vazio(self):
        estoque = Estoque()
        self.assertIsNone(estoque.produto_mais_estocado())

        # RED → remover produto inexistente
    def test_remover_produto_inexistente(self):
        estoque = Estoque()
        with self.assertRaises(ValueError):
            estoque.remover_produto("ProdutoX", 5)

    # RED → listar produtos não deve incluir quantidade zero
    def test_listar_produtos_sem_estoque(self):
        estoque = Estoque()
        estoque.adicionar_produto("Arroz", 10)
        estoque.remover_produto("Arroz", 10)
        self.assertNotIn("Arroz", estoque.listar_produtos())

    # RED → produto mais estocado com empate
    def test_produto_mais_estocado_empate(self):
        estoque = Estoque()
        estoque.adicionar_produto("Arroz", 10)
        estoque.adicionar_produto("Feijao", 10)
        
        resultado = estoque.produto_mais_estocado()
        self.assertIn(resultado, ["Arroz", "Feijao"])

    # RED → adicionar múltiplos produtos e verificar consistência
    def test_multiplas_operacoes(self):
        estoque = Estoque()
        estoque.adicionar_produto("Arroz", 10)
        estoque.adicionar_produto("Feijao", 5)
        estoque.remover_produto("Arroz", 3)

        self.assertEqual(estoque.consultar_quantidade("Arroz"), 7)
        self.assertEqual(estoque.consultar_quantidade("Feijao"), 5)

    # RED → remover até zerar e depois tentar remover novamente
    def test_remover_ate_zerar_e_remover_novamente(self):
        estoque = Estoque()
        estoque.adicionar_produto("Arroz", 5)
        estoque.remover_produto("Arroz", 5)

        with self.assertRaises(ValueError):
            estoque.remover_produto("Arroz", 1)


if __name__ == "__main__":
    unittest.main()