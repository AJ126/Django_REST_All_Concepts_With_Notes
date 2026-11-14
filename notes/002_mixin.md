# Django REST Framework (DRF) – Mixins

## 1. What is a Mixin?

A **Mixin** is a reusable class that provides specific functionality to another class through inheritance.

We use mixins to avoid writing the same code repeatedly.

### Real-life example

Suppose we are developing a Customer Management System. We need to perform the following operations:

1. Display all customer records.
2. Retrieve a single customer record.
3. Create a new customer record.
4. Update an existing customer record.
5. Delete a customer record.

If we write the same logic repeatedly in different views, our code becomes lengthy and difficult to maintain.

Instead, we can use mixins to reuse common functionality.

### Important points about Mixins

- Mixins are a design pattern used to share reusable functionality between classes.
- They commonly work through inheritance.
- They help us avoid code duplication.
- A mixin is generally designed to be combined with another class rather than used independently.
- Mixins can be used with multiple inheritance in Python.
- A mixin can contain methods, class variables, and even instance variables when required.
- Mixins can also inherit from other classes.
- Languages such as Python and Ruby support multiple class inheritance. Languages such as Java and C# do not support traditional multiple class inheritance, but they provide other approaches, such as interfaces, to achieve similar reuse.

**Note:** A mixin is not a special or restricted version of multiple inheritance. It is a reusable class designed to add a particular capability to another class.

---

## 2. Built-in Mixins in Django REST Framework

Django REST Framework provides five commonly used built-in mixins.

These mixins provide reusable methods for performing CRUD operations.

| Mixin | HTTP Method | Purpose | Method |
|---|---|---|---|
| ListModelMixin | GET | Retrieve all records | `.list()` |
| RetrieveModelMixin | GET | Retrieve a single record | `.retrieve()` |
| CreateModelMixin | POST | Create a new record | `.create()` |
| UpdateModelMixin | PUT / PATCH | Update an existing record | `.update()` / `.partial_update()` |
| DestroyModelMixin | DELETE | Delete an existing record | `.destroy()` |

To use these mixins, we generally combine them with `GenericAPIView`.

## 3. GenericAPIView

`GenericAPIView` is a class provided by Django REST Framework.

It provides common functionality required when creating API views.

Some important features include:

- `queryset`: Defines which model records should be accessed.
- `serializer_class`: Defines which serializer should be used.
- Object lookup: Helps retrieve a particular object.
- Request handling support: Provides common functionality for working with API requests.

**Important:** Mixins provide methods for CRUD operations, while `GenericAPIView` provides common API functionality. We connect them by defining HTTP method handlers such as `get()`, `post()`, `put()`, and `delete()`.

### 3.1 ListModelMixin

`ListModelMixin` is used to retrieve all records from the database.

- HTTP method: GET
- Method provided by mixin: `.list()`

**Example:**

```python
from rest_framework import generics, mixins
from .models import Customer
from .serializers import CustomerSerializer

class CustomerListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
```

**Explanation:**

- `ListModelMixin` provides the `.list()` method.
- `GenericAPIView` provides common API functionality.
- `queryset` defines the records to retrieve.
- `serializer_class` defines how the records should be converted into JSON-compatible data.
- The `get()` method calls `.list()` to return all customer records.

### 3.2 RetrieveModelMixin

`RetrieveModelMixin` is used to retrieve a single record using its primary key.

- HTTP method: GET
- Method provided by mixin: `.retrieve()`

**Example:**

```python
from rest_framework import generics, mixins
from .models import Customer
from .serializers import CustomerSerializer

class CustomerRetrieveView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
```

**Explanation:**

- `RetrieveModelMixin` provides the `.retrieve()` method.
- We pass `request`, `args`, and `kwargs` to the method.
- The primary key is generally passed through the URL.
- The mixin retrieves the matching record and returns its serialized data.

Example URL:

```text
http://127.0.0.1:8000/customer/1/
```

Here, `1` is the primary key of the customer record.

### 3.3 CreateModelMixin

`CreateModelMixin` is used to create a new record in the database.

- HTTP method: POST
- Method provided by mixin: `.create()`

**Example:**

```python
from rest_framework import generics, mixins
from .models import Customer
from .serializers import CustomerSerializer

class CustomerCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request)
```

**Explanation:**

- `CreateModelMixin` provides the `.create()` method.
- The `post()` method calls `.create()`.
- The mixin passes incoming request data to the serializer.
- The serializer validates the data and saves the new record if it is valid.

### 3.4 UpdateModelMixin

`UpdateModelMixin` is used to update an existing record.

It supports two types of updates:

1. PUT – Used for a complete update of a resource.
2. PATCH – Used for a partial update of a resource.

Methods provided by the mixin:

- `.update()` – Handles a regular update.
- `.partial_update()` – Handles a partial update.

**Example:**

```python
from rest_framework import generics, mixins
from .models import Customer
from .serializers import CustomerSerializer

class CustomerUpdateView(
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
```

**Explanation:**

- `UpdateModelMixin` provides both update methods.
- The `put()` method calls `.update()`.
- The `patch()` method calls `.partial_update()`.
- The record is identified using its primary key.

### 3.5 DestroyModelMixin

`DestroyModelMixin` is used to delete an existing record from the database.

- HTTP method: DELETE
- Method provided by mixin: `.destroy()`

**Example:**

```python
from rest_framework import generics, mixins
from .models import Customer
from .serializers import CustomerSerializer

class CustomerDeleteView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

**Explanation:**

- `DestroyModelMixin` provides the `.destroy()` method.
- The `delete()` method calls `.destroy()`.
- The record is identified using its primary key.
- The matching record is deleted from the database.

---

## 4. Advantages of Mixins

1. **Code Reusability:** We can reuse the same functionality in multiple views.
2. **Less Code Duplication:** We do not need to write the same CRUD logic repeatedly.
3. **Easy Maintenance:** Changes to shared functionality can be made in one place.
4. **Flexibility:** We can combine different mixins according to our requirements.
5. **Clean Code:** Our views become shorter and easier to understand.

---

## 5. Custom SerializerMixin

Apart from the built-in DRF mixins, we can also create our own custom mixins.

A custom mixin is useful when we want to reuse common functionality across multiple serializers or views.

### Example

Suppose we have multiple serializers, such as:

- CustomerSerializer
- ProductSerializer
- EmployeeSerializer

If all these serializers need the same functionality to convert a name into uppercase, we can write that functionality once in a custom mixin.

**Step 1: Create a custom mixin**

```python
class CommonSerializerMixin:

    def format_name(self, obj):
        return obj.name.upper()
```

**Step 2: Use the custom mixin in CustomerSerializer**

```python
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(
    CommonSerializerMixin,
    serializers.ModelSerializer
):

    display_name = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'

    def get_display_name(self, obj):
        return self.format_name(obj)
```

**Explanation:**

- `CommonSerializerMixin` contains reusable functionality.
- `format_name()` converts the customer's name into uppercase.
- `CustomerSerializer` inherits from both `CommonSerializerMixin` and `ModelSerializer`.
- `SerializerMethodField()` allows us to add a custom field to the serializer output.
- `get_display_name()` calls the reusable `format_name()` method.

We can also reuse `CommonSerializerMixin` in other serializers.

### Difference between Serializer, ModelSerializer, Mixin, and SerializerMixin

| Name | Description |
|---|---|
| Serializer | Used to convert complex data into Python-compatible data and validate incoming data. |
| ModelSerializer | A serializer that automatically provides fields and common functionality based on a Django model. |
| Mixin | A reusable class that provides specific functionality to another class. |
| SerializerMixin | A custom mixin created by us to share common serializer functionality. It is not a built-in DRF class. |

---

## 6. Error Handling in Django

When we develop APIs, we should handle errors properly.

We should not expose unnecessary internal Django errors or technical details to partner applications.

For example, suppose a partner application requests a customer record that does not exist.

Instead of returning an uncontrolled server error, we should return an appropriate error response.

### Example using a Django class-based view and custom SerializeMixin

```python
import json

from django.http import HttpResponse
from django.views import View

class ShowInfoTestListWithMixin(SerializeMixin, View):

    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        try:
            data = testInfo.objects.get(id=pk)

        except testInfo.DoesNotExist:

            json_data = json.dumps({
                'msg': 'Specified Record Not Found'
            })

            return HttpResponse(
                json_data,
                content_type='application/json',
                status=404
            )

        else:

            json_data = self.serialize_data(data)

            return HttpResponse(
                json_data,
                content_type='application/json'
            )
```

**Explanation:**

- `SerializeMixin` is a custom mixin that provides the `serialize_data()` method.
- `testInfo.objects.get(id=pk)` retrieves the requested record.
- If the record does not exist, Django raises `testInfo.DoesNotExist`.
- The `except` block handles the error.
- We return a meaningful error message with HTTP status code `404`.
- If the record exists, the `else` block serializes the data and returns it.

**Note:** This example uses a normal Django class-based view (`View`) and a custom mixin. It is not an example of a built-in DRF mixin.

### Setting HTTP status codes in HttpResponse

We can explicitly set an HTTP status code using the `status` parameter.

Example:

```python
return HttpResponse(
    json_data,
    content_type='application/json',
    status=403
)
```

Common HTTP status codes:

| Status Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## 7. Django dumpdata Command

The `dumpdata` command is used to export data from the database into a fixture format.

By default, Django exports data in JSON format.

### 7.1 Display all records in the terminal

```bash
python manage.py dumpdata app_002_mixins.testInfo
```

**Explanation:**

- `dumpdata` is the Django management command.
- `app_002_mixins` is the application name.
- `testInfo` is the model name.
- The command displays the model's records in JSON format.

### 7.2 Display formatted JSON data

```bash
python manage.py dumpdata app_002_mixins.testInfo --indent 4
```

The `--indent 4` option formats the JSON output with four spaces of indentation, making it easier to read.

### 7.3 Export JSON data into a file

```bash
python manage.py dumpdata app_002_mixins.testInfo --indent 4 > emp.json
```

**Explanation:**

- `>` is a command-line output redirection operator.
- It redirects the command output into a file.
- `emp.json` is the file where the exported data is stored.

### 7.4 Explicitly specify JSON format

```bash
python manage.py dumpdata app_002_mixins.testInfo --format json --indent 4 > emp.json
```

Here, `--format json` explicitly specifies JSON as the output format.

### 7.5 Export data in XML format

```bash
python manage.py dumpdata app_002_mixins.testInfo --format xml --indent 4
```

This command displays the exported data in XML format.

To save the XML output into a file:

```bash
python manage.py dumpdata app_002_mixins.testInfo --format xml --indent 4 > emp.xml
```

**Note:** The `dumpdata` command exports data; it does not delete or modify the original database records.

---

## 8. Disable CSRF Verification in Django

CSRF stands for **Cross-Site Request Forgery**.

Django provides CSRF protection to help prevent unauthorized requests made through a user's authenticated browser session.

Sometimes, during API testing, we may need to disable CSRF verification for a particular view.

There are different ways to disable CSRF verification.

**Important:** Disabling CSRF protection should only be done when necessary. Do not disable it casually in production.

### 8.1 Disable CSRF using @csrf_exempt decorator

We can use the `@csrf_exempt` decorator to disable CSRF verification for a particular function-based view.

**Example:**

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    # View logic
    pass
```

### 8.2 Disable CSRF for a class-based view

For class-based views, we can use `method_decorator`.

**Example:**

```python
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(View):

    def get(self, request, *args, **kwargs):
        # GET logic
        pass

    def post(self, request, *args, **kwargs):
        # POST logic
        pass
```

**Explanation:**

- `method_decorator` allows us to apply a function-based decorator to a class-based view method.
- `name='dispatch'` applies the decorator to the class's `dispatch()` method.
- `@csrf_exempt` disables CSRF verification for requests handled by that view.

### 8.3 Disable CSRF through settings.py

We can also disable CSRF middleware at the project level by commenting out the following middleware in `settings.py`:

```python
'django.middleware.csrf.CsrfViewMiddleware',
```

**Important warning:**

This disables Django's CSRF middleware project-wide. It is strongly discouraged for production applications, especially applications using session-based authentication.

In Django REST Framework, CSRF requirements also depend on the authentication method. For example, `SessionAuthentication` enforces CSRF validation for authenticated requests.

---

## 9. Access POST Request Data in Django

When a partner application sends data to our API using the POST method, we need to access the data inside the `post()` method.

In normal Django views, we can access the raw request body using:

```python
request.body
```

The `request.body` property returns the raw request body as bytes.

If the incoming data is JSON, we need to decode it and convert it into a Python object.

### Example using normal Django

```python
import json

from django.http import JsonResponse
from django.views import View

class CustomerCreateView(View):

    def post(self, request, *args, **kwargs):

        try:
            data = json.loads(request.body.decode('utf-8'))

        except (json.JSONDecodeError, UnicodeDecodeError):

            return JsonResponse(
                {'error': 'Invalid JSON data'},
                status=400
            )

        # Access the received data
        name = data.get('name')
        address = data.get('address')

        return JsonResponse({
            'message': 'Data received successfully',
            'name': name,
            'address': address
        })
```

**Explanation:**

1. `request.body` gets the raw request body in bytes.
2. `.decode('utf-8')` converts the bytes into a string.
3. `json.loads()` converts the JSON string into a Python dictionary.
4. We can access individual values using `data.get()`.
5. `json.JSONDecodeError` handles invalid JSON data.
6. `UnicodeDecodeError` handles data that cannot be decoded as UTF-8.

### Important: request.body vs request.data

In normal Django views, we commonly use `request.body` to access raw request data.

In Django REST Framework, we generally use:

```python
request.data
```

DRF automatically parses incoming request data based on the request's content type and configured parsers.

**Example using DRF:**

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class CustomerCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        name = data.get('name')
        address = data.get('address')

        return Response({
            'message': 'Data received successfully',
            'name': name,
            'address': address
        })
```

**Remember:**

| Normal Django | Django REST Framework |
|---|---|
| `request.body` | `request.data` |
| Raw request body in bytes | Parsed request data |
| We may need to decode and parse JSON manually | DRF parses supported request formats automatically |

