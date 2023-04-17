class PageLocators:
    def set_month_birth(month):
        return f'option[value="{month}"]'

    def set_year_birth(year):
        return f'option[value="{year}"]'

    def set_day_birth(day):
        return f"react-datepicker__day--{day}"

    first_name = '#firstName'
    last_name = '#lastName'
    email = '#userEmail'

    gender_male = '[for="gender-radio-1"]'
    gender_female = '[for="gender-radio-2"]'
    gender_other = '[for="gender-radio-3"]'

    phone = '#userNumber'

    date_birth_field = '#dateOfBirthInput'
    date_birth_month = f'select[class="react-datepicker__month-select"] {set_month_birth("10")}'
    date_birth_year = f'select[class="react-datepicker__year-select"] {set_year_birth("2000")}'
    date_birth_day = f'*[class="react-datepicker__day {set_day_birth("020")}"]'

    hobby_field = '#subjectsInput'
    hobby_choose = '[for="hobbies-checkbox-1"]'

    photo = '#uploadPicture'

    address = '#currentAddress'

    state_choose = '#react-select-3-input'
    city_choose = '#react-select-4-input'

    submit = '#submit'

    element_form_one = '.table'
    element_form_two = 'td'

    close_form = '#closeLargeModal'
