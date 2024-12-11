import pytest
from app.app import app, initialize_database

@pytest.fixture
def client():
    # Configura a aplicação para teste
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            initialize_database()
        yield client

def test_get_movies_by_year(client):
    response = client.get("/api/movies/1980")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["year"] == 1980

def test_get_winners(client):
    response = client.get("/api/movies/winners")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert any(movie["winner"] for movie in data)

def test_multiple_winners(client):
    response = client.get("/api/movies/multiple-winners")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "year" in data[0]
    assert "win_count" in data[0]  # Corrigido para usar 'win_count'

def test_intervals(client):
    response = client.get("/api/movies/intervals")
    assert response.status_code == 200
    data = response.get_json()
    assert "maximum" in data  # Corrigido para usar 'maximum'
    assert "minimum" in data  # Corrigido para usar 'minimum'
    assert len(data["maximum"]) > 0
    assert len(data["minimum"]) > 0

def test_invalid_route(client):
    response = client.get("/api/invalid-route")
    assert response.status_code == 404
    data = response.get_json()
    assert data["error"] == "Rota não encontrada"
