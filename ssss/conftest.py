import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browserInvocation(request):
    driver = webdriver.Chrome(executable_path="C:\Python Softwares\ChromeDriver\chromedriver.exe")
    driver.get("http://qamain1.seatseller.travel/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()