from selenium.webdriver.common.by import By
from base.base_page import BasePage
import allure

class AccountInfoPage(BasePage):
    # --- Locators de todos los campos y botones del formulario ---
    TITLE_MR_RADIO = (By.ID, "id_gender1")
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS1_INPUT = (By.ID, "address1")
    ADDRESS2_INPUT = (By.ID, "address2")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = (By.ID, "mobile_number")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_CHECKBOX = (By.ID, "optin")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="create-account"]')
    DATE_DAY_DROPDOWN = (By.ID, "days") 
    DATE_MONTH_DROPDOWN = (By.ID, "months")
    DATE_YEAR_DROPDOWN = (By.ID, "years")
    ACCOUNT_CREATED_MESSAGE = (By.CSS_SELECTOR, 'h2[data-qa="account-created"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[data-qa="continue-button"]')  
    ACCOUNT_DELETED_MESSAGE = (By.CSS_SELECTOR, 'h2[data-qa="account-deleted"]')


    def select_title_mr(self):
        """
        Selecciona el radio button 'Mr' como título.
        Útil para tests que requieren completar datos de género.
        """
        self.select_radio(self.TITLE_MR_RADIO)

    def get_name_value(self):
        """
        Devuelve el valor actual del input 'Name' (autocompletado).
        Se usa para validar que el nombre fue transferido correctamente desde la pantalla anterior.
        """
        return self.get_input_value(self.NAME_INPUT)

    def get_email_value(self):
        """
        Devuelve el valor actual del input 'Email' (autocompletado y deshabilitado).
        Útil para verificar el flujo de datos entre pantallas.
        """
        return self.get_input_value(self.EMAIL_INPUT)

    # --- Métodos para escribir texto en los campos del formulario ---

    def type_password(self, password):
        """Completa el campo Password."""
        self.type_text(self.PASSWORD_INPUT, password)


    def type_first_name(self, first_name):
        """Completa el campo First Name."""
        self.type_text(self.FIRST_NAME_INPUT, first_name)

    def type_last_name(self, last_name):
        """Completa el campo Last Name."""
        self.type_text(self.LAST_NAME_INPUT, last_name)

    def type_company(self, company):
        """Completa el campo Company."""
        self.type_text(self.COMPANY_INPUT, company)

    def type_address1(self, address1):
        """Completa el campo Address 1 (dirección principal)."""
        self.type_text(self.ADDRESS1_INPUT, address1)

    def type_address2(self, address2):
        """Completa el campo Address 2 (dirección secundaria, opcional)."""
        self.type_text(self.ADDRESS2_INPUT, address2)

    def type_state(self, state):
        """Completa el campo State."""
        self.type_text(self.STATE_INPUT, state)

    def type_city(self, city):
        """Completa el campo City."""
        self.type_text(self.CITY_INPUT, city)

    def type_zipcode(self, zipcode):
        """Completa el campo Zipcode (código postal)."""
        self.type_text(self.ZIPCODE_INPUT, zipcode)

    def type_mobile_number(self, mobile_number):
        """Completa el campo Mobile Number."""
        self.type_text(self.MOBILE_NUMBER_INPUT, mobile_number)

    # --- Métodos para checkboxes ---

    def check_newsletter(self):
        """Marca el checkbox 'Sign up for our newsletter!' si no está marcado."""
        self.select_checkbox(self.NEWSLETTER_CHECKBOX)

    def check_offers(self):
        """Marca el checkbox 'Receive special offers from our partners!' si no está marcado."""
        self.select_checkbox(self.OFFERS_CHECKBOX)



    @allure.step("Completar formulario de Account Information")
    def fill_account_information(self, user, day="5", month="March", year="2014"):
        """
        Completa el formulario de datos de cuenta usando los datos del diccionario 'user'.
        """
        self.type_password(user["password"])
        self.select_from_dropdown_by_visible_text(self.DATE_DAY_DROPDOWN, day)
        self.select_from_dropdown_by_visible_text(self.DATE_MONTH_DROPDOWN, month)
        self.select_from_dropdown_by_visible_text(self.DATE_YEAR_DROPDOWN, year)
        self.check_newsletter()
        self.check_offers()
        self.type_first_name(user["name"])  # Usamos el 'name' generado con Faker como primer nombre
        self.type_last_name(user["last_name"])
        self.type_company(user["company"])
        self.type_address1(user["address1"])
        self.type_address2(user["address2"])
        self.type_state(user["state"])
        self.type_city(user["city"])
        self.type_zipcode(user["zipcode"])
        self.type_mobile_number(user["mobile_number"])




    @allure.step("Click en 'Create Account'")
    def click_create_account(self):
        """Hace click en el botón para crear la cuenta."""
        self.click(self.CREATE_ACCOUNT_BUTTON)

    @allure.step("Validar que el mensaje 'Account Created!' esté visible")
    def is_account_created_message_visible(self):
        """
        Verifica si el mensaje 'ACCOUNT CREATED!' está visible en la página luego de crear el usuario
        """
        return self.is_element_visible(self.ACCOUNT_CREATED_MESSAGE)



    @allure.step("Click en botón 'Continue'")
    def click_continue_button(self):
        """
        Hace click en el botón 'Continue' que aparece después del mensaje 'ACCOUNT CREATED!'.
        """
        self.click(self.CONTINUE_BUTTON)


    @allure.step("Verificar que el mensaje 'ACCOUNT DELETED!' esté visible")
    def is_account_deleted_message_visible(self):
        """
        Verifica que se muestra el mensaje 'ACCOUNT DELETED!' después de eliminar la cuenta.
        """
        return self.wait_for_element(self.ACCOUNT_DELETED_MESSAGE).is_displayed()

