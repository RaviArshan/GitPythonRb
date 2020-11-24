from selenium.webdriver.common.by import By


class BookinguserInfo:
    def __init__(self,driver):
        self.driver = driver

    pName =(By.CSS_SELECTOR , "input[data-pax-details='NAME']")
    pAge  =(By.CSS_SELECTOR , "input[data-pax-details='AGE']")
    pMobileNo = (By.CSS_SELECTOR , "input[placeholder='Phone Number']")
    pEmail = (By.CSS_SELECTOR , "input[placeholder='Email']")
    pButton = (By.XPATH , "//div[@class='GD55KTWLDJ']/button[1]")

    def getPassengerName(self):
        return self.driver.find_element(*BookinguserInfo.pName)

    def getPassengerAge(self):
        return self.driver.find_element(*BookinguserInfo.pAge)

    def getPassengerMobileNo(self):
        return self.driver.find_element(*BookinguserInfo.pMobileNo)

    def getPassengerEmail(self):
        return self.driver.find_element(*BookinguserInfo.pEmail)

    def getBookingButton(self):
        return self.driver.find_element(*BookinguserInfo.pButton)