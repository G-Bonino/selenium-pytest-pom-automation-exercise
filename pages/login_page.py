from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    # Locators para el formulario de registro
    NEW_USER_SIGNUP_HEADER = (By.XPATH, "//h2[text()='New User Signup!']")
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    # Locators para logear
    LOGIN_TO_YOUR_ACCOUNT_TEXT = (By.XPATH, "//h2[contains(text(),'Login to your account')]")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')

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


    def is_login_to_your_account_visible(self):
        """Verifica si se muestra el título 'Login to your account' en la pantalla de login."""
        return self.is_element_visible(self.LOGIN_TO_YOUR_ACCOUNT_TEXT)

    def enter_login_email(self, email):
        """Ingresa el email en el campo de login."""
        self.type_text(self.LOGIN_EMAIL_INPUT, email)

    def enter_login_password(self, password):
        """Ingresa el password en el campo de login."""
        self.type_text(self.LOGIN_PASSWORD_INPUT, password)

    def click_login_button(self):
        """Hace click en el botón 'Login'."""
        self.click(self.LOGIN_BUTTON)



