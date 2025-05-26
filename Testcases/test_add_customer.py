import string
import random

import  pytest
from selenium import webdriver
from PageObjects.LoginPage import Login_Page
from selenium.webdriver.common.by import By
from time import sleep
from utilities.ReadProperties import Readconfig
from utilities.customerlogger import LogGen
from PageObjects.Addcustomers import AddCustomer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Test_003_Addcustomer:

    baseUrl=Readconfig.getApplicaition()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_Addcustomer(self,setup):

        self.logger.info("*******TC003_Addcustomer**********")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = Login_Page(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()
        self.logger.info("******login succesful***")

        self.logger.info("*****starting adding customer****")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        sleep(5)
        self.addcust.clickOnCustomerMenuItem()
        sleep(5)
        self.addcust.clickOnAddNew()
        self.logger.info("******providing customer details***********")

        self.email=random_generator()+'@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.Firstname('divya')
        self.addcust.Lastname('Rao')
        self.addcust.company('UARER')
        self.addcust.setcustomerRoles('Administrators')
        self.addcust.setAdminContent('Admin content entered in the textbox')
        self.addcust.setGender('Male')
        self.addcust.saveOnClick()

        self.logger.info("*************Saving the customer details****")
        self.logger.info("****adding customer validation***")
        self.msg=self.driver.find_element(By.TAG_NAME,'body').text
        if "The new customer has been added successfully." in self.msg:
            assert True==True
            self.logger.info("****Add customer TC passed***")
        else:
            self.logger.info("****Add customer TC failed****")
            assert True == False

        self.driver.close()




