import  pytest
from selenium import webdriver
from PageObjects.LoginPage import Login_Page
from selenium.webdriver.common.by import By
from time import sleep
from utilities.ReadProperties import Readconfig
from utilities.customerlogger import LogGen
from PageObjects.Addcustomers import AddCustomer
from PageObjects.search_result import searchresult

class Test_004_Search:
    baseUrl = Readconfig.getApplicaition()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()

    logger = LogGen.loggen()

    def test_search_email(self,setup):
        self.logger.info("***search TC_004***")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = Login_Page(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()
        self.logger.info("******login succesful***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        sleep(5)
        self.addcust.clickOnCustomerMenuItem()
        sleep(4)

        self.searchcust= searchresult(self.driver)
        self.searchcust.setemail("abc@gmail.com")
        self.searchcust.clickOnsearch()
        sleep(4)
        status=self.searchcust.search_customer("abc@gmail.com")
        assert True==status
        self.logger.info("****finished searching****")
        self.driver.close()


    def test_search_by_name(self, setup):
        self.logger.info("***search TC_005***")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = Login_Page(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()
        self.logger.info("******login succesful***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        sleep(5)
        self.addcust.clickOnCustomerMenuItem()
        sleep(4)

        self.searchcust = searchresult(self.driver)
        self.searchcust.setfirstname("ab")
        self.searchcust.setlastname("cd")
        self.searchcust.clickOnsearch()
        sleep(4)
        status =self.searchcust.search_customerby_name("ab cd")
        assert True == status
        self.logger.info("****finished searching****")
        self.driver.close()



