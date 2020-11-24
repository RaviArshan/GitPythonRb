from selenium.webdriver.common.by import By


class ServiceSeat:
    def __init__(self,driver):
        self.driver = driver

    service = (By.XPATH, "//table[@class='search']/tbody/tr/td[9]/div/div/button[@id='2000002134210065605']")
    seat = (By.XPATH, "//div[@class='GD55KTWM0H']/table/tbody/tr/td/div[text()='3']")
    bp = (By.CSS_SELECTOR, "input[placeholder='Select Boarding Point']")
    dp = (By.CSS_SELECTOR, "input[placeholder='Select Dropping Point']")

    def selectService(self):
        return self.driver.find_element(*ServiceSeat.service)

    def selectSeat(self):
        return self.driver.find_element(*ServiceSeat.seat)

    def selectBP(self):
        return self.driver.find_element(*ServiceSeat.bp)

    def selectDP(self):
        return self.driver.find_element(*ServiceSeat.dp)