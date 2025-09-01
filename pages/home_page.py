from selenium.webdriver.common.by import By
from base.base_page import BasePage

class HomePage(BasePage):
    # Locator para el logo (verifica que estás en la Home)
    LOGO = (By.CSS_SELECTOR, "img[alt='Website for automation practice']")
    # Locator para el botón 'Signup / Login'

    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    LOGGED_IN_AS_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]") # texto que verifica si ya estamos loggeados

    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/delete_account') and contains(text(), 'Delete Account')]")

    LOGOUT_BUTTON = (By.XPATH, "//a[contains(@href, '/logout') and contains(text(), 'Logout')]")

    CONTACT_US_LINK = (By.LINK_TEXT, "Contact us")
    
    def go_to(self):
        """Navega a la página principal."""
        self.navigate_to("https://automationexercise.com/")

    def is_logo_visible(self):
        """Verifica si el logo está visible (confirma que es que la Home está cargando correctamente)."""
        return self.is_element_visible(self.LOGO)
        

    def click_signup_login(self):
        """Hace click en el botón 'Signup / Login'."""
        self.click(self.SIGNUP_LOGIN_BUTTON)


    def is_logged_in_as_visible(self, expected_name):
        """
        Verifica que el mensaje 'Logged in as <nombre>' esté visible y contenga el nombre esperado.
        """
        element = self.wait_for_element(self.LOGGED_IN_AS_TEXT)
        return expected_name in element.text


    def click_delete_account(self):
        """
        Hace click en el botón 'Delete Account' desde la Home.
        """
        self.click(self.DELETE_ACCOUNT_BUTTON)


    def click_logout(self):
        """Hace click en el botón 'Logout' desde la Home."""
        self.click(self.LOGOUT_BUTTON)


    def click_contact_us(self):
        """Abre la pantalla 'Contact Us' desde la Home."""
        self.click(self.CONTACT_US_LINK)