import pytest
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
    page.wait_for_page_ready()
    page.login("standard_user", "secret_sauce")
    page.wait_for_inventory_page()
    assert "inventory" in driver.current_url