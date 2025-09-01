# pages/test_cases_page.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class TestCasesPage(BasePage):
    # El título "Test Cases" que aparece en esa página
    PAGE_HEADER = (By.XPATH, "//h2[normalize-space()='Test Cases']")

    def is_visible(self) -> bool:
        """Devuelve True si el título 'Test Cases' está visible."""
        return self.wait_for_element(self.PAGE_HEADER) is not None

    def url_is_correct(self) -> bool:
        """Valida que la URL actual contenga /test_cases."""
        return "/test_cases" in self.driver.current_url
