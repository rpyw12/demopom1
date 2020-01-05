from genrics.base import Genrics
from time import sleep
from genrics.screenshot import takeScreenshot
class LoginPage(Genrics):

#-----variables with attribute value-----------------------------
    username_textfield='username'
    password_textfield='pwd'
    login_button='loginButton'

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

#--------action methods --------------------------------------
    def enterUsername(self,usn):
        self.entertext('id', self.username_textfield, usn)

    def enterPassword(self,pwd):
        #self.getElement('name',self.password_textfield).send_keys(pwd)
        self.entertext('name',self.password_textfield,pwd)

    def clickLoginButton(self):
        #self.getElement('id',self.login_button).click()
        self.clickelement('id',self.login_button)

    def validateHomePage(self):
        sleep(3)
        actual_title = self.driver.title
        expected_title = 'actiTIME - Enter Time-Track'
        if expected_title == actual_title:
            print('login is pass')
        else:
            print('test is fail')
            takeScreenshot(self.driver)
            assert expected_title == actual_title

    def validateLoginPage(self):
        sleep(3)
        actual_title = self.driver.title
        expected_title = 'actiTIME - Login'
        if expected_title == actual_title:
            print('login is pass')
        else:
            print('test is fail')
            takeScreenshot(self.driver)
            assert expected_title == actual_title


