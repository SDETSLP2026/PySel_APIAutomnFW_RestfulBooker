# 🚀 Python API Automation Framework

A **Hybrid Custom API Automation Framework** built using **Python** and **PyTest**, designed for **scalable, maintainable, and enterprise-grade API testing**.
This framework follows industry best practices with a clean folder structure, extensibility, and support for parallel execution and rich reporting.

---

## 📌 Key Highlights

* Modular and scalable folder structure
* Supports CRUD-based API testing
* Parallel execution using PyTest xdist
* Schema validation for advanced API testing
* Rich test reporting with Allure & PyTest HTML
* Easy to extend for CI/CD pipelines (GitHub Actions, Jenkins, GitLab CI)

---
![Screenshot 2024-08-05 at 08 18 38](https://github.com/user-attachments/assets/3c7d5fe5-207a-42e7-84fe-f4d53354d987)


## 📂 Project Structure

```
python-api-automation-framework/
│
├── config/              # Environment & configuration files
├── data/                # Test data (CSV, Excel, JSON)
├── helpers/             # Utility & helper methods
├── payloads/            # Request payloads
├── schemas/             # JSON schema validations
├── tests/
│   ├── crud/             # CRUD-based API tests
│   └── conftest.py       # PyTest fixtures
├── reports/             # Test execution reports
├── requirements.txt     # Project dependencies
└── README.md
```

---

## 🛠 Tech Stack

* **Language**: Python 3.13
* **HTTP Client**: Requests
* **Test Framework**: PyTest
* **Reporting**:

  * Allure Report
  * PyTest HTML
* **Test Data Management**:

  * CSV
  * Excel
  * JSON
  * Faker
* **API Validation**:

  * jsonschema
* **Parallel Execution**:

  * pytest-xdist

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/python-api-automation-framework.git
cd python-api-automation-framework
```

### 2️⃣ Install Dependencies

```bash
pip install requests pytest pytest-html faker allure-pytest jsonschema
```

### 3️⃣ Install Parallel Execution Support

```bash
pip install pytest-xdist
```

---

## ▶️ Running Tests

### ✅ Run a Single Test with Allure Report

```bash
pytest src/tests/crud/test_create_booking.py --alluredir=allure_result
```

### ⚡ Run Tests in Parallel

```bash
pytest -n auto
```

### 📊 Generate Allure Report

```bash
allure serve allure_result
```

---

## 🧪 Supported Test Scenarios

* CRUD API testing
* Schema validation
* Data-driven testing
* Negative and edge-case testing
* Parallel test execution
* CI/CD-friendly execution

---

## 👨‍💻 Author

**Pramod Dutta**
QA Leader | SDET | Automation Architect | Educator

## 👨‍💻 Edited By

**Swapnil Padekar**

---

## 🌐 Community & Learning Resources

* 🌍 **Website**: [https://thetestingacademy.com](https://thetestingacademy.com)
* 💼 **LinkedIn**: [https://www.linkedin.com/in/pramoddutta](https://www.linkedin.com/in/pramoddutta)
* 📺 **YouTube**: [https://www.youtube.com/@TheTestingAcademy](https://www.youtube.com/@TheTestingAcademy)
* 📸 **Instagram**: [https://www.instagram.com/thetestingacademy](https://www.instagram.com/thetestingacademy)
* 📝 **Blog**: [https://scrolltest.com](https://scrolltest.com)
* 🧠 **Courses & Mentorship**: [https://thetestingacademy.com](https://thetestingacademy.com)

---

## 🤝 Contributions

Contributions are welcome!
If you’d like to improve this framework:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it with attribution.

---

## ⭐ Support the Project

If you find this framework helpful:

* Star ⭐ the repository
* Share it with the QA & Testing community
* Subscribe to **The Testing Academy** on YouTube
