from selenium import webdriver
import pytest

@pytest.yield_fixture(scope='function')
def setupclass(request, browser):
    if browser == 'chrome':
        url = 'http://localhost/login.do'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(url)
    else:
        url = 'http://localhost/login.do'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(url)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()

#**************************************************

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')



