import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Chrome options setup (Screen record-ku vasadhiya window size fix panrom)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) # Script mudinjaalum browser close aagadhu
    
    # Driver initialization
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(10) # Elements load aaga 10 seconds wait pannum
    
    yield driver
    
    # driver.quit() # Recording-kaga idhai comment pannirukom. Video eduthu mudicha apram release pannikkalam.