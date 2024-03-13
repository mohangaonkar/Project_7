from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginHome:
    textbox_username_id = (By.ID, "Email")
    textbox_password_id = (By.ID, "Password")
    button_login_xpath = (By.XPATH,"//button[@type='submit']")
    logout_linktext = (By.LINK_TEXT,"Logout")

    def __int__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(*LoginHome.textbox_username_id).clear()
        self.driver.find_element(*LoginHome.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(*LoginHome.textbox_password_id).clear()
        self.driver.find_element(*LoginHome.textbox_password_id).send_keys(password)

    def loginButton(self):
        self.driver.find_element(*LoginHome.button_login_xpath).click()

    # def logout(self):
    #     self.driver.find_element(*LoginHome.logout_linktext).click()