from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import configReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):  # this method will click on the locator given
        if str(locator).endswith("_xpath"):  # if the locator variable name is ends with _xpath it will click on the
            # xpath
            self.driver.find_element(By.XPATH(configReader.readConfig("locator", locator)).click())
        elif str(locator).endswith("_css"):
            self.driver.find_element(By.CSS_SELECTOR(configReader.readConfig(("locator", locator)).click()))
        elif str(locator).endswith("_id"):
            self.driver.find_element(By.ID(configReader.readConfig(("locator", locator)).click()))

    def type(self, locator, value):  # this method is the replacement method of send_keys
        if str(locator).endswith("_xpath"):
            self.driver.find_element(By.XPATH(configReader.readConfig("locator", locator)).send_keys(value))
        elif str(locator).endswith("_css"):
            self.driver.find_element(By.CSS_SELECTOR(configReader.readConfig(("locator", locator)).send_keys(value)))
        elif str(locator).endswith("_id"):
            self.driver.find_element(By.ID(configReader.readConfig(("locator", locator)).send_keys(value)))

    def select_dropdown(self, locator, value):  # this method is for dropdown value selection method
        global dropdown
        if str(locator).endswith("_xpath"):
            dropdown = self.driver.find_element(By.XPATH(configReader.readConfig("locator", locator)).send_keys(value))
        elif str(locator).endswith("_css"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR(configReader.readConfig(("locator", locator)).send_keys(value)))
        elif str(locator).endswith("_id"):
            dropdown = self.driver.find_element(By.ID(configReader.readConfig(("locator", locator)).send_keys(value)))
        select = Select(dropdown)
        select.select_by_visible_text(value)

