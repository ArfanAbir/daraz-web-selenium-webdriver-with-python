from Pages.RegistrationPage import SignUpPage
from Tests.BasePage import BasePage


class SignUpWithEmail(BasePage):
    def test_Sign_Up(self):
        signup = SignUpPage(self.driver)
        signup.click_on_signup_btn()
        signup.register_btn()
        signup.signup_email()
        signup.phone_number("nazrul.qups@gmail.com")
        signup.drag_and_drop()
        signup.password_input("abc123")
        signup.birth_month_box()
        signup.birth_month()
        signup.birth_day_box()
        signup.birth_day()
        signup.birth_year_box()
        signup.birth_year()
        signup.gender_box()
        signup.gender()
        signup.full_name("Arfan Abir")
        signup.check_box()
        signup.submit_btn()

