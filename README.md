# QA Automation Portfolio – Selenium + Python (POM) sobre Automation Exercise

[![Python](https://img.shields.io/badge/Python-3.12+-blue)]()
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)]()
[![pytest](https://img.shields.io/badge/pytest-8.x-yellow)]()
[![Allure](https://img.shields.io/badge/Allure-Report-orange)]()
[![Linux](https://img.shields.io/badge/OS-Linux-grey)]()

Proyecto de **automatización de pruebas web** sobre **[automationexercise.com](https://automationexercise.com/)** con **Selenium + Python + pytest**, siguiendo **Page Object Model (POM)**.  
Incluye flujos completos de autenticación y el formulario de contacto, con reportes **Allure** y generación de datos con **Faker**.

---
---


- **Pages (POM)**
  - `HomePage`: navegación a Home, acceso a **Signup/Login**, **Contact us**, logout, delete account, etc.
  - `LoginPage`: registro y login (inputs, botones, validaciones).
  - `AccountInfoPage`: alta de cuenta (campos, dropdowns, checkboxes, confirmaciones).
  - `ContactPage`: formulario de contacto, **upload de archivo**, manejo de **alert JS** y confirmación de éxito.
  - `TestCasesPage`: validación de la carga de la página de Test Cases (header y URL correctos).
  - `ProductsPage`: navegación a la sección **All Products**, verificación de lista de productos, acceso a detalles.
  - `ProductDetailPage`: extracción de datos del detalle de un producto (**nombre, categoría, precio, availability, condition, brand**).

- **Tests**
  - `test_auth.py`  
    - **TC_1**: Register User  
    - **TC_2**: Login (credenciales válidas)  
    - **TC_3**: Login (credenciales inválidas)  
    - **TC_4**: Logout
  - `test_contact.py`  
    - **TC_6**: Contact Us Form (completa campos, sube archivo temporal y valida mensaje de éxito)
  - `test_test_cases.py`
    - **TC_7**: Verify Test Cases Page (navega desde Home y valida la carga de la página de Test Cases)
    - **TC_8**: Product Detail Visibility (accede al primer producto y valida que se muestren todos sus detalles)

## Requisitos

- **Python 3.12+**
- **Google Chrome** instalado
- (Opcional) **Allure CLI** para visualizar reportes

---






## Ejecución

Ejecutar todos los tests:
```bash
pytest -q
```

Ejecutar un archivo o caso puntual:
```bash
pytest tests/test_contact.py -q
pytest tests/test_contact.py::test_contact_us_form -q
```

## Pytest Markers
- `@pytest.mark.smoke` → pruebas rápidas y críticas (login, logout, navegación básica).  
- `@pytest.mark.regression` → pruebas de regresión más completas y escenarios negativos.  
- `@pytest.mark.e2e` → flujos end-to-end que recorren múltiples funcionalidades.  

> Los markers están registrados en `pytest.ini` para evitar warnings y poder ejecutar suites específicas, por ejemplo:
> ```bash
> pytest -m smoke
> pytest -m regression
> ```


Para abrir reportes en allure:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```


## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/<tu-usuario>/<tu-repo>.git
cd <tu-repo>

# Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
