import pytest
import sys
from pathlib import Path
from unittest.mock import patch

# Добавляем путь к проекту в PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

# Импортируем app и необходимые функции из backend
from backend.app import app
from backend.app import get_post  # Импортируем функцию, которую будем мокать

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Blog</title>' in response.data

def test_post_route(client):
    """Тест страницы поста"""
    # Тест с моком базы данных
    with patch('backend.app.get_post') as mock_get:  # Исправлен путь для мока
        mock_get.return_value = {
            'id': 1, 
            'title': 'Test', 
            'content': 'Content'
        }
        response = client.get('/1')
        assert response.status_code == 200
        assert b'Test' in response.data
    
    # Тест несуществующего поста
    response = client.get('/999')
    assert response.status_code == 404