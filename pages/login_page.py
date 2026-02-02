from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Attribute name maari irundhaalum, indha XPATH kandu pudichidum
        self.email_field = (By.XPATH, "//input[@type='email' or @name='email']")
        self.password_field = (By.XPATH, "//input[@type='password' or @name='password']")
        self.login_button = (By.XPATH, "//button[contains(text(),'Sign-In') or @type='submit']")

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 20)
        
        # Email fill pannum
        email_input = wait.until(EC.visibility_of_element_located(self.email_field))
        email_input.clear()
        email_input.send_keys(email)
        
        # Password fill pannum
        password_input = self.driver.find_element(*self.password_field)
        password_input.clear()
        password_input.send_keys(password)
        
        # Login button click pannum
        btn = wait.until(EC.element_to_be_clickable(self.login_button))
        btn.click()