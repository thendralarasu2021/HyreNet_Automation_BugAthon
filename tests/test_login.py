import pytest
import time
from pages.login_page import LoginPage

def test_successful_login(driver):
    # 1. HyreNet URL-ku poo
    driver.get("https://app.hyrenet.in/")
    
    # 2. Login Page object create pannu
    login = LoginPage(driver)
    
    # 3. Credentials anupu
    login.login("hyrenet+bugathon@guvi.in", "hyrenettest@123")
    
    # 4. Wait for dashboard
    time.sleep(5)
    
    # 5. Dashboard vandhucha nu verify pannu
    assert "dashboard" in driver.current_url.lower()
    print("Thala, Automation Login Success!")