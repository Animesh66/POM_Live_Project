from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Pages.BasePage import BasePage
from Utilities import configReader


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, name, ph_no, email, country, city, username, password):
        self.type("name_textbox_xpath", name)
        self.type("phone_textbox_xpath", ph_no)
        self.type("email_textbox_xpath", email)
        country_dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("", ""))
        select_country = Select(country_dropdown)
        select_country.select_by_visible_text(country)
        self.type("city_textbox_xpath", city)
        self.type("username_textbox_xpath", username)
        self.type("password_textbox_xpath", password)
