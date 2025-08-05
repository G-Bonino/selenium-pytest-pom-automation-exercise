import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_info_page import AccountInfoPage
import time
import allure

from faker import Faker

@allure.title("Test Case 1: Register User - Hasta click en Signup/Login")
def test_register_user_step1(browser):
    home_page = HomePage(browser)
    login_page = LoginPage(browser)
    account_info_page = AccountInfoPage(browser)
    fake = Faker() 


    with allure.step("Navegar a la página principal"):
        home_page.go_to()
        assert home_page.is_logo_visible(), "No se encontró el logo en la Home"

    with allure.step("Hacer click en 'Signup / Login'"):
        home_page.click_signup_login()


    with allure.step("Verificar que aparece 'New User Signup!'"):
        assert login_page.is_new_user_signup_visible(), "No se muestra 'New User Signup!'"

    name = fake.first_name()
    email = fake.unique.email()
    with allure.step(f"Completar el nombre '{name}' y el email '{email}'"):
        login_page.enter_signup_name(name)
        login_page.enter_signup_email(email)
        print(f"Usuario generado: {name} | {email}")

    with allure.step("Hacer click en 'Signup'"):
        login_page.click_signup_button()


    with allure.step("Seleccionar título 'Mr'"):
        account_info_page.select_title_mr()

    with allure.step("Validar que 'Name' se autocompletó correctamente"):
        name_autocompleted = account_info_page.get_name_value()
        assert name_autocompleted == name, f"El nombre autocompletado '{name_autocompleted}' no coincide con '{name}'"

    with allure.step("Validar que 'Email' se autocompletó correctamente"):
        email_autocompleted = account_info_page.get_email_value()
        assert email_autocompleted == email, f"El email autocompletado '{email_autocompleted}' no coincide con '{email}'"
