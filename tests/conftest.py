import pytest                 # 1. Импортируем библиотеку pytest
import os                     # 2. Импортируем модуль os (для работы с переменными окружения)
from dotenv import load_dotenv # 3. Импортируем функцию load_dotenv (читает .env)

load_dotenv()                  # 4. Загружаем переменные из .env в окружение

@pytest.fixture                # 5. Декоратор — говорит pytest: "это фикстура"
def api_client():              # 6. Определяем функцию api_client
        return os.getenv("BASE_URL") # 7. Читаем из окружения значение BASE_URL и возвращаем
# """Возвращает базовый URL из .env"""
