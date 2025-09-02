from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
import allure

class ProductsPage(BasePage):
    # Locators
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    SALE_IMAGE = (By.ID, "sale_image")
    ALL_PRODUCTS_TITLE = (By.XPATH, "//h2[@class='title text-center' and normalize-space()='All Products']")
    FIRST_VIEW_PRODUCT_BUTTON = (By.XPATH, "(//a[contains(@href, '/product_details')])[1]")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".features_items .col-sm-4")  # items en el grid

    @allure.step("Ir a la sección de Productos desde el navbar")
    def go_to_products_page(self):
        """Hace click en el botón de navegación hacia la sección Products"""
        self.click(self.PRODUCTS_BUTTON)

    @allure.step("Verificar que la página 'All Products' se haya cargado")
    def is_products_page_visible(self):
        """True si se ve la imagen 'sale' y el título 'All Products'"""
        return self.is_element_visible(self.SALE_IMAGE) and self.is_element_visible(self.ALL_PRODUCTS_TITLE)

    @allure.step("Verificar que la lista de productos es visible")
    def is_product_list_visible(self, timeout: int = 10) -> bool:
        """Espera que exista al menos un card de producto visible"""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_any_elements_located(self.PRODUCT_CARDS)
        )
        return True
    
    @allure.step("Hacer clic en 'View Product' del primer producto")
    def click_view_first_product(self):
        btn = self.wait_for_element(self.FIRST_VIEW_PRODUCT_BUTTON)
        url = btn.get_attribute("href")
        self.driver.get(url)
