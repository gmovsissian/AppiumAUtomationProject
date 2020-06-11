from Pages.BasePage import BaseScreen

class MainPage(BaseScreen):

    signUpbtn_ID = "app.x.android:id/btn_register"
    signInbtn_ID="app.x.android:id/btn_login"
    signEmailbtn_ID="app.x.android:id/selectEmailView"
    signPhonebtn_ID="app.x.android:id/selectPhoneView"

    def clickSignUP(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id(self.signUpbtn_ID).click()

    def clickSignIn(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id(self.signInbtn_ID).click()

    def signUpByEmail(self):
        self.driver.find_element_by_id(self.signEmailbtn_ID).click()

    def signUpByPhone(self):
        self.driver.find_element_by_id(self.signPhonebtn_ID).click()

    def signInByEmail(self):
        self.driver.find_element_by_id(self.signEmailbtn_ID).click()

    def singInPhone(self):
        self.driver.find_element_by_id(self.signPhonebtn_ID).click()
        self.driver.find_elements_by_class_name()

