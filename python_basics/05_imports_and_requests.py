# Импорт модуля и GET-запрос

import requests

response = requests.get("https://api.github.com")
print(f"Статус-код ответа GitHub: {response.status_code}")
print(f"Тип ответа: {type(response)}")
