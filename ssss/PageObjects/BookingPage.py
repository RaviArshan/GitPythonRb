from selenium.webdriver.common.by import By


class BookingPage:
    def __init__(self, driver):
        self.driver = driver

    source = (By.XPATH, "//input[@placeholder='From']")
    destination = (By.XPATH, "//input[@placeholder='To']")
    searchButton= (By.CSS_SELECTOR, "button[data-search-element='SEARCH_BUTTON']")
    otherServices = (By.LINK_TEXT, "OTHER SERVICES")

    def getSource(self):
        return self.driver.find_element(*BookingPage.source)

    def getDestination(self):
        return self.driver.find_element(*BookingPage.destination)

    def getSearchButton(self):
        return self.driver.find_element(*BookingPage.searchButton)

    def getOtherServices(self):
        return self.driver.find_element(*BookingPage.otherServices)