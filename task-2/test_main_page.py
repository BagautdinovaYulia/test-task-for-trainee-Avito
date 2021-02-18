import pytest
import time
from pages.base_page import BasePage
from pages.main_page import MainPage

url = "https://m.avito.ru/moskva/nedvizhimost?searchForm=true"

class testMainPage:

    def test_switching_between_tabs_AlphabetLine_dosent_reset_the_selection(self, browser):
        page = MainPage(browser, url)
        page.open_page()
        page.switch_tabs_save_checkboxes()

    def test_when_select_station_from_the_button_floating_SelectNStations(self, browser):
        page = MainPage(browser, url)
        page.open_page()
        page.should_be_repeat_when_selected_tabs_should_not_expand()

    def test_when_choosing_any_station_from_the_alphabetical_list_the_selection_is_duplicated_inside_the_line_while_the_line_does_not_unfold;(self, browser):
        page = MainPage(browser, url)
        page.open_page()
        page.select_repeat_line_tab_be_not_extend()

    def test_the_Reset_button_appears_only_for_selected_stations(self,  browser):
        page = MainPage(browser, url)
        page.open_page()
        page.reset_button_should_be_not_active()
        page.random_station_should_be_chose_from_list()
        page.scroll_up_page()
        page.reset_button_should_be_active)

    def test_when_choosing_a_metro_station_through_the_search_bar_the_search_is_closed(self, browser):
        page = MainPage(browser, url)
        page.open_page()
        page.stations_list_be_closed_while_searching_in_search_box()

    def test_on_the_Refine_screen_the_applied_filter_by_metro_is_displayed_with_the_wording_Nstations _selected”. (self, browser):
        page = MainPage(browser, url)
        page.open_page()
        page.correct_words_be_on_choice_button()