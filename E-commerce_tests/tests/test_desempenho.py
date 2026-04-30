import time

def buscar_produto():
    time.sleep(0.2)  # simula tempo de resposta da API
    return {"produto": "Notebook"}

def test_tempo_resposta(benchmark):
    resultado = benchmark(buscar_produto)
    assert resultado["produto"] == "Notebook"