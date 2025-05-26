from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class AddCustomer:

    lnkCustomer_menu_xpath='//nav[@class="mt-2"]/ul/li[4]/a/p'
    lnkCustomer_sub_menu_xpath='//nav[@class="mt-2"]/ul/li[4]/ul/li/a//p'
    btn_addCustomer_xpath='//a[@class="btn btn-primary"]'
    txt_email_id_xpath='//input[@id="Email"]'
    txt_password_xpath='//input[@id="Password"]'
    txt_firstname_xpath='//input[@id="FirstName"]'
    txt_lstname_xpath='//input[@id="LastName"]'
    rd_malegender_xpath='//input[@id="Gender_Male"]'
    rd_femalegender_xpath='//input[@id="Gender_Female"]'
    txt_company_xpath='//input[@id="Company"]'
    txt_customer_role_xpath='//li[@class="select2-selection__choice"]//parent::ul'
    lstitem_Adminstrator_xpath='//span[@class="select2-results"]//li[contains(text(),"Administrators")]'
    lstitem_ForumModerators_xpath='//span[@class="select2-results"]//li[contains(text(),"Forum Moderators")]'
    lstitem_Registered_xpath='// span[@class ="select2-results"] // li[contains(text(), "Registered")]'
    lstitem_Guests_xpath='// span[@ class ="select2-results"] // li[contains(text(), "Guests")]'
    txtarea_Admincomment_xpath='//textarea[@id ="AdminComment"]'
    btn_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
       self.driver.find_element(By.XPATH,self.lnkCustomer_sub_menu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btn_addCustomer_xpath).click()

    def setEmail(self,email):
       self.driver.find_element(By.XPATH,self.txt_email_id_xpath).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(password)

    def setcustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txt_customer_role_xpath).click()
        sleep(3)
        if role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitem_Adminstrator_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitem_Registered_xpath)
        elif role=='Guest':
            sleep(3)
            self.driver.find_element(By.XPATH,"//span[@class='select2-selection__choice__remove']").click()
            self.listitem=self.driver.find_element(By.XPATH,self.lstitem_Guests_xpath)
        else:
            self.driver.find_element(By.XPATH,self.lstitem_Guests_xpath)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setGender(self,gender):
            if gender =='Male':
                self.driver.find_element(By.XPATH,self.rd_malegender_xpath).click()
            elif gender=='Femail':
                self.driver.find_element(By.XPATH,self.rd_femalegender_xpath).click()
            else:
                self.driver.find_element(By.XPATH, self.rd_malegender_xpath).click()

    def Firstname(self,fname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(fname)

    def Lastname(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lstname_xpath).send_keys(lname)

    def company(self,company):
        self.driver.find_element(By.XPATH,self. txt_company_xpath).send_keys(company)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtarea_Admincomment_xpath).send_keys(content)

    def saveOnClick(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()


