# tests/test_contact.py
import os
import tempfile
import pytest
import allure
from faker import Faker
import time

from pages.home_page import HomePage
from pages.contact_page import ContactPage

@allure.title("Test Case 6: Contact Us Form")
@allure.description("Completa el formulario de contacto, sube un archivo y verifica el mensaje de éxito.")
def test_contact_us_form(browser):
    fake = Faker()
    home_page = HomePage(browser)
    contact_page = ContactPage(browser)

    # Datos generados con Faker (usuarios únicos por ejecución)
    name = fake.name()
    email = fake.unique.email()
    subject = fake.sentence(nb_words=4)
    message = fake.paragraph(nb_sentences=3)

    with allure.step("Navegar a la Home"):
        home_page.go_to()
        assert home_page.is_logo_visible(), "La Home no cargó correctamente (logo no visible)."

    with allure.step("Ir a 'Contact Us'"):
        #leé el click contact us desde la home page.
        home_page.click_contact_us()
        assert contact_page.is_loaded(), "No se cargó la sección 'Contact Us'."

    with allure.step("Completar el formulario con datos válidos"):
        contact_page.type_name(name)
        contact_page.type_email(email)
        contact_page.type_subject(subject)
        contact_page.type_message(message)

    # Se crea un archivo temporal para probar el upload
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
    # Escribo contenido dentro del archivo temporal
        tmp.write(f"Evidence for contact form\nUser: {name}\nEmail: {email}\n".encode("utf-8"))
    # Guardo la ruta completa del archivo temporal
        tmp_path = tmp.name

    try:
        # Selenium necesita la ruta ABSOLUTA del archivo para poder "subirlo" al input <type="file">
        # os.path.abspath() convierte tmp_path en una ruta absoluta garantizada
        with allure.step("Subir archivo"):
            contact_page.upload_file(os.path.abspath(tmp_path))


        with allure.step("Enviar el formulario"):
            contact_page.click_submit()

        with allure.step("Verificar mensaje de éxito"):
            assert contact_page.is_success_alert_visible(), \
                "No se mostró el mensaje de éxito del formulario."

        with allure.step("Volver a Home y validar"):
            contact_page.click_home()
            assert home_page.is_logo_visible(), "No se visualiza el logo al volver a la Home."
    finally:
    # El bloque finally se ejecuta SIEMPRE, aunque el test falle.
    # Uso esto para limpiar el archivo temporal y no dejar basura en el sistema.
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

