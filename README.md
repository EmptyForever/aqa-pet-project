# AQA Pet Project

Учебный проект по автоматизации тестирования на Python.

## Технологии
- Python 3.14
- Pytest + Requests
- Selenium + Page Object
- pytest-html

## Структура
- `python_basics/` — упражнения по Python
- `research.md` — теория по AQA

- aqa-pet-project/
- ├── .github/workflows/          # CI/CD настройки
- ├── python_basics/              # 5 учебных скриптов по Python
- ├── tests/                      # все тесты
- │   ├── pages/                  # Page Object'ы (UI)
- │   ├── conftest.py             # фикстуры
- │   ├── test_users_api.py       # API тесты
- │   └── test_ui.py              # UI тест
- ├── .env                        # переменные окружения
- ├── .gitignore                  # игнорируемые файлы
- ├── pytest.ini                  # настройки pytest
- ├── requirements.txt            # список библиотек
- ├── research.md                 # теория
- └── README.md                   # описание проекта