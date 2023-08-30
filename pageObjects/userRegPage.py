from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class UserReg_Page:
    Click_LinkRegister_LinkText = (By.LINK_TEXT, "Register")
    Text_UserName_ID = (By.ID, "name")
    Text_Email_NAME = (By.NAME, "email")
    Text_Password_ID = (By.ID, "password")
    Text_ConfirmPassword_ID = (By.ID, "password-confirm")
    Click_Register_ClassName = (By.CLASS_NAME, "btn")
    Status_Text_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def Click_LinkRegister(self):
        self.driver.find_element(*UserReg_Page.Click_LinkRegister_LinkText).click()

    def Enter_UserName(self, username):
        self.driver.find_element(*UserReg_Page.Text_UserName_ID).send_keys(username)

    def Enter_Email(self, email):
        self.driver.find_element(*UserReg_Page.Text_Email_NAME).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*UserReg_Page.Text_Password_ID).send_keys(password)

    def Enter_ConfirmPassword(self, confirmpassword):
        self.driver.find_element(*UserReg_Page.Text_ConfirmPassword_ID).send_keys(confirmpassword)

    def Click_Register(self):
        self.driver.find_element(*UserReg_Page.Click_Register_ClassName).click()

    def Status(self):
        try:
            self.driver.find_element(*UserReg_Page.Status_Text_XPATH)
            return True
        except NoSuchElementException:
            return False
