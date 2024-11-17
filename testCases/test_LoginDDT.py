import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from Utilities.readProperties import readconfig
from PageObjects.Login import LoginHome 
from Utilities.customLogger import LogGen
from Utilities import XLutils
import os

class Test_001_Login:
    driver: WebDriver
    baseURL = readconfig.getappURL()
    path = ".//TestData/login_Data.xlsx"



    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("******verifying login*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginHome()
        self.lp.__int__(self.driver)

        self.rows = XLutils.getRowcount(self.path,'Sheet1')
        for r in range(2,self.rows+1):
            self.user =XLutils.readData(self.path,'Sheet1',r,1)
            self.password= XLutils.readData(self.path,'Sheet1',r,2)
            self.exp = XLutils.readData(self.path,'Sheet1',r,3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.loginButton()
            time.sleep(5)



        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        act_title = self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******login passed*******")
            self.driver.close()
        else:
            self.logger.error("********login failed*******")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False



