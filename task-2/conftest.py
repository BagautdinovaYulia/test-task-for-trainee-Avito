import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def setup_method(self):
    chrome_options = self.create_device_emulation_options("Samsung Galaxy S5")
    self.driver = webdriver.Chrome(options=chrome_options)

@pytest.fixture(scope="session")
def brouser():
    browser = self.driver
	#browser.implicitly_wait(5)
    yield browser
    browser.quit()