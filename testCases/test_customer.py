import random
import string

import pytest
import time

from selenium import webdriver
from PageObjects.AddCustomerPage import AddCustomer
from Utilities.readProperties import readconfig
from Utilities.customLogger import LogGen
from PageObjects.Login import LoginHome


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))




class Test_002_Customer:
    baseURL = readconfig.getappURL()
    username = readconfig.useremail()
    password = readconfig.userpassword()
    passcode = readconfig.cpassword()
    fname = readconfig.cfirstname()
    lname = readconfig.clastname()
    dob = readconfig.cdob()

    logger = LogGen.loggen()

    # def test_addCustomer(self, setup):
    #     self.logger.info("*****Test_002_customer initiated*****")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()

    def test_login(self, setup):
        self.logger.info("******verifying login*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginHome()
        self.lp.__int__(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginButton()




        self.logger.info("*******adding customer********")
        self.addcust = AddCustomer()
        # self.addcust.__int__(self.driver)
        self.addcust.customer_menu_xpath()
        self.addcust.custmer_subMenu_xpath()
        self.addcust.btn_Addnew_xpath()

        self.email = random_generator()+"@gmail.com"
        self.addcust.txtbox_mail_xpath(self.email)

        self.addcust.txtbox_password_xpath(self.passcode)

        self.addcust.txtbox_fname_xpath(self.fname)
        self.addcust.txtbox_lname_xpath(self.lname)
        self.addcust.rdbtn_gender_xpath()
        self.addcust.dob_xpath(self.dob)
        self.addcust.btn_save_xpath()


