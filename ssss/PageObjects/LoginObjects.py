from selenium.webdriver.common.by import By


class LoginObjects:
    def __init__(self , driver):
        self.driver = driver

    emailBox = (By.NAME, "emailbox")
    passWord = (By.NAME, "password")
    button = (By.XPATH, "//div[@class='lower']/button")

    def getEmail(self):
        return self.driver.find_element(*LoginObjects.emailBox)

    def getPassWord(self):
        return self.driver.find_element(*LoginObjects.passWord)

    def getButton(self):
        return self.driver.find_element(*LoginObjects.button)