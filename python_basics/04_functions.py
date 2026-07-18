def check_status_code(code):
    if code == 200:
        return True
    else:
        return False


print(f"Код 200 -> {check_status_code(200)}")
print(f"Код 404 -> {check_status_code(404)}")
