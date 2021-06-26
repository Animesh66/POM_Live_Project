from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities import configReader


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, name, ph_no, email, country, city, username, password):
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(name)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(ph_no)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(email)
        country_dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("", ""))
        select_country = Select(country_dropdown)
        select_country.select_by_visible_text(country)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(city)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(username)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(password)
