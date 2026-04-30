import requests

BASE = "http://localhost:8000"

def test_rate_limit():
    session = requests.Session()

    for i in range(120):
        r = session.get(BASE + "/api", timeout=1)

        if i >= 100:
            assert r.status_code == 429