import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import locators


@pytest.mark.order(3)
def test_login_from_login_button(site, wait, user_credentials):
    # Extract credentials provided by the fixture
    login, password = user_credentials
    # Wait until the account login button is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
    site.find_element(By.XPATH, locators.login_or_make_order_btn).click()
    # Wait until the login button is clickable, then fill fields login, password, and click login
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
    site.find_element(By.XPATH, locators.login_input_email).send_keys(login)
    site.find_element(By.XPATH, locators.login_input_password).send_keys(password)
    site.find_element(By.XPATH, locators.login_btn).click()
    # Ensure that after authorisation returned to main page and 'account login' button changed to 'make order' button
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
    assert site.current_url == 'https://stellarburgers.nomoreparties.site/' and \
           site.find_element(By.XPATH, locators.login_or_make_order_btn).text == 'Оформить заказ'


@pytest.mark.order(4)
def test_login_to_personal_area(site, wait, user_credentials):
    # Extract credentials provided by the fixture
    login, password = user_credentials
    # Wait until the personal area link is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
    site.find_element(By.XPATH, locators.header_personal_area_btn).click()
    # Wait until the login button is clickable, then fill fields login, password, and click login
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
    site.find_element(By.XPATH, locators.login_input_email).send_keys(login)
    site.find_element(By.XPATH, locators.login_input_password).send_keys(password)
    site.find_element(By.XPATH, locators.login_btn).click()
    # Ensure that after authorisation returned to main page and 'account login' button changed to 'make order' button
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
    assert site.current_url == 'https://stellarburgers.nomoreparties.site/' and \
           site.find_element(By.XPATH, locators.login_or_make_order_btn).text == 'Оформить заказ'


@pytest.mark.order(5)
def test_login_from_registration_page(site, wait, user_credentials):
    # Extract credentials provided by the fixture
    login, password = user_credentials
    # Wait until the account login button is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
    site.find_element(By.XPATH, locators.login_or_make_order_btn).click()
    # Wait until the registration button is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.do_register)))
    site.find_element(By.XPATH, locators.do_register).click()
    # Wait until the login link on registration page is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_link)))
    site.find_element(By.XPATH, locators.login_link).click()
    # Wait until the login button is clickable, then fill fields login, password, and click login
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
    site.find_element(By.XPATH, locators.login_input_email).send_keys(login)
    site.find_element(By.XPATH, locators.login_input_password).send_keys(password)
    site.find_element(By.XPATH, locators.login_btn).click()
    # Ensure that after authorisation returned to main page and 'account login' button changed to 'make order' button
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
    assert site.current_url == 'https://stellarburgers.nomoreparties.site/' and \
           site.find_element(By.XPATH, locators.login_or_make_order_btn).text == 'Оформить заказ'


@pytest.mark.order(6)
def test_login_from_password_recovery_page(site, wait, user_credentials):
    # Extract credentials provided by the fixture
    login, password = user_credentials
    # Wait until the account login button is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
    site.find_element(By.XPATH, locators.login_or_make_order_btn).click()
    # Wait until the password recovery button is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.password_recovery)))
    site.find_element(By.XPATH, locators.password_recovery).click()
    # Wait until the login link on password recovery page is clickable and then click it
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_link)))
    site.find_element(By.XPATH, locators.login_link).click()
    # Wait until the login button is clickable, then fill fields login, password, and click login
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
    site.find_element(By.XPATH, locators.login_input_email).send_keys(login)
    site.find_element(By.XPATH, locators.login_input_password).send_keys(password)
    site.find_element(By.XPATH, locators.login_btn).click()
    # Ensure that after authorisation returned to main page and 'account login' button changed to 'make order' button
    wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
    assert site.current_url == 'https://stellarburgers.nomoreparties.site/' and \
           site.find_element(By.XPATH, locators.login_or_make_order_btn).text == 'Оформить заказ'