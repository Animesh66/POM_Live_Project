from Utilities import configReader


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, name, ph_no, email, country, city, username, password):
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(name)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(ph_no)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(email)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(name)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(city)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(username)
        self.driver.find_element(By.XPATH, configReader.readConfig("", "")).send_keys(password)
