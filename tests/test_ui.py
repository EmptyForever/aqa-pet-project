import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage

@pytest.fixture # @pytest.fixture — Декоратор-маркер, который превращает обычную функцию в фикстуру pytest [STEM]. Он говорит фреймворку, что этот код нужно запускать автоматически для подготовки окружения тестов.
def driver(): # def driver(): — Объявление функции-фикстуры по имени driver. Теперь любой тест, у которого в аргументах будет написано слово driver, автоматически получит доступ к настроенному браузеру.
    service = Service(ChromeDriverManager().install()) # service = Service(ChromeDriverManager().install()) — Менеджер драйверов проверяет версию вашего браузера Chrome, при необходимости автоматически скачивает из интернета нужный ChromeDriver и передает путь к нему в службу Service.
    driver = webdriver.Chrome(service=service) # driver = webdriver.Chrome(service=service) — Эта строка физически запускает на компьютере чистый процесс браузера Google Chrome, управляемый через скачанный ранее ChromeDriver.
    driver.maximize_window() # driver.maximize_window() — Команда разворачивает открывшееся окно браузера на весь экран, чтобы элементы сайта не перекрывали друг друга и тест видел все кнопки.
    yield driver # yield driver — Критическая точка разделения («пауза»). Фикстура отдаёт управление и ссылку на запущенный браузер driver внутрь теста. Код фикстуры замирает и ждёт, пока тест полностью выполнится.
    driver.quit() # driver.quit() — Этап уборки (Teardown). Как только тест завершился (успешно или с ошибкой), фикстура «просыпается» и выполняет эту команду, которая закрывает браузер и полностью очищает оперативную память от процессов Chrome.

def test_login(driver):
    page = MainPage(driver)
    page.open()

    # Ждём, пока поле user-name станет кликабельным, max = 10 sec (10 - второй аргумент, любое число)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "user-name")))

    page.login("standard_user", "secret_sauce")

    # Проверка: после логина URL содержит inventory
    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url