import os
from locators.page_locators import PageLocators
from selene import be, have, command

from models.registration_model import FormRegistration


class RegistrationPage:

    def __init__(self, browser):
        self.browser = browser
        self.first_name = browser.element(PageLocators.first_name)
        self.last_name = browser.element(PageLocators.last_name)
        self.email = browser.element(PageLocators.email)
        self.gender = browser.element(PageLocators.gender_other)
        self.phone = browser.element(PageLocators.phone)
        self.hobby_one = browser.element(PageLocators.hobby_field)
        self.hobby_two = browser.element(PageLocators.hobby_choose)
        self.photo = browser.element(PageLocators.photo)
        self.address = browser.element(PageLocators.address)
        self.state = browser.element(PageLocators.state_choose)
        self.city = browser.element(PageLocators.city_choose)
        self.submit = browser.element(PageLocators.submit)

    def open_browser(self):
        self.browser.open(PageLocators.URL)
        return self

    def _set_first_name(self, first_name):
        self.first_name.should(be.blank).type(first_name)
        return self

    def _set_last_name(self, last_name):
        self.last_name.should(be.blank).type(last_name)
        return self

    def _set_email(self, email):
        self.email.should(be.blank).type(email)
        return self

    def _set_gender(self, gender):
        self.gender.should(have.text(gender)).click()
        return self

    def _set_phone(self, phone):
        self.phone.should(be.blank).type(phone)
        return self

    def set_date_birth(self):
        self.browser.element(PageLocators.date_birth_field).click()
        self.browser.element(PageLocators.date_birth_month).click()
        self.browser.element(PageLocators.date_birth_year).click()
        self.browser.element(PageLocators.date_birth_day).click()

        return self

    def _set_hobby_one(self, hobby):
        self.hobby_one.should(be.blank).type(hobby).press_enter()
        return self

    def _set_hobby_two(self, hobby):
        self.hobby_two.should(have.text(hobby)).click()
        return self

    def _set_photo(self, photo):
        self.photo.send_keys(os.getcwd() + "/" + photo)
        return self

    def _set_address(self, address):
        self.address.should(be.blank).type(address)
        return self

    def _set_state(self, state):
        self.state.should(be.blank).type(state).press_enter()
        return self

    def _set_city(self, city):
        self.city.should(be.blank).type(city).press_enter()
        return self

    def click_submit(self):
        self.submit.perform(command.js.click)
        return self

    def registration_user(self, user):
        self._set_first_name(user.first_name)
        print(user.first_name)
        self._set_last_name(user.last_name)
        print(user.last_name)
        self._set_email(user.email)
        print(user.email)
        self._set_gender(user.gender)
        print(user.gender)
        self._set_phone(user.phone_number)
        print(user.phone_number)
        self.set_date_birth()

        self._set_hobby_one(user.interests)
        self._set_hobby_two(user.hobby)
        self._set_photo(user.photo_path)
        self._set_address(user.address)
        self._set_state(user.state)
        self._set_city(user.city)
        self.click_submit()
        return self

    def assert_saved_form(self, user):
        name = user.first_name + ' ' + user.last_name
        birthday = user.birth_day + ' ' + user.birth_month + ',' + user.birth_year
        state_city = user.state + ' ' + user.city

        self.browser.element(PageLocators.element_form_one).all(PageLocators.element_form_two).even.should(
            have.exact_texts(
                name,
                user.email,
                user.gender,
                f'{user.phone_number}',
                birthday,
                user.interests,
                user.hobby,
                user.photo_path,
                user.address,
                state_city
            )
        )
        self.browser.element(PageLocators.close_form).perform(command.js.click)

        return self
