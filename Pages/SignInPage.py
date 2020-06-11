from Pages.BasePage import BaseScreen

class SignInPage(BaseScreen):
    emailfield_ID="app.x.android:id/primaryInputView"
    editText_class="android.widget.EditText"
    nextButton_ID="app.x.android:id/submitInputButton"

    def inputEmail(self,email):
        self.driver.find_element_by_id(self.emailfield_ID).find_element_by_class_name(self.editText_class).send_keys(email)
    def clickNextBtn(self):
        self.driver.find_element_by_id(self.nextButton_ID).click()