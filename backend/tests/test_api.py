import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("app.supabase_client")
def test_should_return_400_when_name_is_missing(mock_supabase, client):
    payload = {"code": "123456789"}

    response = client.post("/api/cards", json=payload)

    assert response.status_code == 400


@patch("app.supabase_client")
def test_should_return_400_when_code_is_missing(mock_supabase, client):
    payload = {"name": "Carrefour"}

    response = client.post("/api/cards", json=payload)

    assert response.status_code == 400


@patch("app.supabase_client")
def test_should_save_card_when_mocking_supabase(mock_supabase, client):
    payload = {"name": "Fnac", "code": "ABC123XYZ"}

    mock_execute = MagicMock()
    mock_execute.execute.return_value = MagicMock(data=[payload])

    mock_table = MagicMock()
    mock_table.insert.return_value = mock_execute
    mock_supabase.table.return_value = mock_table

    response = client.post("/api/cards", json=payload)

    assert response.status_code == 201
    mock_supabase.table.assert_called_with("cards")
    mock_table.insert.assert_called_once_with({"name": "Fnac", "code": "ABC123XYZ"})
