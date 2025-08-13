from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from tests.pages.login_page import LoginPage

def test_login_smoke():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        lp = LoginPage(driver)
        lp.open("https://example.com/login")
        lp.login("demo","secret")
        assert "dashboard" in driver.current_url.lower()
    finally:
        driver.quit()
