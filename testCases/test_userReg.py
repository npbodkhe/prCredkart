from pageObjects.userRegPage import UserReg_Page


class Test_UserReg:
    def test_userreg_01(self, setup):
        self.driver = setup
        self.rp = UserReg_Page(self.driver)
        self.rp.Click_LinkRegister()
        self.driver.save_screenshot("C:\\Users\\npbod\\Videos\\Captures\\revision\\prCredkart\\Screenshot"
                                    "\\RegisterPage.png")
        self.rp.Enter_UserName("TestUser11")
        self.rp.Enter_Email("test@hotmail.com")
        self.rp.Enter_Password("test@321")
        self.rp.Enter_ConfirmPassword("test@321")
        self.rp.Click_Register()
        self.driver.save_screenshot("C:\\Users\\npbod\\Videos\\Captures\\revision\\prCredkart\\Screenshot"
                                    "\\RegisterSuccessful.png")
        if self.rp.Status() == True:
            self.driver.save_screenshot("C:\\Users\\npbod\\Videos\\Captures\\revision\\prCredkart\\Screenshot"
                                        "\\RegisterSuccessful.png")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\npbod\\Videos\\Captures\\revision\\prCredkart\\Screenshot"
                                        "\\RegisterFailed.png")
            assert False
        self.driver.close()
