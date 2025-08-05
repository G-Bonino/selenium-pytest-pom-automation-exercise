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

@pytest.fixture
def fake_user_data():
    fake = Faker()
    return {
        "name": fake.first_name(),
        "email": fake.unique.email(),
        "password": fake.password(length=10, special_chars=True),
        "first_name": "",    # Se autocompleta igual que name
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile_number": fake.phone_number(),
    }



@allure.title("Test Case 1: Register User")
def test_register_user_step1(browser,fake_user_data):
    home_page = HomePage(browser)
    login_page = LoginPage(browser)
    account_info_page = AccountInfoPage(browser)
    # Accedo a todos los datos desde el diccionario
    user = fake_user_data

    with allure.step("Navegar a la página principal"):
        home_page.go_to()
        assert home_page.is_logo_visible(), "No se encontró el logo en la Home"

    with allure.step("Hacer click en 'Signup / Login'"):
        home_page.click_signup_login()


    with allure.step("Verificar que aparece 'New User Signup!'"):
        assert login_page.is_new_user_signup_visible(), "No se muestra 'New User Signup!'"

    with allure.step(f"Completar el nombre '{user['name']}' y el email '{user['email']}'"):
        login_page.enter_signup_name(user['name'])
        login_page.enter_signup_email(user['email'])
        print(f"Usuario generado: {user['name']} | {user['email']}")

    with allure.step("Hacer click en 'Signup'"):
        login_page.click_signup_button()

    with allure.step("Seleccionar título 'Mr'"):
        account_info_page.select_title_mr()

    with allure.step("Validar que 'Name' se autocompletó correctamente"):
        name_autocompleted = account_info_page.get_name_value()
        assert name_autocompleted == user['name'], (
            f"El nombre autocompletado '{name_autocompleted}' no coincide con '{user['name']}'"
        )

    with allure.step("Validar que 'Email' se autocompletó correctamente"):
        email_autocompleted = account_info_page.get_email_value()
        assert email_autocompleted == user['email'], (
            f"El email autocompletado '{email_autocompleted}' no coincide con '{user['email']}'"
        )

    # Luego usás el mismo diccionario para llenar el formulario completo:
    account_info_page.fill_account_information(user)
    account_info_page.click_create_account()

    time.sleep(10)