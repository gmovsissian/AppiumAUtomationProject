from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction


class BaseScreen:
    def __init__(self, driver: Remote):
        self.driver = driver

    profile_bottom_bar_ID="app.x.android:id/bottom_bar_item_profile"
    news_bottom_bar_ID="app.x.android:id/bottom_bar_item_news"
    profile_bottom_bar_Class="android.widget.ImageView"
    profile_following_btn_ID="app.x.android:id/textSubscriptions"

    def clickProfilebtn(self):
        self.driver.find_element_by_id(self.profile_bottom_bar_ID).click()
    def clicNewsbtn(self):
        self.driver.find_element_by_id(self.news_bottom_bar_ID).click()
    def clickFollowingbtn(self):
        self.driver.find_element_by_id(self.profile_following_btn_ID).click()

    def checkNavBarIsVisible(self):
        return self.driver.find_element_by_id('app.x.android:id/bottom_navigation_bar_v2').is_displayed()


