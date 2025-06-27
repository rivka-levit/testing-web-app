# 📚 Bookstore Website - Selenium Test Automation Project


### Overview

This repository contains the final project from the course 
["Test Automation with Selenium and Python"](https://stepik.org/course/575). 
The project demonstrates how to automate end-to-end tests for a bookstore 
website using:

✅ Selenium WebDriver  
✅ pytest as the test runner  
✅ Page Object Model (POM) for maintainable and scalable test structure

The goal of this project is to practice real-world test automation techniques for web applications and serve as a solid 
foundation for future automation projects.

<br>

### 🛠️ Tech Stack

- Python 3.x
- Selenium WebDriver
- pytest
- Page Object Model (POM) Design Pattern

<br>

### ▶️ Setup Instructions

1. Clone the Repository
    ```
    git clone https://github.com/rivka-levit/testing-web-app.git
    cd testing-web-app
    ```

2. Set Up Virtual Environment
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install Dependencies
    ```
    pip install -r requirements.txt
    ```

4. Download WebDriver  
    Make sure you have the appropriate ChromeDriver in your system 
    PATH.

    For ChromeDriver: https://sites.google.com/chromium.org/driver/

<br>

### 🧪 Running the Tests

To run all tests:
```
pytest
```

To run tests that need review:
```
pytest -v --tb=line --language=en -m need_review  
```

<br>

### 💡 Project Highlights

- Page Object Model: Clean separation between test logic and page structure for 
maintainability
- Reusable Components: Common methods for interacting with elements and handling waits
- Scalable Design: Easy to add new tests or extend existing functionality
- pytest Fixtures: Efficient setup and teardown for test environments

<br>

### 🙌 Acknowledgments

This project was created as part of the "Test Automation with Selenium and 
Python" course. Thanks to the instructor for providing clear, practical lessons 
on building effective UI automation frameworks.
