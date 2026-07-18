# Списки и словари

user = {
    "name": "Alex",
    "id": 1,
    "email": "alex@example.com"
}

users_list = [
    {"id": 1, "name": "Alex"},
    {"id": 2, "name": "Maria"}
]

print(f"Имя пользователя из словаря: {user['name']}")
print(f"Первый пользователь в списке: {users_list[0]['name']}")
print(f"Весь список: {users_list}")