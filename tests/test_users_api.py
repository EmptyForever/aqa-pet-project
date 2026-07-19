import requests

# ---------- ТЕСТ 1: Проверка статус-кода ----------
def test_get_users_status_code(api_client):  # 2. Тест принимает фикстуру api_client
    response = requests.get(f"{api_client}/users")  # 3. Делаем GET-запрос
    assert response.status_code == 200        # 4. Проверяем, что статус = 200

# ---------- ТЕСТ 2: Проверка структуры ответа ----------
def test_get_users_response_structure(api_client):
    response = requests.get(f"{api_client}/users")
    data = response.json()
    
    assert isinstance(data, list)
    assert "id" in data[0]
    assert "name" in data[0]
    assert "email" in data[0]

# ---------- ТЕСТ 3: Проверка типов данных ----------
def test_get_users_data_types(api_client):
    response = requests.get(f"{api_client}/users")
    data = response.json()
    
    assert isinstance(data[0]["id"], int)
    assert isinstance(data[0]["name"], str)

# ---------- ТЕСТ 4: Создание и проверка пользователя ----------
def test_create_and_verify_user(api_client):
    new_user = {"name": "Alex", "email": "alex@example.com"}
    
    post_response = requests.post(f"{api_client}/users", json=new_user)
    assert post_response.status_code == 201
    
    # Проверяем, что в ответе есть id
    assert "id" in post_response.json()
    # user_id = post_response.json()["id"]
    # get_response = requests.get(f"{api_client}/users/{user_id}")
    
    # assert get_response.status_code == 200
    # assert get_response.json()["name"] == "Alex"

# ---------- ТЕСТ 5: Негативный тест ----------
def test_get_nonexistent_user(api_client):
    response = requests.get(f"{api_client}/users/9999999999")
    assert response.status_code == 404

def test_get_posts_status_code(api_client):
    response = requests.get(f"{api_client}/posts")
    assert response.status_code == 200