from selenium.webdriver.common.by import By
from Utilities import configReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):  # this function will click on the locator
        if str(locator).endswith("_xpath"):
            self.driver.find_element(By.XPATH(configReader.readConfig("locator", locator)).click())
        elif str(locator).endswith("_css"):
            self.driver.find_element(By.CSS_SELECTOR(configReader.readConfig(("locator", locator)).click()))
        elif str(locator).endswith("_id"):
            self.driver.find_element(By.ID(configReader.readConfig(("locator", locator)).click()))

    def type(self, locator, value):
        self.driver.find_element(By.XPATh(configReader.readConfig("locator", locator)).send_keys(value))


