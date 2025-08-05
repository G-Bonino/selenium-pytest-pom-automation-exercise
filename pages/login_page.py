from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    # Locators para el formulario de registro
    NEW_USER_SIGNUP_HEADER = (By.XPATH, "//h2[text()='New User Signup!']")
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def is_new_user_signup_visible(self):
        """Verifica si el encabezado 'New User Signup!' está visible."""
        return self.is_element_visible(self.NEW_USER_SIGNUP_HEADER)

    def enter_signup_name(self, name):
        """Escribe el nombre en el campo de registro."""
        self.type_text(self.SIGNUP_NAME_INPUT, name)

    def enter_signup_email(self, email):
        """Escribe el email en el campo de registro."""
        self.type_text(self.SIGNUP_EMAIL_INPUT, email)

    def click_signup_button(self):
        """Hace click en el botón de 'Signup'."""
        self.click(self.SIGNUP_BUTTON)
