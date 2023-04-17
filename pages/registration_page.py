import os

from selene.support.shared import browser
from locators.page_locators import PageLocators
from selene import be, have, command


class RegistrationPage:
    def __init__(self):
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

    def set_first_name(self, first_name):
        self.first_name.should(be.blank).type(first_name)
        return

    def set_last_name(self, last_name):
        self.last_name.should(be.blank).type(last_name)
        return

    def set_email(self, email):
        self.email.should(be.blank).type(email)
        return

    def set_gender(self, gender):
        self.gender.should(have.text(gender)).click()
        return

    def set_phone(self, phone):
        self.phone.should(be.blank).type(phone)
        return

    def set_date_birth(self):
        browser.element(PageLocators.date_birth_field).click()

        browser.element(PageLocators.date_birth_month).click()
        browser.element(PageLocators.date_birth_year).click()
        browser.element(PageLocators.date_birth_day).click()

        return

    def set_hobby_one(self, hobby):
        self.hobby_one.should(be.blank).type(hobby).press_enter()
        return

    def set_hobby_two(self, hobby):
        self.hobby_two.should(have.text(hobby)).click()
        return

    def set_photo(self, photo):
        self.photo.send_keys(os.getcwd() + "/" + photo)
        return

    def set_address(self, address):
        self.address.should(be.blank).type(address)
        return

    def set_state(self, state):
        self.state.should(be.blank).type(state).press_enter()
        return

    def set_city(self, city):
        self.city.should(be.blank).type(city).press_enter()
        return

    def click_submit(self):
        self.submit.perform(command.js.click)
        return

    def registration_user(self, user):
        self.set_first_name(user.first_name)
        self.set_last_name(user.last_name)
        self.set_email(user.email)
        self.set_gender(user.gender)
        self.set_phone(user.phone_number)
        self.set_date_birth()
        self.set_hobby_one(user.interests)
        self.set_hobby_two(user.hobby)
        self.set_photo(user.photo_path)
        self.set_address(user.address)
        self.set_state(user.state)
        self.set_city(user.city)
        self.click_submit()
        return

    def assert_saved_form(self, user):
        name = user.first_name + ' ' + user.last_name
        birthday = user.birth_day + ' ' + user.birth_month + ',' + user.birth_year
        state_city = user.state + ' ' + user.city

        browser.element(PageLocators.element_form_one).all(PageLocators.element_form_two).even.should(
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
        browser.element(PageLocators.close_form).perform(command.js.click)
