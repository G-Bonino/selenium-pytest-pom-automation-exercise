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

- **Tests**
  - `test_auth.py`  
    - **TC_1**: Register User  
    - **TC_2**: Login (credenciales válidas)  
    - **TC_3**: Login (credenciales inválidas)  
    - **TC_4**: Logout
  - `test_contact.py`  
    - **TC_6**: Contact Us Form (completa campos, sube archivo temporal y valida mensaje de éxito)

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

Abrir reportes en allure:
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
