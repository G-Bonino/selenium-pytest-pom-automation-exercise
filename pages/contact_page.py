from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from base.base_page import BasePage
import allure

class ContactPage(BasePage):
    """
    Contact Us – prioridad de selectores:
    1) ID  2) data-qa  3) name  4) CSS/XPath robusto (último recurso)
    """

    # Encabezado real: <h2 class="title text-center">Contact <strong>Us</strong></h2>
    CONTACT_HEADING = (
        By.XPATH,
        "//h2[@class='title text-center' and contains(., 'Contact') and contains(., 'Us')]"
    )

    # Campos del formulario (ID > data-qa > name)
    NAME_INPUT       = (By.CSS_SELECTOR, "[data-qa='name']")     # no hay id
    EMAIL_INPUT      = (By.CSS_SELECTOR, "[data-qa='email']")    # no hay id
    SUBJECT_INPUT    = (By.CSS_SELECTOR, "[data-qa='subject']")  # no hay id
    MESSAGE_TEXTAREA = (By.ID, "message")                        # sí hay id

    # Upload (sin id/data-qa)
    FILE_INPUT       = (By.NAME, "upload_file")

    # Submit (a veces existe data-qa; si no, fallback por tipo)
    SUBMIT_PRIMARY   = (By.CSS_SELECTOR, "[data-qa='submit-button']")
    SUBMIT_FALLBACK  = (By.CSS_SELECTOR, "input[type='submit']")

    # Mensaje inline de éxito
    SUCCESS_ALERT    = (By.CSS_SELECTOR, ".status.alert.alert-success")

    # Botón Home (el que mostraste)
    HOME_BUTTON      = (By.CSS_SELECTOR, "a.btn.btn-success[href='/']")

    # ============== Helpers internos ==============

    def _accept_js_alert_if_present(self, timeout=2) -> bool:
        """Acepta un alert() de JS si aparece; devuelve True si lo aceptó."""
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            # opcional: print(alert.text)
            alert.accept()
            return True
        except TimeoutException:
            return False

    # ============== Flujo de página ==============

    def is_loaded(self) -> bool:
        """La página está lista si vemos el encabezado o el primer input del formulario."""
        return self.is_element_visible(self.CONTACT_HEADING) or self.is_element_visible(self.NAME_INPUT)

    @allure.step("Completar nombre")
    def type_name(self, name: str):
        self.type_text(self.NAME_INPUT, name)

    @allure.step("Completar email")
    def type_email(self, email: str):
        self.type_text(self.EMAIL_INPUT, email)

    @allure.step("Completar subject")
    def type_subject(self, subject: str):
        self.type_text(self.SUBJECT_INPUT, subject)

    @allure.step("Completar mensaje")
    def type_message(self, message: str):
        self.type_text(self.MESSAGE_TEXTAREA, message)

    @allure.step("Subir archivo")
    def upload_file(self, file_path: str):
        self.wait_for_element(self.FILE_INPUT).send_keys(file_path)

    @allure.step("Enviar formulario de contacto")
    def click_submit(self):
        """Click en submit; intenta por data-qa y si no está, por type='submit'. Luego acepta alert si aparece."""
        try:
            self.click(self.SUBMIT_PRIMARY)
        except Exception:
            self.click(self.SUBMIT_FALLBACK)
        # aceptar posible alert JS
        self._accept_js_alert_if_present(timeout=3)

    @allure.step("Verificar éxito del envío")
    def is_success_alert_visible(self) -> bool:
        """
        Éxito si:
          - hubo alert JS (ya aceptado), o
          - aparece el div .status.alert.alert-success
        """
        # por si el test llama esto sin haber pasado por click_submit:
        if self._accept_js_alert_if_present(timeout=1):
            return True
        return self.is_element_visible(self.SUCCESS_ALERT)

    @allure.step("Volver a Home")
    def click_home(self):
        """Click en el botón Home y dejar que la navegación siga."""
        self.click(self.HOME_BUTTON)
