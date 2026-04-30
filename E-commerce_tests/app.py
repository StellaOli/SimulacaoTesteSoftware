# app.py
from fastapi import FastAPI, Response

app = FastAPI()

contador = {}

@app.get("/api")
def api(response: Response):
    ip = "local"
    contador[ip] = contador.get(ip, 0) + 1

    if contador[ip] > 100:
        response.status_code = 429
        return {"erro": "rate limit"}

    return {"ok": True}

@app.get("/produto/1")
def produto():
    return {"produto": "Notebook"}

@app.post("/compra")
def compra():
    return {"status": "ok"}