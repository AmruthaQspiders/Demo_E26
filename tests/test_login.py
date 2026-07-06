from pages.login_page import LoginPage
import pytest


@pytest.mark.smoke
def test_valid_login(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    lp.click_login()
    lp.enter_email("tweetyy123@gmail.com")
    lp.enter_password("TTweety@9090")
    lp.click_login_button()

@pytest.mark.regression
def test_invalid_login(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    lp.click_login()
    lp.enter_email("twee123@gmail.com")
    lp.enter_password("@9090")
    lp.click_login_button()


## READ EXCEL DATA
'''
from Demo_Tricentis_Framework.pages.login_page import LoginPage
import pytest
from Demo_Tricentis_Framework.utilities import read_excel

@pytest.mark.smoke 
@pytest.mark.parametrize("username,password", read_excel.get_data())
def test_valid_login(setup_and_teardown,username,password): ## setup tear return driver object
     lp = LoginPage(setup_and_teardown)
     lp.click_login()
     lp.enter_email(username)
     lp.enter_password(password)
     lp.click_login_button()

'''

