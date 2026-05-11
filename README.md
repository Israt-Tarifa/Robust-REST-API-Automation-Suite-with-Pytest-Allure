# Robust REST API Automation Suite with Pytest & Allure 🚀

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-white.svg)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Report-Allure-green.svg)](https://docs.qameta.io/allure/)

This is a professional-grade API automation framework built to ensure high-quality RESTful service validation. It uses **Python**, **Pytest**, and **Allure Reports** to provide a scalable and highly visual testing experience.
---

## Tools & Technologies

- Python
- Pytest
- Requests
- python-dotenv
- Faker
- pytest-html
- GitHub

---
## 📂 Project Structure

```text
student_api_framework/
│
├── .venv/                     # Virtual environment
│
├── student_api_framework/     # Main project package
│   ├── allure-results/        # Allure raw results (JSON)
│   ├── reports/               # HTML test reports output
│   │
│   ├── testcases/             # Test scripts
│   │   ├── __init__.py
│   │   ├── conftest.py        # Fixtures & global setup
│   │   ├── test_login.py
│   │   ├── test_post_student.py
│   │   ├── test_get_student.py
│   │   ├── test_update_student.py
│   │   └── test_delete_student.py
│   │
│   ├── utils/                # Helper & config layer
│   │   ├── __init__.py
│   │   ├── config.py         # Base URL & environment config
│   │   └── helper_function.py # Reusable API functions
│   │
│   ├── .env                  # Sensitive data (tokens, credentials)
│   ├── .gitignore            # Ignored files list
│   ├── pytest.ini            # Pytest configuration
│   └── requirements.txt      # Project dependencies
```
------

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Israt-Tarifa/Robust-REST-API-Automation-Suite-with-Pytest-Allure.git
cd Robust-REST-API-Automation-Suite-with-Pytest-Allure
```

### 2. Create and Activate Virtual Environment

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment File

Create a `.env` file in the project root:
```
BASE_URL=http://54.255.195.111:5171
API_USERNAME=your_username
API_PASSWORD=your_password
```
> Note: Never commit `.env` to GitHub. It is listed in `.gitignore`.

### 5. Run All Tests
```bash
pytest -v -s
```

### 6. Run a Specific Test File
```bash
pytest testcases/test_post_student.py
```

### 7. Run a Specific Test Function
```bash
pytest testcases/test_delete_student.py::test_delete_student_by_id
```

## Generate & View HTML Report

The HTML report is auto-generated after every test run inside the `reports/` folder.

To generate:
```bash
pytest -v -s
```
To view on Windows:
```bash
start reports/test_report.html
```
To view on macOS:
```bash
open reports/test_report.html
```
## 📊 Test Execution Dashboards

### Allure Overview
Below is the high-level summary of the test execution results, showcasing the pass/fail ratio and overall test health.
![Allure Dashboard](./assets/allure.png)

### Graphical Analysis
Visual representation of test severity, duration, and status trends.
![Test Graphs](./assets/Graphs.png)

### Category & Suite Breakdown
Detailed view of test cases organized by their functional categories and suites.
![Category View](./assets/Catagory.png)

### Execution Timeline
A visual timeline showing when each test was executed and how long it took.
![Timeline](./assets/timeline.png)

---

## 🌟 Project Key Features
*   **Comprehensive API Testing**: Validates REST endpoints for status codes, response bodies, and headers.
*   **Modular Framework**: Separated logic for `test_cases` and `utils` for better maintainability.
*   **Rich Reporting**: Advanced reporting with screenshots, steps, and graphs using Allure.
*   **Configurable**: Easy management of environment settings via `pytest.ini`.

## 👩‍💻 Author
**Israt Jahan Tarifa**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/israt-tarifa/) 
[![GitHub](https://img.shields.io/badge/GitHub-Profile-lightgrey?style=flat&logo=github)](https://github.com/Israt-Tarifa)
