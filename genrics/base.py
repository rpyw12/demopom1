from selenium.webdriver.common.by import By
import logging

class Genrics():

    logging.basicConfig(filename='testlog', level=logging.INFO)

    def __init__(self,driver):
        self.driver=driver


    def getByType(self,locator_type):

        locator_type=locator_type.lower()

        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'classname':
            return By.CLASS_NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'cssselector':
            return By.CSS_SELECTOR
        elif locator_type == 'linktext':
            return By.LINK_TEXT
        elif locator_type == 'partiallinktext':
            return By.PARTIAL_LINK_TEXT
        else:
            logging.info(('the locator type ',locator_type,' is not found'))


    def getElement(self,locator_type,locator_value):
        try:
            bytype=self.getByType(locator_type)
            element=self.driver.find_element(bytype,locator_value)
            logging.info((" the element with the locator type ",locator_type," and locator value ",
                  locator_value,' is found'))
        except:
            print(" the element with the locator type ", locator_type," and locator value ",
                  locator_value,' is not found')
        return element

    def entertext(self,locator_type,locator_valu,data):
        try:
            element=self.getElement(locator_type,locator_valu)
            element.send_keys(data)
            logging.info(('data ',data,' is sent to the component with locator type ',
                  locator_type,' and locator value ',locator_valu))
        except:
            print('data ', data, ' is not sent to the component with locator type ',
                  locator_type, ' and locator value ',locator_valu)

    def clickelement(self, locator_type, locator_valu):
        try:
            element = self.getElement(locator_type, locator_valu)
            element.click()
            logging.info(('clicked on the component with locator type ',
                  locator_type, ' and locator value ', locator_valu))
        except:
            print('not clicked on the component with locator type ',
                  locator_type, ' and locator value ', locator_valu)
























