import  pytest
from selenium import webdriver
from PageObjects.LoginPage import Login_Page
from selenium.webdriver.common.by import By
from time import sleep
from utilities.ReadProperties import Readconfig
from utilities.customerlogger import LogGen
from utilities import xlutilities
from time import sleep


class Test_002DDT_Login:
    baseUrl=Readconfig.getApplicaition()
    path ='.//Testdata/testdata_2.xlsx'
    logger=LogGen.loggen()

    def test_login__DDT(self,setup):

        self.logger.info('**********login  tc *****')
        self.logger.info('**********login_DDT tc started*****')
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp=Login_Page(self.driver)
        self.rows=xlutilities.get_rowcount(self.path,'Sheet1')

        lst_result=[]

        for r in range(2,self.rows+1):
            self.user=xlutilities.read_data(self.path,'Sheet1',r,1)
            self.password=xlutilities.read_data(self.path,'Sheet1',r,2)
            self.exp=xlutilities.read_data(self.path,'Sheet1',r,3)
            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.login_click()
            sleep(2)
            actual_title=self.driver.title
            exp_title='Dashboard / nopCommerce administration'

            if actual_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info('the testcase is pass')
                    self.lp.logout_click()
                    lst_result.append('Pass')
                elif self.exp=='Fail':
                    self.logger.info('the testcase is failed')
                    self.lp.logout_click()
                    lst_result.append('Fail')
            elif actual_title !=exp_title:
                if self.exp=='Pass':
                    self.logger.info('the testcase is failed')
                    lst_result.append('Fail')
                elif self.exp=='Fail':
                    self.logger.info('the testcase is passsed')
                    lst_result.append('Pass')

        if "Fail" not in lst_result :
            self.logger.info("DDT test case passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("DDT test case failed")
            self.driver.close()
            assert False


        self.logger.info("DDT login case completed")