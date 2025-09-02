# pages/product_detail_page.py

from selenium.webdriver.common.by import By
from base.base_page import BasePage
import allure

class ProductDetailPage(BasePage):
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']//h2")
    PRODUCT_CATEGORY = (By.XPATH, "//div[@class='product-information']//p[starts-with(normalize-space(),'Category')]")
    # precio: suele estar como "Rs. 500" dentro de un <span>
    PRODUCT_PRICE = (By.XPATH, "//div[@class='product-information']//span[contains(., 'Rs.')]")
    # estos tres vienen como <p><b>Label:</b> valor</p>
    PRODUCT_AVAILABILITY = (By.XPATH, "//div[@class='product-information']//p[./b[contains(.,'Availability')]]")
    PRODUCT_CONDITION = (By.XPATH, "//div[@class='product-information']//p[./b[contains(.,'Condition')]]")
    PRODUCT_BRAND = (By.XPATH, "//div[@class='product-information']//p[./b[contains(.,'Brand')]]")

    @allure.step("Obtener detalles visibles del producto")
    def get_product_details(self):
        return {
            "name": self.get_text(self.PRODUCT_NAME),
            "category": self.get_text(self.PRODUCT_CATEGORY),
            "price": self.get_text(self.PRODUCT_PRICE),
            "availability": self.get_text(self.PRODUCT_AVAILABILITY),
            "condition": self.get_text(self.PRODUCT_CONDITION),
            "brand": self.get_text(self.PRODUCT_BRAND),
        }
