# 📦 Sistema de Estoque com TDD

## 📚 Disciplina

Simulação e Teste de Software

## 🎯 Objetivo da Atividade

Implementar um **Sistema de Estoque** utilizando a metodologia **TDD (Test-Driven Development)**, garantindo que todas as funcionalidades sejam guiadas por testes automatizados.

---

## 🧠 O que é TDD?

TDD (Desenvolvimento Orientado a Testes) é uma abordagem onde:

1. Primeiro escrevemos um **teste que falha (RED)**
2. Depois escrevemos o **código mínimo para passar (GREEN)**
3. Por fim, **refatoramos o código (REFACTOR)**

Esse ciclo se repete para cada nova funcionalidade.

---

## 🔁 Ciclo aplicado na atividade

### 🔴 RED

* Criação de testes antes da implementação
* Garantia de que a funcionalidade ainda não existe

### 🟢 GREEN

* Implementação do código mínimo necessário para passar no teste
* Sem antecipação de requisitos (YAGNI)

### 🔵 REFACTOR

* Melhoria do código mantendo todos os testes passando
* Aplicação de boas práticas como DRY e legibilidade

---

## ⚙️ Funcionalidades implementadas

A classe `Estoque` possui os seguintes métodos:

* `adicionar_produto(nome, quantidade)`
* `remover_produto(nome, quantidade)`
* `consultar_quantidade(nome)`
* `listar_produtos()`
* `produto_mais_estocado()`

---

## 📋 Regras de Negócio

* ❌ Não é permitido adicionar ou remover quantidade ≤ 0
* ❌ Não é possível remover mais unidades do que o disponível
* 🔄 Produtos existentes têm sua quantidade incrementada
* 📦 Produto inexistente retorna 0 ao consultar
* 📊 Retorna `None` se o estoque estiver vazio

---

## 🧪 Testes Automatizados

Arquivo: `test_estoque.py`

A suíte de testes foi desenvolvida seguindo TDD, cobrindo cenários normais, erros e casos de borda.

Os testes incluem:

* Adição de produtos
* Soma de produtos existentes
* Validação de quantidades inválidas
* Remoção de produtos
* Controle de saldo insuficiente
* Consulta de produtos inexistentes
* Listagem de produtos disponíveis
* Produto mais estocado
* Tratamento de estoque vazio
* Remoção de produto inexistente
* Exclusão de produtos com quantidade zero da listagem
* Empate no produto mais estocado
* Execução de múltiplas operações
* Tentativa de remoção após estoque zerado

✔ Total: **15 testes automatizados**
✔ Cobertura de casos normais, exceções e edge cases
✔ Todos os testes passam com sucesso

---

## 💻 Implementação

Arquivo: `estoque.py`

### Estrutura interna

* Utilização de um dicionário para armazenar produtos e quantidades:

```python
self._produtos = {}
```

---

## 🔧 Refatorações aplicadas

Durante o desenvolvimento orientado a testes, foram realizadas refatorações para melhorar a qualidade do código sem alterar seu comportamento.

### 🔹 Refatoração principal

* Criação de método auxiliar para validação:

```python
def _validar_quantidade(self, quantidade):
```

✔ Evita repetição de código (DRY)
✔ Centraliza regras de validação

---

### 🔹 Refatorações menores

✔ Uso de `.get()` para simplificar lógica:

```python
self._produtos.get(nome, 0)
```

✔ Substituição de `if/else` por expressão mais simples:

```python
self._produtos[nome] = self._produtos.get(nome, 0) + quantidade
```

✔ Uso de **list comprehension** para código mais limpo:

```python
[nome for nome, qtd in self._produtos.items() if qtd > 0]
```

✔ Simplificação de condições lógicas:

```python
if nome not in self._produtos or self._produtos[nome] < quantidade:
```

✔ Uso de função built-in para eficiência:

```python
max(self._produtos, key=self._produtos.get)
```

---

## 🚀 Como executar

1. Certifique-se de ter Python instalado
2. Execute os testes com o comando:

```bash
python -m unittest test_estoque.py
```

---

## ✅ Resultado esperado

Todos os testes devem passar:

```
...............
OK
```

---

## 📌 Conclusão

A aplicação de TDD permitiu:

* Garantir qualidade desde o início do desenvolvimento
* Criar código mais limpo, modular e testável
* Detectar erros rapidamente
* Facilitar futuras manutenções e refatorações

Além disso, refatorações incrementais melhoraram a legibilidade e reduziram duplicações, mantendo a estabilidade garantida pelos testes automatizados.

---

## 👨‍💻 Autor

Stella Oliveira
