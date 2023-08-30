from pageObjects.userLogIn import User_LogIn
from utilities.logger import LogGenerator


class Test_LogIn:
    log = LogGenerator.loggen()

    def test_logIn_01(self, setup):
        self.log.info("TC test_logIn_01 is started")
        self.driver = setup
        self.log.info("Invoking Browser")
        self.log.info("Opening Browser")
        self.lp = User_LogIn(self.driver)
        self.log.info("Clicking on Link LogIn Link")
        self.lp.Click_LinkLogIn()
        self.log.info("Entering Email")
        self.lp.Enter_Email("TestUser1")
        self.log.info("Entering Password")
        self.lp.Enter_Password("test@321")
        self.log.info("Clicking on LogIn Button")
        self.lp.Click_LogInButton()
        self.driver.close()
