import time
from .base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):
    
    def switch_tabs_save_checkboxes(self):
            lst = self.some_random_stations_should_be_chosen_from_alphabet_list() 
            self.scrollg_up()
            if self.is_element_present(By.CSS_SELECTOR, '[data-marker="metro-select-dialog/chips/more"]):
                self.browser.find_element(By.CSS_SELECTOR, '[data-marker="metro-select-dialog/chips/more"]).click()
            lstN = self.browser.find_elements(By.CLASS_NAME, "css-1j6zceg")
            for a in range(len(lstN)):
                self.browser.execute_script("arguments[0];", lst[a])
                assert lstN[a].text == lst[i]
            self.switch_tab(By.CSS_SELECTOR, '[class ="css-17syd5g"][tabindex="-1"]')
            self.scrollg_up()
            lstM = self.browser.find_elements(By.CSS_SELECTOR, '[class ="css-17syd5g"][tabindex="-1"]')
            for a in range(len(lstM)):
                self.browser.execute_script("arguments[0];", lst[a])
                assert lstN[a].text == lstM[a].text
    
    def floating_button_after_choose_station(self):
            self.random_station_should_be_chose_from_list()
            assert self.is_active(By.CSS_SELECTOR, '[data-marker="metro-select-dialog/apply"]')
    
    def select_repeat_line_tab_be_not_extend(self):
        choice = self.random_station_should_be_chose_from_list()
        self.scrollg_up()
        self.switch_tab(By.CLASS_NAME, "css-1j6zceg")
        choice2 = self.browser.find_element(By.CSS_SELECTOR, '[class="css-1suadfl"][aria-checked="true"] [class="_2Jon7"]').get_attribute('textContent')
        assert len(self.browser.find_elements(By.CLASS_NAME, "css-1j6zceg")) == 0 and choice == choice2
    
    def reset_button_should_be_active(self):
            self.is_element_active(By.CLASS_NAME, 'css-yz1jyo')
    def reset_button_should_be_not_active(self):
            self.is_element_not_active(By.CLASS_NAME, 'css-yz1jyo')
    def random_station_should_be_chose_from_list(self):
            return self.choose_one_random_element_from_checkboxes(By.CLASS_NAME, "css-1suadfl")
    
    def stations_list_be_closed_while_searching_in_search_box(self):
            self.browser.find_element(By.CSS_SELECTOR, '[data-marker="metro-select-dialog/search"]').send_keys(' ')
            assert self.is_not_active(By.CSS_SELECTOR, '[data-marker="metro-select-dialog/tabs"]')
    
    def correct_words_be_on_choice_button(self):
            lst = self.some_random_stations_should_be_chosen_from_alphabet_list()
            button = self.browser.find_element(By.CSS_SELECTOR, '[data-marker="metro-select-dialog/apply"]').text
            if len(lst) % 10 in (0, 5, 6, 7, 8, 9) or len(lst) in (11, 12, 13, 14):
                assert button == (f"Выбрать {len(lst)} станций")
            elif len(lst) % 10 in (2, 3, 4):
                assert button == (f"Выбрать {len(lst)} станции")
            elif len(lst) % 10 == 1:
                assert button == (f"Выбрать 1 станцию")