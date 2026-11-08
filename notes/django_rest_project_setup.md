# How to Install and Set Up a Django REST Framework Project

## 1. Install Django

Django is a Python web framework used to build web applications and backend systems.

**Command:**
```bash
pip install django
```

**Check Django installation:**
```bash
python -m django --version
```

---

## 2. Install Django REST Framework (DRF)

Django REST Framework (DRF) is a toolkit built on top of Django. It helps us create REST APIs easily.

For example, we can create APIs to:
- Add customer details.
- Get customer details.
- Update customer details.
- Delete customer details.

**Command:**
```bash
pip install djangorestframework
```

---

## 3. Install Additional Useful Packages

### 3.1 Django Filter

`django-filter` allows us to filter API data based on specific fields.

**Command:**
```bash
pip install -U django-filter
```

**Real-life example:**

Suppose we have 100 customer records and want to display only customers from Latur.

We can use Django Filter to filter customers based on their city.

### 3.2 Django CORS Headers

`django-cors-headers` allows us to configure Cross-Origin Resource Sharing (CORS).

It is important when connecting an Angular frontend with a Django REST backend.

**Command:**
```bash
pip install django-cors-headers
```

**Real-life example:**

Suppose your frontend and backend are running on different origins:

- Angular frontend: `http://localhost:4200`
- Django backend: `http://127.0.0.1:8000`

These are different origins. Browsers restrict requests between different origins unless the backend allows them through CORS configuration.

This package helps us configure which frontend origins are allowed to access our backend APIs.

---

## 4. Create a Django Project

After installing the required packages, create a new Django project.

**Command:**
```bash
django-admin startproject django_rest_all_concepts
```

**Alternative command:**

If `django-admin` is blocked or not recognized, use:

```bash
python -m django startproject django_rest_all_concepts
```

**Project structure:**

```text
django_rest_all_concepts/
│
├── manage.py
│
└── django_rest_all_concepts/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 5. Configure Installed Applications

After creating the project, open the `settings.py` file.

Add the following packages to `INSTALLED_APPS`.

**File: `settings.py`**

```python
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django REST Framework
    'rest_framework',

    # Third-party apps
    'django_filters',
    'corsheaders',
]
```

**Explanation:**

- `rest_framework`: Enables Django REST Framework functionality.
- `django_filters`: Enables filtering functionality in APIs.
- `corsheaders`: Provides CORS configuration for frontend-backend communication.

**Important:** Adding `corsheaders` to `INSTALLED_APPS` is not enough. You must also configure its middleware and allowed frontend origins in `settings.py`.

Add the CORS middleware near the top of `MIDDLEWARE`, before `CommonMiddleware`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # CORS middleware
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Allow your Angular frontend:

```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200',
]
```

---

## 6. Summary of Installed Packages

| Package | Purpose |
|---|---|
| Django | Build backend web applications |
| djangorestframework | Create REST APIs |
| django-filter | Filter API data |
| django-cors-headers | Configure frontend-backend CORS |

**Installation commands together:**

```bash
pip install django
pip install djangorestframework
pip install -U django-filter
pip install django-cors-headers
```

**Note:** Run these commands after activating your project's virtual environment so the packages are installed inside that environment.