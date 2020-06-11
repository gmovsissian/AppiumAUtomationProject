import pytest
from Pages.MainPage import MainPage
from Pages.ProfilePage import ProfilePage
from Pages.SignUpPage import SignUpPage
from Pages.SignInPage import SignInPage
from Pages.BasePage import BaseScreen
import time

@pytest.mark.usefixtures("driver_setup")
class Test():

	def test_signUp(self):
		mainPage = MainPage(self.driver)
		mainPage.clickSignUP()
		mainPage.signUpByEmail()
		signUpPage = SignUpPage(self.driver)
		signUpPage.inputName("Gurgen")
		signUpPage.inputEmail("gurgen.movsisyan", "@x.me")
		signUpPage.clickSignUPbtn()
		signUpPage.passInstructions()
		baseSceen = BaseScreen(self.driver)
		assert baseSceen.checkNavBarIsVisible()

	def test_signIn(self):
		mainPage = MainPage(self.driver)
		mainPage.clickSignIn()
		mainPage.signInByEmail()
		signInPage = SignInPage(self.driver)
		signInPage.inputEmail("gurgen.movsisyan+1@x.me")
		signInPage.clickNextBtn()
		baseSceen = BaseScreen(self.driver)
		assert baseSceen.checkNavBarIsVisible()
		baseSceen.clickProfilebtn()
		profilePage=ProfilePage(self.driver)
		assert profilePage.getUser_Name()=="Gurgen 1"


	def test_scroll(self):
		baseSceen = BaseScreen(self.driver)
		baseSceen.clickProfilebtn()
		baseSceen.clicNewsbtn()
		time.sleep(3)
		baseSceen.clickFollowingbtn()
		for i in range (3):
			baseSceen.scrollaction()