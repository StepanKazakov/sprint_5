import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import locators


@pytest.mark.order(1)
def test_registration_with_random_data(site, wait, user_credentials):
    # Extract credentials provided by the fixture
    login, password = user_credentials
    # Wait until the personal area link is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
    site.find_element(By.XPATH, locators.header_personal_area_btn).click()
    # Wait until the register button is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.do_register)))
    site.find_element(By.XPATH, locators.do_register).click()
    # Wait until the registration form is ready and fill it with the generated data
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.register_btn)))
    site.find_element(By.XPATH, locators.input_name).send_keys('VIP client')
    site.find_element(By.XPATH, locators.input_email).send_keys(login)
    site.find_element(By.XPATH, locators.input_password).send_keys(password)
    # Submit the registration form
    site.find_element(By.XPATH, locators.register_btn).click()
    # Ensure that after registration, the user is redirected to the login page
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
    assert site.current_url == 'https://stellarburgers.nomoreparties.site/login'


@pytest.mark.order(2)
def test_registration_with_incorrect_password_get_mistake(site, wait):
    # Wait until the personal area link is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
    site.find_element(By.XPATH, locators.header_personal_area_btn).click()
    # Wait until the register button is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.do_register)))
    site.find_element(By.XPATH, locators.do_register).click()
    # Wait until the registration form is ready and fill it with incorrect password - less than 6 symbols length
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.register_btn)))
    site.find_element(By.XPATH, locators.input_name).send_keys('wrong client')
    site.find_element(By.XPATH, locators.input_email).send_keys('123@ya.ru')
    site.find_element(By.XPATH, locators.input_password).send_keys(credentials.wrong_password())
    # Submit the registration form
    site.find_element(By.XPATH, locators.register_btn).click()
    # Ensure that after click registration, the user stayed at same page and got error description
    assert site.current_url == 'https://stellarburgers.nomoreparties.site/register' and \
           site.find_element(By.XPATH, locators.incorrect_password).text == 'Некорректный пароль'
