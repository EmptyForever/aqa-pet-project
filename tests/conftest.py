import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def api_client():
    """Возвращает базовый URL из .env"""
    return os.getenv("BASE_URL")
