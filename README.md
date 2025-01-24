# Django Application with Custom User Model and REST APIs

## Overview
This project implements a Django-based web application featuring:
- A custom user model (`CustomUser`) with fields for age and phone number.
- RESTful APIs for user registration, login, profile viewing, and a status check endpoint.
- Frontend templates for registration, login, and profile pages.

The project adheres to REST principles, using JSON responses with proper HTTP status codes. The application is built using vanilla Django (without Django REST Framework).

---

## Features
1. **Custom User Model**:
   - Extends Django's `AbstractUser`.
   - Includes additional fields: `age` and `phone_number`.

2. **REST APIs**:
   - **Signup**: Allows users to register by providing their details.
   - **Login**: Authenticates users using their username and password.
   - **Profile**: Displays the logged-in user's information.
   - **Status**: A simple health check endpoint that returns a 200 OK response with a message.

3. **Frontend Pages**:
   - `register.html`: User registration form.
   - `login.html`: User login form.
   - `profile.html`: Displays user details after login.

4. **Django App Structure**:
   - The application is modular and uses Django's app concept for scalability and maintainability.

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- Django 4.x

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## API Endpoints

### 1. Signup
- **URL**: `/api/signup/`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "password": "password123",
    "age": 25,
    "phone_number": "1234567890"
  }
  ```
- **Response**:
  - **201 Created**: User created successfully.
  - **400 Bad Request**: Validation errors.

### 2. Login
- **URL**: `/api/signin/`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "password": "password123"
  }
  ```
- **Response**:
  - **200 OK**: Login successful.
  - **401 Unauthorized**: Invalid credentials.

### 3. Profile
- **URL**: `/api/profile/`
- **Method**: GET
- **Headers**: Authentication required.
- **Response**:
  ```json
  {
    "username": "testuser",
    "email": "test@example.com",
    "age": 25,
    "phone_number": "1234567890"
  }
  ```

### 4. Status
- **URL**: `/api/status/`
- **Method**: GET
- **Response**:
  ```json
  {
    "message": "alive"
  }
  ```

---

## File Structure
```
project-root/
├── application/
│   ├── migrations/        # Migration files
│   ├── templates/         # HTML templates
│   │   ├── application/
│   │       ├── register.html
│   │       ├── login.html
│   │       └── profile.html
│   ├── admin.py           # Admin site configuration
│   ├── models.py          # CustomUser model
│   ├── views.py           # API and page views
│   ├── forms.py           # Forms for registration and login
├── manage.py              # Django project manager
├── db.sqlite3             # SQLite database file (after migration)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Development and Contribution
1. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```

2. Commit your changes:
   ```bash
   git add .
   git commit -m "Add feature description"
   ```

3. Push to the repository:
   ```bash
   git push origin feature-name
   ```

4. Create a pull request on GitHub.

---

## License
This project is licensed under the MIT License.
