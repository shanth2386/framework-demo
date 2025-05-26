import  pytest
from selenium import webdriver
from PageObjects.LoginPage import Login_Page
from selenium.webdriver.common.by import By
from time import sleep
from utilities.ReadProperties import Readconfig
from utilities.customerlogger import LogGen




class TestLogin:
    baseUrl=Readconfig.getApplicaition()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepagetitle(self,setup):

        self.logger.info('**********homepagetitle tc *****')
        self.logger.info('**********homepagetitle tc started*****')
        self.driver=setup
        self.driver.get(self.baseUrl)
        actual_title=self.driver.title

        if actual_title=='nopCommerce demo store. Login':
            assert True
            self.driver.close()
            self.logger.info('**********homepagetitle tc passed*****')
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"homepage_title.png")
            assert False
            self.driver.close()
            self.logger.info('**********homepagetitle tc Failed*****')

    def test_login(self,setup):

        self.logger.info('**********login  tc *****')
        self.logger.info('**********login tc started*****')
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp=Login_Page(self.driver) # creating the object for page object class
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()
        actual_title=self.driver.title

        if actual_title=='Dashboard / nopCommerce administration':
                assert True
                self.driver.close()
                self.logger.info('**********Loginpage tc Passed*****')
        else:
                 self.driver.save_screenshot(".\\Screenshots\\" + 'loginsuccess.png')
                 assert False
                 self.driver.close()
                 self.logger.info('**********Loginpage tc Failed*****')

