from Pages.BasePage import BaseScreen

class ProfilePage(BaseScreen):
    user_Name_ID="app.x.android:id/fullNameView"

    def getUser_Name(self):
        return self.driver.find_element_by_id(self.user_Name_ID).get_attribute("text")
