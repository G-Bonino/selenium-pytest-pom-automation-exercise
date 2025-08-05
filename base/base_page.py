from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        """Navega a la URL indicada."""
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        """Espera hasta que el elemento sea visible y lo devuelve."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Hace click en el elemento identificado por locator."""
        element = self.wait_for_element(locator)
        element.click()

    def type_text(self, locator, text):
        """Limpia y escribe texto en el campo identificado por locator."""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def select_from_dropdown_by_visible_text(self, locator, text):
        """Selecciona una opción del dropdown por el texto visible."""
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(text)

    def select_from_dropdown_by_index(self, locator, index):
        """Selecciona una opción del dropdown por el índice."""
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_index(index)

    def select_checkbox(self, locator):
        """Marca el checkbox si no está seleccionado (por buenas prácticas)."""
        checkbox = self.wait_for_element(locator)
        if not checkbox.is_selected():
            checkbox.click()

    def unselect_checkbox(self, locator):
        """Desmarca el checkbox si está seleccionado."""
        checkbox = self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()

    def select_radio(self, locator):
        """Marca el radio button si no está seleccionado (mismo patrón que checkbox)."""
        radio = self.wait_for_element(locator)
        if not radio.is_selected():
            radio.click()

    def hover_over_element(self, locator):
        """Hace hover (mouse over) sobre el elemento."""
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def get_select_options(self, locator):
        """Devuelve una lista con los textos de todas las opciones de un dropdown."""
        dropdown = Select(self.wait_for_element(locator))
        return [option.text for option in dropdown.options]

    def reload_page(self):
        """Recarga la página actual."""
        self.driver.refresh()

    def is_element_visible(self, locator, timeout=10):
        """Devuelve True si el elemento es visible, False si no (espera hasta timeout)."""
        try:
            self.wait_for_element(locator, timeout)
            return True
        except:
            return False

    def get_input_value(self, locator):
        """
        Obtiene el atributo 'value' de un input.
        Útil para verificar campos completados o campos disabled.
        """
        element = self.wait_for_element(locator)
        return element.get_attribute("value")
