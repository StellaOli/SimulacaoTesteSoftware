from locust import HttpUser, task, between

class UsuarioEcommerce(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = between(1, 3)

    @task(3)
    def ver_produto(self):
        self.client.get("/produto/1")

    @task(1)
    def comprar(self):
        self.client.post("/compra", json={"id": 1})