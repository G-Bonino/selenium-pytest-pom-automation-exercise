from selenium.webdriver.common.by import By
from base.base_page import BasePage

class HomePage(BasePage):
    # Locator para el logo (verifica que estás en la Home)
    LOGO = (By.CSS_SELECTOR, "img[alt='Website for automation practice']")
    # Locator para el botón 'Signup / Login'

    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")

    def go_to(self):
        """Navega a la página principal."""
        self.navigate_to("https://automationexercise.com/")

    def is_logo_visible(self):
        """Verifica si el logo está visible (confirma que es que la Home está cargando correctamente)."""
        return self.is_element_visible(self.LOGO)
        

    def click_signup_login(self):
        """Hace click en el botón 'Signup / Login'."""
        self.click(self.SIGNUP_LOGIN_BUTTON)
