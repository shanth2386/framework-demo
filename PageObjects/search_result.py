from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class searchresult:

    txt_email_xpath="//input[@id='SearchEmail']"
    txt_firstname_xpath="//input[@id='SearchFirstName']"
    txt_lastname_xpath="//input[@id='SearchLastName']"
    btn_search_xpath="//button[@id='search-customers']"

    table_search_grid_xpath="//table[@id='customers-grid']"
    table_rows_xpath="//table[@id='customers-grid']//tbody/tr"
    table_cols_xpath="//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self,driver):
        self.driver=driver

    def setemail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setfirstname(self,fname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(fname)

    def setlastname(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lname)

    def clickOnsearch(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()

    def getnorows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_rows_xpath))

    def getnoofcols(self):
        return len(self.driver.find_elements(By.XPATH,self.table_cols_xpath))

    def search_customer(self,email):
        flag=False
        for r in range(1,self.getnorows()+1):
            table=self.driver.find_element(By.XPATH,self.table_search_grid_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid.strip()==email:
                flag=True
                break
        return flag



    def search_customerby_name(self,Name):
        flag=False
        for r in range(1,self.getnorows()+1):
            table=self.driver.find_element(By.XPATH,self.table_search_grid_xpath)
            name=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text.strip()
            if name ==Name:
                flag=True
                break
        return flag