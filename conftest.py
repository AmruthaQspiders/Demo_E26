import pytest

from selenium import webdriver

@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome()   ## setup
    driver.maximize_window()
    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()    


## Cross browser Testing
'''
import pytest

from selenium import webdriver

@pytest.fixture(params=['chrome','edge','firefox'])
def setup_and_teardown(request):
    parameter = request.param   ## store the current parameter

    if parameter == 'chrome':
        driver = webdriver.Chrome()
    elif parameter == 'edge':
        driver = webdriver.Edge()
    elif parameter == 'firefox':
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()'''

# # request is a built-in pytest object
# # Whenever a fixture is parameterized , the current parameter is stored
#  inside request.parm
#
# # First execution --> request.parm = 'chrome'
# # Second execution --> request.parm = 'edge'....
