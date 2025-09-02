import pytest
import allure
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage

@allure.epic("Products")
@allure.feature("Product Detail View")
@allure.story("TC_8 Product Detail Visibility")
@allure.title("Test Case 8: Verificar visibilidad del detalle de producto")
@allure.description(
    "Desde la lista de productos, accede al detalle del primer producto y "
    "verifica que se muestren nombre, categoría, precio, disponibilidad, condición y marca."
)
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_product_detail_visible(browser):
    products_page = ProductsPage(browser)

    with allure.step("Navegar a la URL principal"):
        # Garantizamos estar en la home independientemente del conftest.py
        browser.get("https://automationexercise.com/")

    with allure.step("Ir a la sección 'Products' desde el navbar"):
        products_page.go_to_products_page()

    with allure.step("Verificar que se cargó 'All Products'"):
        assert products_page.is_products_page_visible(), "La página 'All Products' no se cargó correctamente."

    with allure.step("Verificar que la lista de productos es visible"):
        assert products_page.is_product_list_visible(), "La lista de productos no es visible."

    with allure.step("Hacer clic en 'View Product' del primer producto"):
        products_page.click_view_first_product()

    product_detail = ProductDetailPage(browser)

    with allure.step("Verificar que todos los detalles del producto están visibles"):
        details = product_detail.get_product_details()
        for key, value in details.items():
            assert value.strip() != "", f"El campo '{key}' está vacío o no se encontró."
