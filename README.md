# My Utility Hub

Welcome to **My Utility Hub** – a Django-based project that combines three useful utilities into one sleek, responsive application. With a beautifully designed home page, users can easily navigate between the Basic Calculator, BMI Calculator, and Unit Converter.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Basic Calculator:** Perform arithmetic operations (addition, subtraction, multiplication, division).
- **BMI Calculator:** Calculate your Body Mass Index (BMI) using your weight and height.
- **Unit Converter:** Convert between kilometers and miles.
- **Responsive Home Page:** A unified dashboard where users can click on any tool to access its functionality.
- **Clean, Modern Design:** Styled using CSS for an enhanced user experience.

---

## Installation

### Prerequisites
- Python 3.x
- Django 5.1.5

### Steps

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Shaiful967532/Django_Edge_Project.git
    cd my-utility-hub
    ```

2. **Set Up a Virtual Environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install Django:**
    ```bash
    pip install django
    ```

4. **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

6. **Open Your Browser:**
   Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the home page and select any utility.

---

## Usage

- **Home Page:**  
  The home page displays cards for each utility (Basic Calculator, BMI Calculator, Unit Converter). Click on any card to navigate to the respective tool.

- **Basic Calculator:**  
  Perform basic arithmetic operations using the provided form.

- **BMI Calculator:**  
  Enter your weight and height to calculate your BMI.

- **Unit Converter:**  
  Convert values between kilometers and miles with a few clicks.

---

## Project Structure

my-utility-hub/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── templates/
│       └── myapp/
│           └── home.html
├── unit_converter/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── templates/
│       └── unit_converter/
│           └── index.html
├── bmi_calculator/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── templates/
│       └── bmi_calculator/
│           └── index.html
├── basic_calculator/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── templates/
│       └── basic_calculator/
│           └── index.html
└── static/
    └── css/
        └── styles.css


---

## Screenshots

![image](https://github.com/user-attachments/assets/9c20733a-df92-42a7-b63f-1e4295627d9b)

![image](https://github.com/user-attachments/assets/b59d54f9-3dbf-4267-8aca-9434b3db54b4)

![image](https://github.com/user-attachments/assets/ed85a872-1c2d-4bb0-8cd5-ad29255210e7)

![image](https://github.com/user-attachments/assets/0dccce60-cf0c-4f16-b300-a5b044c2f02a)


---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add some feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature
    ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy using **My Utility Hub**! If you have any questions or run into issues, feel free to open an issue on GitHub.
