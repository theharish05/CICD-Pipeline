from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.data == b"OK"

def test_version():
    response = client.get("/version")
    assert response.status_code == 200
