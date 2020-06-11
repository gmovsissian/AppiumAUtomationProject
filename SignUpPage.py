from Pages.BasePage import BaseScreen
import datetime

class SignUpPage(BaseScreen):
    edittext_class="android.widget.EditText"
    namefield_ID="app.x.android:id/primaryInputView"
    emailField_ID="app.x.android:id/emailEditText"
    phoneField_ID="app.x.android:id/mePhoneViewEditText"
    signUpButton_ID="app.x.android:id/submitInputButton"
    nextButton_ID="app.x.android:id/nextButton"

    def inputName(self,name):
        self.driver.find_element_by_id(self.namefield_ID).find_element_by_class_name(self.edittext_class).send_keys(name)

    def inputEmail(self,email,domain):
        now=str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        self.driver.find_element_by_id(self.emailField_ID).find_element_by_class_name(self.edittext_class).send_keys(email+"+"+now+domain)

    def inputPhone(self,number):
        self.driver.find_element_by_id(self.phoneField_ID).send_keys(number)

    def clickSignUPbtn(self):
        self.driver.find_element_by_id(self.signUpButton_ID).click()

    def passInstructions(self):
        if self.driver.find_element_by_id("app.x.android:id/hintImageView").is_displayed():
            for i in range(4):
                self.driver.find_element_by_id(self.nextButton_ID).click()

