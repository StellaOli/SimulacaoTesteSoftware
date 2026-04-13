import requests
import pytest
import jsonschema

BASE_URL = "https://dummyjson.com"

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "username", "email"],
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "email": {"type": "string"}
    }
}


def obter_token():
    """Login e retorno de token JWT"""
    payload = {
        "username": "kminchelle",
        "password": "0lelplR"
    }

    resp = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert resp.status_code == 200, f"Falha no login: {resp.text}"

    return resp.json()["token"]


@pytest.fixture
def produto_criado():
    """Cria produto (DummyJSON usa produtos em vez de usuários)"""
    payload = {
        "title": "Produto Teste",
        "price": 100
    }

    resp = requests.post(f"{BASE_URL}/products/add", json=payload)
    assert resp.status_code == 200

    produto = resp.json()
    yield produto

    # DummyJSON não deleta de verdade, isso é só para simular o fluxo
    requests.delete(f"{BASE_URL}/products/{produto['id']}")


def test_get_lista_produtos():
    """GET coleção"""
    resp = requests.get(f"{BASE_URL}/products")
    assert resp.status_code == 200
    assert len(resp.json()["products"]) > 0


def test_get_produto_schema():
    """GET recurso + schema"""
    resp = requests.get(f"{BASE_URL}/products/1")
    assert resp.status_code == 200

    jsonschema.validate(instance=resp.json(), schema={
        "type": "object",
        "required": ["id", "title", "price"]
    })


def test_produto_inexistente():
    """GET inexistente"""
    resp = requests.get(f"{BASE_URL}/products/999999")
    assert resp.status_code == 404


def test_criar_produto():
    """POST"""
    payload = {
        "title": "iPhone Teste",
        "price": 999
    }

    resp = requests.post(f"{BASE_URL}/products/add", json=payload)
    assert resp.status_code == 200

    data = resp.json()
    assert "id" in data
    assert data["title"] == payload["title"]


def test_update_produto():
    """PUT"""
    payload = {
        "title": "Produto Atualizado"
    }

    resp = requests.put(f"{BASE_URL}/products/1", json=payload)
    assert resp.status_code == 200

    assert resp.json()["title"] == payload["title"]


def test_delete_produto():
    """DELETE"""
    resp = requests.delete(f"{BASE_URL}/products/1")
    assert resp.status_code == 200


# 🔐 TESTES DE AUTENTICAÇÃO 
def test_acesso_com_token():
    """Acesso autenticado"""
    token = obter_token()
    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.get(f"{BASE_URL}/auth/me", headers=headers)
    assert resp.status_code == 200


def test_acesso_sem_token():
    """Sem token → 401"""
    resp = requests.get(f"{BASE_URL}/auth/me")
    assert resp.status_code == 401


def test_fixture(produto_criado):
    """Teste com fixture"""
    assert "id" in produto_criado


def test_tempo_resposta():
    """Performance"""
    resp = requests.get(f"{BASE_URL}/products/1")
    assert resp.elapsed.total_seconds() < 2.0