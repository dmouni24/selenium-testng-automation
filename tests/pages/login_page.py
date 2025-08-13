from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def open(self, url):
        self.driver.get(url)
    def login(self, user, pwd):
        self.driver.find_element(By.ID,"username").send_keys(user)
        self.driver.find_element(By.ID,"password").send_keys(pwd)
        self.driver.find_element(By.ID,"login").click()
