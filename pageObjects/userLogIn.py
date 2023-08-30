from selenium.webdriver.common.by import By


class User_LogIn:
    Click_LinkLogIn_LINKTEXT = (By.LINK_TEXT, "Login")
    Text_Email_ID = (By.ID, "email")
    Text_Password_ID = (By.ID, "password")
    Click_LogInButton_XPATH = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def Click_LinkLogIn(self):
        self.driver.find_element(*User_LogIn.Click_LinkLogIn_LINKTEXT).click()

    def Enter_Email(self, email):
        self.driver.find_element(*User_LogIn.Text_Email_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*User_LogIn.Text_Password_ID).send_keys(password)

    def Click_LogInButton(self):
        self.driver.find_element(*User_LogIn.Click_LogInButton_XPATH).click()
