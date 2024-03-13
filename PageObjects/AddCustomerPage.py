from selenium.webdriver.common.by import By


class AddCustomer:
    customer_menu_xpath=(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]")
    custmer_subMenu_xpath=(By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    btn_Addnew_xpath=(By.XPATH,"//a[@class='btn btn-primary']")
    txtbox_mail_xpath=(By.XPATH,"//input[@id='Email']")
    txtbox_password_xpath=(By.XPATH,"//input[@id='Password']")
    txtbox_fname_xpath=(By.XPATH,"//input[@id='FirstName']")
    txtbox_lname_xpath=(By.XPATH,"//input[@id='LastName']")
    rdbtn_gender_xpath=(By.XPATH,"//input[@id='Gender_Male']")
    dob_xpath=(By.XPATH,"//input[@id='DateOfBirth']")
    txt_company_xpath=(By.XPATH,"//input[@id='Company']")
    chckbox_xpath=(By.XPATH,"//input[@id='IsTaxExempt']")
    btn_save_xpath=(By.XPATH,"//button[@name='save']")

    def __int__(self,driver):
        self.driver=driver

    def clickoncustomer(self):
        self.driver.find_element(self.customer_menu_xpath).click()

    def clicksubcustomer(self):
        self.driver.find_element(self.custmer_subMenu_xpath).click()

    def clickAdd(self):
        self.driver.find_element(self.btn_Addnew_xpath).click()

    def enterEmail(self,email):
        self.driver.find_element(self.txtbox_mail_xpath).send_keys(email)

    def enterFname(self,firstname):
        self.driver.find_element(self.txtbox_fname_xpath).send_keys(firstname)

    def enterLname(self,lastname):
        self.driver.find_element(self.txtbox_lname_xpath).send_keys(lastname)

    def gender(self,male):
        self.driver.find_element(self.rdbtn_gender_xpath).send_keys(male)

    def DOB(self,dob):
        self.driver.find_element(self.dob_xpath).send_keys(dob)

    def clickSave(self,save):
        self.driver.find_element(self.btn_save_xpath).click()
