import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class PythonOrgSearchChrome(pytest.TestCase):

	def setup_method(self):
		mobile_emulation = {"deviceName": "Samsung Galaxy S5"}
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
		self.driver = webdriver.Chrome(executable_path='/tools/chromedriver', chrome_options=chrome_options)

	@pytest.fixture
	def brouser():
    	driver = self.driver
		driver.get("https://m.avito.ru/moskva/kommercheskaya_nedvizhimost?cd=1&pmax=100&searchForm=true")

	def test_guest_can_go_to_metro_page_with_input(self):
		with_input = driver.find_elements_by_css_selector("input[data-marker='metro-select/withoutValue']").click()
		sleep(3)
		self.driver.quit()

	def test_guest_can_go_to_metro_page_with_button(self): #failed
		with_button = driver.find_elements_by_css_selector("input[data-marker='metro-select/selectIcon']").click()
		sleep(3)
		self.driver.quit()
	
	def test_find_station_by_name(self):
		find_station = driver.find_elements_by_css_selector("input[data-marker='metro-select-dialog/search']").click()
		find_station.send_keys("Алексеевская")
		to_apply = driver.find_elements_by_css_selector("input[data-marker='metro-select-dialog/stations/item/toggle']").click()
		#Проверить, что на станции Алексеевская стоит галочка  label aria-checked="false"
		select_station = find_elements_by_css_selector("input[data-marker='metro-select-dialog/apply']").click()
		sleep(3)
		self.driver.quit()

	def test_floating_button_select_N_stations(self):
    	floating_button = driver.find_elements_by_name("Академическая").click()
		floating_button = driver.find_elements_by_name("Александровский парк").click()
		to_apply = driver.find_elements_by_css_selector("input[data-marker='metro-select-dialog/stations/item/toggle']").click()

		self.driver.quit()

	
