import time

from PageObjects.BookingPage import BookingPage
from PageObjects.BookingUserInfo import BookinguserInfo
from PageObjects.LoginObjects import LoginObjects
from PageObjects.SelectServiceSeatBPDP import ServiceSeat
from Utilities.BaseClass import BaseClass


class TestSeatseller(BaseClass):
    def test_seatseller(self):
        print("Test Develop Branch Ui")
        self.driver.implicitly_wait(120)
        loginObj = LoginObjects(self.driver)
        loginObj.getEmail().send_keys("test_fee")
        loginObj.getPassWord().send_keys("Rdebus123")
        loginObj.getButton().click()
        bookingObj = BookingPage(self.driver)
        time.sleep(20)
        bookingObj.getSource().send_keys("Bangalore")
        fromCities = self.driver.find_elements_by_xpath("//table/tbody/tr/td/strong[text()='Bangalore']")
        for fCity in fromCities:
            if fCity.text == "Bangalore":
                fCity.click()
                break;
        bookingObj.getDestination().send_keys("Chennai")
        toCities = self.driver.find_elements_by_xpath("//table/tbody/tr/td/strong[text()='Chennai']")
        for tCity in toCities:
            if tCity.text == "Chennai":
                tCity.click()
                break;
        bookingObj.getSearchButton().click()
        bookingObj.getOtherServices().click()
        serviceSeatBPDP = ServiceSeat(self.driver)
        serviceSeatBPDP.selectService().click()
        serviceSeatBPDP.selectSeat().click()
        serviceSeatBPDP.selectBP().click()
        boardingPoint = self.driver.find_elements_by_css_selector("td[role='menuitem']")
        for bp in boardingPoint:
            if bp.text == "Domlur - 06:00 PM":
                bp.click()
                break;
        serviceSeatBPDP.selectDP().click()
        droppingPoint = self.driver.find_elements_by_css_selector("td[role='menuitem']")
        for dp in droppingPoint:
            if dp.text == "100 feet road - 05:00 AM":
                dp.click()
                break;
        bookingUInfo = BookinguserInfo(self.driver)
        bookingUInfo.getPassengerName().send_keys("Ravi Test Booking")
        gender = self.driver.find_elements_by_css_selector("input[type='radio']")
        gender[1].click()
        bookingUInfo.getPassengerAge().send_keys("28")
        bookingUInfo.getPassengerMobileNo().send_keys("8553440468")
        bookingUInfo.getPassengerEmail().send_keys("ravi.m@redbus.com")
        bookingUInfo.getBookingButton().click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//button[@type='button']/div[text()='Debit Card »']").click()

