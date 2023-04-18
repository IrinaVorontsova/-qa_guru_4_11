import allure

from models.registration_model import FormRegistration, Hobbies
from pages.registration_page import RegistrationPage


class TestPage:

    @staticmethod
    def set_url():
        with allure.step("Set test UTL"):
            return 'https://demoqa.com/automation-practice-form'

    def test_form(self, driver_browser):
        browser = driver_browser

        registration = RegistrationPage(browser)

        with allure.step("Open URL"):
            browser.open(TestPage.set_url())

        with allure.step("Set user data"):
            user = FormRegistration(
                first_name='Антон',
                last_name='Антонов',
                email='anton@anton.ru',
                gender="Other",
                phone_number=7111111111,
                birth_month="November",
                birth_year="2000",
                birth_day="20",
                interests=Hobbies.science.value,
                hobby='Sports',
                photo_path="photo_test.jpg",
                address='USA, 12723 street',
                state='Rajasthan',
                city='Jaiselmer'
            )

        with allure.step("Transmitted user data"):

            registration.registration_user(user, browser)

        with allure.step("Compare transmitted and real data"):
            registration.assert_saved_form(user, browser), \
                "Some field was not corrected"
