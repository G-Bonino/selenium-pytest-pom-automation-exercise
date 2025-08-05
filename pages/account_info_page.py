from selenium.webdriver.common.by import By
from base.base_page import BasePage

class AccountInfoPage(BasePage):
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
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@data-qa="create-account"]') # Verificá el XPATH si el botón es <button>. Si es <input>, corregimos.


    def select_title_mr(self):
        """Selecciona el título 'Mr' (por ID)."""
        self.select_element(self.TITLE_MR_RADIO)

    def get_name_value(self):
        """Devuelve el valor del campo 'Name'."""
        return self.get_input_value(self.NAME_INPUT)

    def get_email_value(self):
        """Devuelve el valor del campo 'Email' (aunque esté disabled)."""
        return self.get_input_value(self.EMAIL_INPUT)


