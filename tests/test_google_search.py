
import pytest
from pages.home_page import HomePage

def test_google_search(driver):
    page = HomePage(driver)
    page.open("https://www.google.com")
    page.search("Selenium")
    assert "Selenium" in driver.title
