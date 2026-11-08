# Introduction to API, REST API, JSON and Django REST Framework (DRF)

## 1. What is an API?

API stands for **Application Programming Interface**.

An API allows two different software applications to communicate and exchange information with each other.

**In simple words:**

An API is a communication interface between software applications.

**Main objective of an API:**

To allow different applications or software components to communicate, integrate and exchange information.

**Examples:**

- A Java application can communicate with a Python application using an API.
- A BookMyShow application communicates with a payment gateway to complete a movie ticket booking.
- An Angular frontend communicates with a Django backend to retrieve customer information.

**Important:** An API allows different applications to communicate without requiring them to know each other's internal implementation.

### Real-life example: Restaurant

Imagine you visit a restaurant to order food.

**How does the process work?**

1. You (customer) request food.
2. The waiter takes your request.
3. The waiter communicates with the kitchen.
4. The kitchen prepares the food.
5. The waiter delivers the food to you.

**Restaurant vs Software Application**

| Restaurant | Software Application |
|---|---|
| Customer | Client application |
| Waiter | API |
| Kitchen | Backend / Server |
| Food order | Request |
| Prepared food | Response / Data |

**Important:** Just as a waiter acts as an interface between a customer and the kitchen, an API acts as a communication interface between applications.

### Example: Angular + Django

Imagine you have two applications:

- Angular frontend
- Django backend

Angular wants to retrieve customer records from Django.

Instead of directly accessing Django's database, Angular sends an HTTP request to a Django API.

**How does it work?**

1. Angular sends a request to the Django API.
2. Django receives the request.
3. Django retrieves customer information from the database.
4. Django sends the data back to Angular.
5. Angular displays the customer information.

**Important:** The frontend does not need direct database access. It communicates with the backend through APIs.

---

## 2. What is a REST API?

REST stands for **Representational State Transfer**.

REST is an architectural style that defines guidelines for designing web APIs.

**In simple words:**

REST APIs allow applications to communicate using standard HTTP methods and resource-based URLs.

### Common HTTP Methods Used in REST APIs

| HTTP Method | Purpose | Example |
|---|---|---|
| GET | Retrieve data | Get all customers |
| POST | Create new data | Add a customer |
| PUT | Update complete data | Update customer details |
| PATCH | Update partial data | Update customer address |
| DELETE | Delete data | Delete a customer |

**Example API endpoints:**

```text
GET     /api/customers/
POST    /api/customers/
GET     /api/customers/1/
PUT     /api/customers/1/
PATCH   /api/customers/1/
DELETE  /api/customers/1/
```

These endpoints represent operations on customer resources.

---

## 3. What is JSON?

JSON stands for **JavaScript Object Notation**.

JSON is a lightweight data format used to exchange information between applications.

It is easy for humans to read and easy for programming languages to process.

### Why do we use JSON?

Different technologies can understand JSON, including:

- Angular
- React
- Python
- Java
- Android applications

**Example:**

Suppose Django sends customer information to Angular.

Django sends JSON:

```json
{
    "id": 1,
    "name": "Shiv",
    "address": "Latur",
    "mobile": "9876543210"
}
```

Angular receives this JSON data and displays the customer information in a table.

**Important:**

- JSON is a data format, not a programming language.
- JSON is commonly used to exchange data between frontend and backend applications.

---

## 4. What Happens When Angular Calls a Django API?

Imagine Angular wants to retrieve all customer records from Django.

**API URL:**

```text
GET http://127.0.0.1:8000/api/customers/
```

### Step-by-step process

**Step 1: Angular sends an HTTP request**

Angular sends a GET request to the Django API.

```typescript
this.http.get('http://127.0.0.1:8000/api/customers/')
```

**Step 2: Django receives the request**

Django checks the URL configuration (`urls.py`) and identifies the corresponding view.

**Step 3: The view processes the request**

The Django view communicates with the database using Django ORM.

```python
customers = Customer.objects.all()
```

This retrieves all customer records from the database.

**Step 4: Data is converted into JSON-compatible data**

Django ORM returns Python model objects.

These objects need to be converted into a format suitable for API responses.

This is where DRF serializers become important.

**Step 5: Django sends an HTTP response**

Django returns the customer data, usually in JSON format.

**Step 6: Angular receives the response**

Angular receives the JSON data and displays customer information in a table.

### Complete communication flow

```text
Angular Frontend
       |
       | HTTP GET Request
       v
Django URL Configuration
       |
       v
Django View / DRF APIView
       |
       v
Django ORM
       |
       v
Database
       |
       v
Django ORM returns data
       |
       v
DRF Serializer
       |
       v
JSON Response
       |
       v
Angular Frontend
       |
       v
Display Customer Records
```

---

## 5. What is Django REST Framework (DRF)?

Django REST Framework (DRF) is a powerful third-party Python package built on top of Django for developing Web APIs.

Django already provides:
- Models
- Views
- URL routing
- Database connectivity
- Authentication

However, building professional APIs requires additional functionality, such as:

- Data serialization.
- Data validation.
- API request and response handling.
- Authentication.
- Permissions.
- Pagination.
- Filtering.
- API documentation support.

DRF provides ready-made tools for these tasks.

### Why do we use DRF?

Imagine you are building a Customer Management System.

You need to:
- Add customer details.
- Retrieve customer details.
- Update customer information.
- Delete customer records.
- Authenticate users.
- Restrict access to APIs.
- Validate customer information.
- Implement pagination and filtering.

You could build these features manually using normal Django views, but DRF provides reusable functionality that makes API development easier and more maintainable.

---

## 6. Django vs Django REST Framework

| Django | Django REST Framework |
|---|---|
| General-purpose web framework | Toolkit for building Web APIs |
| Uses Django views | Provides APIView, ViewSets, etc. |
| Can return HTML responses | Provides API Response objects |
| Uses Django Forms for form validation | Provides serializers for API validation |
| Has built-in authentication | Adds API authentication integrations |
| Provides Django ORM | Uses the existing Django ORM |

**Important:** Django REST Framework does not replace Django. It extends Django with additional tools for API development.

---

## 7. Difference Between a Normal Django View and a DRF View

Both normal Django views and DRF views can be used to create APIs.

However, DRF provides additional API-related functionality.

### 7.1 Normal Django View

Django provides `JsonResponse` to return JSON data.

**Example:**

```python
from django.http import JsonResponse

def customer_list(request):
    customers = [
        {"id": 1, "name": "Shiv"},
        {"id": 2, "name": "Parvati"}
    ]

    return JsonResponse(customers, safe=False)
```

**Explanation:**

- `JsonResponse` is provided by Django.
- It converts Python data into a JSON HTTP response.
- `safe=False` allows us to return a list instead of a dictionary.
- By default, `JsonResponse` expects a dictionary.

### 7.2 Django REST Framework View

DRF provides its own `Response` class and API view decorators.

**Example:**

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def customer_list(request):

    customers = [
        {"id": 1, "name": "Shiv"},
        {"id": 2, "name": "Parvati"}
    ]

    return Response(customers)
```

**Explanation:**

- `@api_view(['GET'])` converts a normal Django function into a DRF function-based API view.
- It allows only GET requests.
- `Response` is provided by DRF.
- The `Response` class supports content negotiation, meaning DRF can select an appropriate response format based on the request and available renderers.

### Why Prefer DRF?

Imagine you are building a real customer application with:

- 10 API endpoints.
- Authentication.
- Permissions.
- Data validation.
- Pagination.
- Filtering.
- File uploads.

You could implement these features manually using normal Django views, but DRF provides reusable functionality to handle them more easily.

**Important:** Normal Django views are useful for simple APIs, but DRF is particularly helpful when building larger and more complex REST APIs.

---

## 8. What is an API Endpoint?

An API endpoint is a specific URL through which an application accesses a particular API resource or operation.

**Example:**

```text
http://127.0.0.1:8000/api/customers/
```

Here:

| Part | Meaning |
|---|---|
| `http://` | Communication protocol |
| `127.0.0.1` | Localhost / IP address |
| `8000` | Django server port |
| `/api/customers/` | API endpoint path |

### More Examples

```text
GET     http://127.0.0.1:8000/api/customers/
POST    http://127.0.0.1:8000/api/customers/
GET     http://127.0.0.1:8000/api/customers/1/
PUT     http://127.0.0.1:8000/api/customers/1/
DELETE  http://127.0.0.1:8000/api/customers/1/
```

**Real-life example:**

Suppose your Customer Management System has 100 customers.

- `/api/customers/` accesses the customer collection.
- `/api/customers/1/` accesses the customer whose ID is 1.

The HTTP method determines what operation is performed on the endpoint.

---

## Important Points to Remember

1. **API:** Allows different software applications to communicate.
2. **REST:** An architectural style for designing web APIs.
3. **JSON:** A data format used to exchange information.
4. **Django:** A Python web framework.
5. **DRF:** A toolkit built on Django for developing Web APIs.
6. **Serializer:** Converts complex Django data into Python data suitable for rendering and validates incoming data.
7. **API Endpoint:** A URL used to access a particular API resource or operation.
8. **HTTP Methods:** GET, POST, PUT, PATCH and DELETE define common API operations.