import pytest
import allure
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.home_page import HomePage
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






@allure.title("TC09 - Search Product")
@allure.description("""
Navega al home. Luego hace click en 'products'. Busca un producto en específico y espera que sus resultados sean visibles.
""")
@pytest.mark.smoke
@pytest.mark.products
@pytest.mark.parametrize("search_term", ["dress"])  # acá se puede cambiar el producto a buscar.
def test_search_product(browser, search_term):
    home = HomePage(browser)
    products = ProductsPage(browser)

    # Paso 2: Navegar a la URL
    with allure.step("Navegar a 'http://automationexercise.com'"):
        home.navigate_to("http://automationexercise.com")

    # Paso 3: Verificar home visible
    with allure.step("Verificar que la home esté visible"):
        assert home.is_home_page_visible(), "La home no se visualiza correctamente"

    # Paso 4: Click en 'Products'
    with allure.step("Ir a la sección 'Products'"):
        products.go_to_products_page()

    # Paso 5: Verificar 'All Products' visible
    with allure.step("Verificar que la página 'All Products' esté visible"):
        assert products.is_products_page_visible(), "'All Products' no está visible"

    # Paso 6: Ingresar término de búsqueda y buscar
    with allure.step(f"Buscar el producto: {search_term}"):
        products.search_product(search_term)

    # Paso 7: Verificar 'Searched Products' visible
    with allure.step("Verificar que 'Searched Products' sea visible"):
        assert products.is_search_result_section_visible(), "No se muestra el título 'Searched Products'"

    # Paso 8: Verificar productos visibles (al menos 1 card)
    with allure.step("Verificar que hay productos visibles en los resultados"):
        assert products.are_search_results_visible(), "No se encontraron productos visibles tras la búsqueda"
