import pytest
import allure
from pages.home_page import HomePage
from faker import Faker

fake = Faker()

@allure.epic("Home Page")
@allure.feature("Subscription Section")
@allure.story("TC_10: Verify Subscription in Home Page")
@allure.title("Test Case 10: Verificar suscripción desde el footer")
@allure.description(
    "Desde la página principal, scrollear hasta el footer y verificar que el texto 'SUBSCRIPTION' "
    "esté visible. Ingresar un email válido en el campo correspondiente y presionar el botón de "
    "suscripción. Confirmar que el mensaje 'You have been successfully subscribed!' se muestre correctamente."
)
def test_verify_subscription(browser):
    home_page = HomePage(browser)

    with allure.step("Navegar a la página principal"):
        home_page.go_to()

    with allure.step("Verificar que la página principal se muestre correctamente"):
        assert home_page.is_home_page_visible(), "La home no está visible"

    with allure.step("Scrollear hasta el footer"):
        home_page.scroll_to_footer()

    with allure.step("Verificar que el texto 'SUBSCRIPTION' esté visible"):
        home_page.verify_subscription_text()

    with allure.step("Ingresar email y hacer click en el botón de suscripción"):
        email = fake.email()
        home_page.subscribe(email)

    with allure.step("Verificar que el mensaje de éxito esté visible"):
        home_page.verify_success_message()
