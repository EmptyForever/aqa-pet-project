import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    page = MainPage(driver)
    page.open()

    # Ждём, пока поле user-name станет кликабельным
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "user-name")))

    page.login("standard_user", "secret_sauce")

    # Проверка: после логина URL содержит inventory
    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url