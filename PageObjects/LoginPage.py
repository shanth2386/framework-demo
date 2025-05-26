from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_Page:

     textbox_username_id='Email'
     textbox_password_id='Password'
     button_login_xpath="//button[@class='button-1 login-button']"
     logout_link_xpath='//*[@id="navbarText"]/ul/li[3]/a'

     def __init__(self,driver):
        self.driver=driver

     def set_username(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

     def set_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

     def login_click(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

     def logout_click(self):
         WebDriverWait(self.driver, 20).until(
             EC.visibility_of_element_located((By.XPATH, self.logout_link_xpath))
         ).click()



