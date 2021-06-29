from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Pages.BasePage import BasePage
from Utilities import configReader


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, name, ph_no, email, country, city, username, password):
        type("name_textbox_xpath", name)
        type("phone_textbox_xpath", ph_no)
        type("email_textbox_xpath", email)
        country_dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("", ""))
        select_country = Select(country_dropdown)
        select_country.select_by_visible_text(country)
        type("city_textbox_xpath", city)
        type("username_textbox_xpath", username)
        type("password_textbox_xpath", password)
