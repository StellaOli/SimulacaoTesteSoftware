# 🧪 Suíte de Testes para API REST

## 📌 API Escolhida

**DummyJSON**
https://dummyjson.com

---

## 📌 Justificativa

A API DummyJSON foi escolhida por oferecer:

* Autenticação real via JWT
* Endpoint protegido (`/auth/me`)
* Suporte a operações CRUD
* Respostas HTTP adequadas (200, 401, 404, etc.)

Isso permite validar completamente todos os requisitos da atividade prática.

---

## ⚙️ Tecnologias Utilizadas

* Python
* requests
* pytest
* jsonschema

---

## 📁 Estrutura do Projeto

```
meu-projeto/
│-- test_api.py
│-- requirements.txt
│-- README.md
```

---

## 🚀 Como Executar o Projeto

### 1. Clonar ou acessar a pasta do projeto

```bash
cd meu-projeto
```

---

### 2. Criar ambiente virtual

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar os testes

#### ▶️ Rodar todos os testes

```bash
pytest -v
```

#### ▶️ Rodar testes específicos

```bash
pytest -k acesso -v
pytest -k produto -v
pytest -k tempo -v
```

#### ▶️ Rodar um teste específico

```bash
pytest test_api.py::test_get_lista_produtos -v
```

---

## 🧪 Testes Implementados

### 🔹 Testes de Status Code

* GET lista de produtos → 200
* GET produto inexistente → 404

### 🔹 Testes de Schema

* Validação da estrutura do JSON retornado

### 🔹 Testes CRUD

* POST → criação de produto
* GET → leitura de produto
* PUT → atualização de produto
* DELETE → remoção de produto

### 🔹 Testes de Validação

* Verificação de dados retornados após criação e atualização

### 🔹 Testes de Autenticação

* Login com credenciais válidas → token JWT
* Acesso com token → 200
* Acesso sem token → 401

### 🔹 Testes com Fixture

* Criação e limpeza de dados antes/depois do teste

### 🔹 Teste de Performance

* Tempo de resposta menor que 2 segundos

---

## 🔐 Autenticação

A API utiliza autenticação baseada em **JWT (JSON Web Token)**.

### Credenciais de teste:

```json
{
  "username": "kminchelle",
  "password": "0lelplR"
}
```

---

## ⚠️ Observações Importantes

* A API DummyJSON simula persistência de dados (algumas operações não alteram permanentemente o banco).
* Operações como DELETE são apenas simuladas.
* Mesmo assim, a API retorna status codes corretos para testes.

---

## 📊 Resultado Esperado

Todos os testes devem passar com:

```bash
pytest -v
```

---

## 👨‍💻 Autor

Stella Correia.
