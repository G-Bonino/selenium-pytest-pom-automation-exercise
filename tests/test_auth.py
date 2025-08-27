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
@allure.description("Este test registra un usuario y lo elimina. Usa Faker para crear datos falsos")

def test_register_user(browser,fake_user_data):
    home_page = HomePage(browser)
    login_page = LoginPage(browser)
    # Instancia del Page Object que representa la sección 'Enter Account Information'
    # Hereda de BasePage, por lo que puede usar métodos reutilizables como click, type_text, etc.
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

# De acá en adelante en el test se usa lo creado en account_info_page para respetar el page object model.
    with allure.step("Completar el formulario de cuenta y crear la cuenta"):
        account_info_page.fill_account_information(user)
        account_info_page.click_create_account()

    with allure.step("Validar que el mensaje 'ACCOUNT CREATED!' esté visible"):
        assert account_info_page.is_account_created_message_visible(), "No se encontró el mensaje de éxito 'ACCOUNT CREATED!'"

    with allure.step("Hacer click en el botón 'Continue'"):
        account_info_page.click_continue_button()

# vuelve a usar lo de la home

    with allure.step("Verificar que se muestra 'Logged in as <nombre>' en la Home"):
        assert home_page.is_logged_in_as_visible(user["name"]), f"No se encontró el mensaje 'Logged in as {user['name']}'"

    with allure.step("Hacer click en 'Delete Account'"):
        home_page.click_delete_account()


# vuelve a la account_info_page
    with allure.step("Validar que el mensaje 'ACCOUNT DELETED!' esté visible"):
        assert account_info_page.is_account_deleted_message_visible(), "No se encontró el mensaje 'ACCOUNT DELETED!'"

    with allure.step("Hacer click en el botón 'Continue' tras eliminar la cuenta"):
        account_info_page.click_continue_button()




@allure.title("Test Case 2: Login con usuario existente")
@allure.description("Este test verifica que un usuario puede loguearse correctamente y luego eliminar la cuenta.")
def test_login_user_with_correct_credentials(browser):
    home_page = HomePage(browser)
    login_page = LoginPage(browser)
    account_info_page = AccountInfoPage(browser)

    email = "testeando@gmail.com"
    password = "test"
    name = "test"  # Solo para validación del mensaje 'Logged in as'

    with allure.step("Navegar a la página principal"):
        home_page.go_to()
        assert home_page.is_logo_visible()

    with allure.step("Hacer click en 'Signup / Login'"):
        home_page.click_signup_login()

    with allure.step("Verificar que aparece 'Login to your account'"):
        assert login_page.is_login_to_your_account_visible()

    with allure.step("Ingresar email y contraseña válidos"):
        login_page.enter_login_email(email)
        login_page.enter_login_password(password)

    with allure.step("Hacer click en 'Login'"):
        login_page.click_login_button()

    with allure.step("Verificar que se muestra 'Logged in as <nombre>' en la Home"):
        assert home_page.is_logged_in_as_visible(name), f"No se encontró el mensaje 'Logged in as {name}'"

    with allure.step("Eliminar la cuenta"):
        home_page.click_delete_account()

    with allure.step("Verificar que se muestra 'ACCOUNT DELETED!'"):
        assert account_info_page.is_account_deleted_message_visible()

    with allure.step("Click en botón 'Continue' después de eliminar la cuenta"):
        account_info_page.click_continue_button()



@allure.title("Test Case 3: Login con usuario y contraseña incorrectos")
@allure.description("Verifica que se muestre el mensaje de error al intentar loguearse con credenciales inválidas.")
def test_login_user_with_incorrect_credentials(browser):
    fake = Faker()
    home_page = HomePage(browser)
    login_page = LoginPage(browser)

    fake_email = fake.unique.email()
    fake_password = fake.password()

    with allure.step("Navegar a la página principal"):
        home_page.go_to()
        assert home_page.is_logo_visible()

    with allure.step("Hacer click en 'Signup / Login'"):
        home_page.click_signup_login()

    with allure.step("Verificar que aparece 'Login to your account'"):
        assert login_page.is_login_to_your_account_visible()

    with allure.step(f"Ingresar email inválido '{fake_email}' y password inválido"):
        login_page.enter_login_email(fake_email)
        login_page.enter_login_password(fake_password)

    with allure.step("Hacer click en 'Login'"):
        login_page.click_login_button()

    with allure.step("Verificar que se muestra el mensaje de error"):
        assert login_page.is_login_error_visible(), "No se mostró el mensaje de error por login inválido"