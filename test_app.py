from unittest.mock import patch

import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Flask"}

def test_quoted_mocked(client):
    with patch("app.get_quote_of_the_day", return_value="Mocked!"):
        response = client.get("/quote")
    assert response.status_code == 200
    assert response.json == {"quote":"Mocked!"}