import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def open_page(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browse = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def switch_tab(self, how, what):
        element = self.browser.find_element(how, what)
        self.browser.execute_script("arguments[0].click();", element)

    def is_active(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_active(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_active(self, how, what):
        assert self.browser.find_element(how, what).is_enabled()
    
    def is_element_not_active(self, how, what):
        assert self.browser.find_element(how, what).is_enabled() is False

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def choose_one_random_element_from_checkboxes(self, how, what):
        all_checkbox_list = self.browser.find_elements(how, what)
        number = random.randint(0, len(all_checkbox_list) - 1)
        self.browser.execute_script("arguments[0].click();", all_checkbox_list[number])
        chosen_station_name = all_checkbox_list[number].text
        return chosen_station_name

    def choose_random_elements_from_checkboxes(self, how, what):
        all_checkbox_list = self.browser.find_elements(how, what)
        number = random.randint(1, len(all_checkbox_list))
        lst2 = [random.randint(0, len(all_checkbox_list) - 1) for i in range(number)]
        lst = list(set(lst2))
        lst.sort()
        chosen_checkbox_list = []
        for i in range(len(lst)):
            self.browser.execute_script("arguments[0].click();", all_checkbox_list[lst[i]])
            chosen_checkbox_list.append(all_checkbox_list[lst[i]].text)
        return chosen_checkbox_list