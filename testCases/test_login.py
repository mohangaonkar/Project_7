import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from Utilities.readProperties import readconfig
from PageObjects.Login import LoginHome
from Utilities.customLogger import LogGen
import os

class Test_001_Login:
    driver: WebDriver
    baseURL = readconfig.getappURL()
    username = readconfig.useremail()
    password = readconfig.userpassword()


    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("**************Test_001_Login**********")
        self.logger.info("*************Verifying homepage title****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title== "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********home page title test passed******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"homepagetitle.png")
            self.driver.close()
            self.logger.error("*******homepage title failed*********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("******verifying login*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginHome()
        self.lp.__int__(self.driver)
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



