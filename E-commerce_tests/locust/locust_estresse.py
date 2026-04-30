from locust import HttpUser, task, constant_pacing

class StressUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = constant_pacing(0.1)

    @task
    def acessar_produto(self):
        self.client.get("/produto/1")