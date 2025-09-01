
import allure
import pytest
from pages.home_page import HomePage
from pages.cases_page import TestCasesPage

@allure.epic("Navigation")
@allure.feature("Navigation")
@allure.story("TC_7 Verify Test Cases Page")
@allure.title("TC_7 - Verify Test Cases Page")
@allure.description("Verifica que al hacer clic en 'Test Cases' desde Home, se cargue la página de casos de prueba correctamente.")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.smoke
def test_verify_test_cases_page(browser):
    home = HomePage(browser)
    tc_page = TestCasesPage(browser)

    with allure.step("1-2) Navegar al Home"):
        home.go_to()
        assert "automationexercise" in browser.current_url, "No se abrió el Home"

    with allure.step("3) Verificar Home abierto"):
        assert browser.title != "", "El título de Home no se cargó"  

    with allure.step("4) Hacer clic en 'Test Cases'"):
        home.click_test_cases()

    with allure.step("5) Verificar página Test Cases"):
        assert tc_page.is_visible(), "La página 'Test Cases' no cargó correctamente"
        assert tc_page.url_is_correct(), "La URL de 'Test Cases' no es la esperada"