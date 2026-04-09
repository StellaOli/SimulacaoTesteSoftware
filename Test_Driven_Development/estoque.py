class Estoque:

    # GREEN → estrutura inicial para armazenar produtos
    def __init__(self):
        self._produtos = {}  # REFACTOR: nome claro e encapsulado (_)

    # REFACTOR → método auxiliar para evitar repetição (DRY)
    def _validar_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")

    # GREEN → adicionar produto
    def adicionar_produto(self, nome, quantidade):
        self._validar_quantidade(quantidade)

        # REFACTOR → evitar if/else usando .get()
        self._produtos[nome] = self._produtos.get(nome, 0) + quantidade

    # GREEN → remover produto
    def remover_produto(self, nome, quantidade):
        self._validar_quantidade(quantidade)

        # REFACTOR → condição simplificada (mais legível)
        if nome not in self._produtos or self._produtos[nome] < quantidade:
            raise ValueError("Quantidade insuficiente")

        self._produtos[nome] -= quantidade

    # GREEN → consultar quantidade
    def consultar_quantidade(self, nome):
        # REFACTOR → uso de .get() evita if desnecessário
        return self._produtos.get(nome, 0)

    # GREEN → listar produtos com quantidade > 0
    def listar_produtos(self):
        # REFACTOR → list comprehension (mais pythonico)
        return [nome for nome, qtd in self._produtos.items() if qtd > 0]

    # GREEN → produto mais estocado
    def produto_mais_estocado(self):
        if not self._produtos:
            return None

        # REFACTOR → uso direto de função built-in com key
        return max(self._produtos, key=self._produtos.get)