# Циклы и условия

users = [
    {"id": 1, "name": "Alex"},
    {"id": 2, "name": "Maria"},
    {"id": 3, "name": "John"}
]

print("Все ID пользователей:")
for user in users:
    print(f"ID: {user['id']}")

status_code = 200
if status_code == 200:
    print("Запрос выполнен успешно (200 OK)")
else:
    print(f"Ошибка! Код: {status_code}")





users2 = [
    {"id": 1, "name": "Alex"},
    {"id": 2, "name": "Maria"},
    {"id": 3, "name": "John"}
]

print("Все ID пользователей:")
for user in users2:
    print(f"ID: {user['id']}")

status_code2= 200
if status_code2 == 200:
    print("Запрос выполнен успешно (200 OK)")
else:
    print(f"Ошибка! Код: {status_code2}")
