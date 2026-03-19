# 🧮 Projeto Calculadora com Histórico

Este projeto foi desenvolvido como parte da disciplina **Simulação e Teste de Software**, com o objetivo de aplicar conceitos de testes de unidade, integração e uso de test doubles.

---

## 🎯 Objetivo

Implementar e testar uma calculadora que realiza operações matemáticas básicas e registra o histórico das operações em um repositório.

---

## ⚙️ Funcionalidades

A classe `Calculadora` suporta as seguintes operações:

* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão (com tratamento de divisão por zero)
* 🔼 Potência

Além disso:

* 📜 Armazena histórico das operações
* 🔍 Permite recuperar o último resultado
* 🧹 Permite limpar o histórico

---

## 🏗️ Estrutura do Projeto

```
projeto_calculadora/
│
├── src/
│   ├── calculadora.py
│   └── repositorio.py
│
├── tests/
│   ├── test_unidade.py
│   ├── test_integracao.py
│   └── test_doubles.py
│
├── requirements.txt
├── README.md
└── relatorio.md
```

---

## 🧪 Testes

O projeto contém três tipos de testes:

### 🔹 Testes de Unidade

* Validam cada método isoladamente
* Utilizam **stub (MagicMock)** para simular o repositório

### 🔹 Testes de Integração

* Testam a interação entre calculadora e repositório real
* Verificam histórico e fluxo de operações

### 🔹 Test Doubles

* **Stub:** simula comportamento
* **Mock:** verifica chamadas e argumentos
* Utilizados para detectar erros e validar interação entre componentes

---

## 🐞 Bug Encontrado

Foi identificado um bug no método `potencia`, onde o operador utilizado no histórico estava incorreto.

### ❌ Antes:

```
2 * 3 = 8
```

### ✔️ Depois:

```
2 ** 3 = 8
```

O erro foi detectado utilizando testes com **mock**.

---

## 📊 Cobertura de Código

A cobertura foi medida com `coverage.py`.

### ✔️ Resultado final:

* 📈 **100% de cobertura em `calculadora.py`**
* Todos os fluxos e exceções foram testados

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```
git clone <URL_DO_REPOSITORIO>
cd projeto_calculadora
```

---

### 2. Criar ambiente virtual (opcional)

```
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Instalar dependências

```
pip install -r requirements.txt
```

---

### 4. Executar os testes

```
python -m unittest discover tests -v
```

---

### 5. Ver cobertura de código

```
coverage run -m unittest discover tests
coverage report -m
```

Opcional:

```
coverage html
```

Abra:

```
htmlcov/index.html
```

---


## 📌 Autor

Stella 
