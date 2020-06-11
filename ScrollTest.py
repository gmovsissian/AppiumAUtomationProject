import pytest
import time
from Pages.BasePage import BaseScreen
@pytest.mark.usefixtures("driver_setup")
class Test():
    def test_Sign_Up(self):
        baseSceen = BaseScreen(self.driver)
        baseSceen.clickProfilebtn()
        baseSceen.clicNewsbtn()
        time.sleep(3)
        baseSceen.clickFollowingbtn()
        for i in range(3):
            baseSceen.scrollaction()