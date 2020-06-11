from appium import webdriver
import pytest


@pytest.fixture()
def driver_setup(request):
	capabilities = {
        "platformName": "android",
        "platformVersion": "8.0",
        "deviceName": "Galaxy A5 (2017)",
        "app": "C:/Users/Gurgen/Desktop/x-1.0.0app-debug (1).apk",
        "udid": "520094a7ecb4749b",
        "noReset": "true",
        "appActivity": "aam.x.me.presentation.ui.home.DeepLinkActivity",
        "appPackage": "app.x.android"}

	request.instance.driver = webdriver.Remote(
        "http://localhost:4723/wd/hub", capabilities
	)
	yield
	# request.instance.driver.quit()