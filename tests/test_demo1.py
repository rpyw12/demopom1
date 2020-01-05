from pom.loginpage import LoginPage
import pytest
import unittest
from genrics import genricxl

@pytest.mark.usefixtures('setupclass')
class TestDemoOne(unittest.TestCase):

    filepath = "C:/Users/admin/Desktop/testdata.xlsx"

    @pytest.fixture(autouse=True)
    def classsetup(self, setupclass):
        self.lp = LoginPage(self.driver)

    def testOnevalidlogin(self):
        username = genricxl.readData(self.filepath, "Sheet1", 1, "username")
        password = genricxl.readData(self.filepath, "Sheet1", 1,"password")
        self.lp.enterUsername(username)
        self.lp.enterPassword(password)
        self.lp.clickLoginButton()
        self.lp.validateHomePage()

    def testtwoinvalidlogin(self):
        self.lp.enterUsername('admi')
        self.lp.enterPassword('manger')
        self.lp.clickLoginButton()
        self.lp.validateLoginPage()
