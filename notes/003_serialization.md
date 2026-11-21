# Serialization and Deserialization in Django REST Framework (DRF)

## 1. What is Serialization?

The process of converting an object from one form into another form is called **Serialization**.

### Example: Converting a Python dictionary into JSON

Python provides the `json` module to convert Python objects into JSON format.

```python
import json

data = {
    'name': 'Shiv',
    'info': 'Har Har Mahadev',
    'phone': '8888120866'
}

json_data = json.dumps(data)

print(json_data)
```

**Output:**

```json
{"name": "Shiv", "info": "Har Har Mahadev", "phone": "8888120866"}
```

Django also provides an inbuilt `serializers` module to perform serialization. It contains a `serialize()` function.

However, Django REST Framework provides its own Serializer classes, which make serialization, deserialization, and validation easier.

## 2. DRF Serializers

DRF Serializers are responsible for the following activities:

1. Serialization
2. Deserialization
3. Validation

DRF Serializers work similarly to Django Forms and ModelForm classes.

### Main responsibilities

**1. Serialization**

The process of converting complex objects, such as Django Model objects and QuerySets, into Python native data types is called Serialization.

**2. Deserialization**

The process of converting incoming data into Python native data types and then validating and converting it into a form suitable for creating or updating model objects is called Deserialization.

**3. Validation**

Before saving incoming data into the database, serializers validate the data according to the specified rules.

### Why do we need Serialization?

Suppose we have a Django application containing customer details in a database.

If another application sends a GET request, our Django application must:

1. Retrieve data from the database.
2. Convert Model objects or QuerySets into Python native data types.
3. Convert Python native data types into JSON.
4. Send the JSON response to the partner application.

Serialization makes this process possible.

## 3. Serialization Process

Let's understand how to convert Django Model objects into JSON using DRF.

### Step 1: Convert Model objects into Python native data types

```python
info = detail.objects.all()

serializer = detailSerializer(info, many=True)

print(serializer.data)
```

**Explanation:**

- `detail.objects.all()` retrieves all records from the database.
- `many=True` tells the serializer that we are passing multiple objects.
- `serializer.data` returns the serialized data in Python native data types.

**Important:** When serializing a single model object, we don't need `many=True`.

```python
info = detail.objects.get(id=1)

serializer = detailSerializer(info)

print(serializer.data)
```

### Step 2: Convert Python native data types into JSON

DRF provides `JSONRenderer` to convert Python native data types into JSON.

```python
from rest_framework.renderers import JSONRenderer

json_data = JSONRenderer().render(serializer.data)

print(json_data)
```

### Serialization flow

```text
Django Model Objects / QuerySet
              |
              v
       DRF Serializer
              |
              v
   Python Native Data Types
              |
              v
        JSONRenderer
              |
              v
          JSON Data
```

**Remember:**

```text
Python Complex Data Types (Model / QuerySet)
                    |
                    v
             DRF Serializer
                    |
                    v
       Python Native Data Types
                    |
                    v
              JSONRenderer
                    |
                    v
                JSON Data
```

## 4. What is Deserialization?

The process of converting incoming data into Python native data types and then converting validated data into database-supported objects is called Deserialization.

When a partner application sends a POST or PUT request containing JSON data, our Django application must:

1. Receive JSON data.
2. Convert the JSON data into Python native data types.
3. Validate the incoming data.
4. Convert the validated data into a Model object.
5. Save the Model object into the database.

For this process, we use Deserialization.

### Deserialization example

```python
serializer = detailSerializer(data=info)

if serializer.is_valid():
    print(serializer.validated_data)
```

**Explanation:**

- `data=info` passes incoming data to the serializer.
- `is_valid()` checks whether the incoming data satisfies the serializer's validation rules.
- `validated_data` contains the validated Python native data.

### Deserialization flow

```text
        JSON Data
             |
             v
       JSONParser
             |
             v
   Python Native Data Types
             |
             v
       DRF Serializer
             |
             v
          Validation
             |
             v
       validated_data
             |
             v
      Model Object
             |
             v
          Database
```

**Important:** When using DRF API views, `request.data` normally provides the parsed request data. You don't need to manually use `JSONParser` for ordinary DRF requests.

## 5. Creating Records Using Serializer

To perform a CREATE operation using a serializer, we have to override the `create()` method in the serializer class.

### Example

```python
from rest_framework import serializers
from app_003_serialization.models import detail


class detailSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    info = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return detail.objects.create(**validated_data)
```

### Explanation

- `create()` is called when we save new data using `serializer.save()`.
- `validated_data` contains the validated incoming data.
- `detail.objects.create(**validated_data)` creates and saves a new database record.
- `**validated_data` unpacks the dictionary into keyword arguments.

### How to use it?

```python
data = {
    'name': 'Shiv',
    'info': 'Har Har Mahadev',
    'phone': '8888120866'
}

serializer = detailSerializer(data=data)

if serializer.is_valid():
    serializer.save()
    print('Record created successfully')
else:
    print(serializer.errors)
```

**Important:** Calling `serializer.is_valid()` does not save the record. We must call `serializer.save()` after successful validation.

## 6. Updating Records Using Serializer

To handle PUT requests and update existing records, we have to override the `update()` method in the serializer class.

### Example

```python
def update(self, instance, validated_data):

    instance.name = validated_data.get('name', instance.name)
    instance.info = validated_data.get('info', instance.info)
    instance.phone = validated_data.get('phone', instance.phone)

    instance.save()

    return instance
```

### Explanation

- `instance` represents the existing database object.
- `validated_data` contains the validated incoming data.
- `validated_data.get('name', instance.name)` uses the new name if provided; otherwise, it keeps the existing name.
- `instance.save()` saves the updated record.
- `return instance` returns the updated object.

### Complete Serializer Example

```python
from rest_framework import serializers
from app_003_serialization.models import detail


class detailSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    info = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return detail.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.info = validated_data.get('info', instance.info)
        instance.phone = validated_data.get('phone', instance.phone)

        instance.save()

        return instance
```

### How to update an existing record?

```python
info = detail.objects.get(id=1)

data = {
    'name': 'Parvati',
    'info': 'Har Har Mahadev',
    'phone': '8888120866'
}

serializer = detailSerializer(instance=info, data=data)

if serializer.is_valid():
    serializer.save()
    print('Record updated successfully')
else:
    print(serializer.errors)
```

**Important:**

- `serializer.save()` calls `create()` when no existing instance is provided.
- `serializer.save()` calls `update()` when an existing instance is provided.
- PUT requests generally require all required fields.
- For PATCH requests, use `partial=True` to allow updating only selected fields.

```python
serializer = detailSerializer(
    instance=info,
    data=data,
    partial=True
)
```

## 7. Validations Using Serializers

Validation means checking whether incoming data satisfies the required conditions before saving it into the database.

DRF supports three common ways to perform validation:

1. Field-Level Validation
2. Object-Level Validation
3. Validation using Validators

## 7.1 Field-Level Validation

If we want to validate an individual field, we should use Field-Level Validation.

### Syntax

```python
def validate_fieldname(self, value):
    # Validation logic
    return value
```

**Example: Phone Number Validation**

```python
from rest_framework import serializers


class detailSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    info = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=15)

    def validate_phone(self, value):

        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError(
                'Phone number must contain exactly 10 digits.'
            )

        return value
```

### Explanation

- `validate_phone()` is automatically called when DRF validates the `phone` field.
- `value` contains the incoming phone number.
- `isdigit()` checks whether all characters are digits.
- `len(value) != 10` checks whether the phone number contains exactly 10 digits.
- `serializers.ValidationError()` raises a validation error if the condition fails.
- `return value` returns the validated value.

**Remember:** The method name must follow this format:

```text
validate_fieldname()
```

For example:

```python
validate_name()
validate_phone()
validate_email()
validate_address()
```

## 7.2 Object-Level Validation

If we want to perform validation on multiple fields simultaneously, we should use Object-Level Validation.

### Syntax

```python
def validate(self, data):
    # Validation logic
    return data
```

**Example:**

Suppose we have a condition:

- If `info` is `Har Har Mahadev`, the phone number must be `8888120866`.

```python
from rest_framework import serializers


class detailSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    info = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=15)

    def validate(self, data):

        info = data.get('info', '')
        phone = data.get('phone', '')

        if info.lower() == 'har har mahadev':

            if phone != '8888120866':
                raise serializers.ValidationError(
                    'Phone number should be 8888120866 '
                    'for info Har Har Mahadev.'
                )

        return data
```

### Explanation

- `validate()` is automatically called after individual field validations.
- `data` contains the validated field values.
- `data.get('info', '')` retrieves the `info` value.
- `data.get('phone', '')` retrieves the `phone` value.
- We can compare multiple fields and apply conditions.
- `return data` returns the validated data.

### When should we use Object-Level Validation?

Use Object-Level Validation when the validation depends on multiple fields.

Real-life examples:

1. Password and Confirm Password must be the same.
2. Account Number and Re-enter Account Number must be the same.
3. Start Date must be earlier than End Date.
4. If a particular account type is selected, additional information must be provided.
5. If `info` contains `Har Har Mahadev`, the phone number must match a particular value.

## 7.3 Validation Using Validators

DRF also allows us to create separate validation functions and attach them to serializer fields using the `validators` argument.

This is useful when we want to reuse the same validation logic in multiple serializers or fields.

### Example

```python
from rest_framework import serializers


def validate_name(value):

    if value.lower() == 'shiv':
        raise serializers.ValidationError(
            'Name should not be Shiv.'
        )

    return value


class detailSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(
        max_length=100,
        validators=[validate_name]
    )

    info = serializers.CharField(max_length=100)

    phone = serializers.CharField(max_length=15)
```

### Explanation

- `validate_name()` is a separate validation function.
- `value` contains the incoming name.
- If the name is `Shiv`, a validation error is raised.
- `validators=[validate_name]` attaches the validation function to the `name` field.
- `read_only=True` means the `id` field is included in serialized output but is not accepted as input for normal updates or creation.

**Important:** A validator function receives the field value directly. It does not receive `self` or the complete serializer data.

### Difference Between Three Validation Methods

| Validation Type | Purpose | Method / Syntax |
|---|---|---|
| Field-Level | Validate one field | `validate_fieldname(self, value)` |
| Object-Level | Validate multiple fields together | `validate(self, data)` |
| Validators | Attach reusable validation functions to fields | `validators=[validate_function]` |

## 8. Important Serializer Methods and Attributes

| Method / Attribute | Purpose |
|---|---|
| `serializer.data` | Returns serialized representation of the object |
| `serializer.is_valid()` | Checks whether incoming data is valid |
| `serializer.validated_data` | Returns validated input data |
| `serializer.errors` | Returns validation errors |
| `serializer.save()` | Creates or updates an object |
| `create()` | Creates a new object |
| `update()` | Updates an existing object |
| `validate_fieldname()` | Performs field-level validation |
| `validate()` | Performs object-level validation |

### Useful validation option

Instead of manually checking `serializer.errors`, we can use:

```python
serializer.is_valid(raise_exception=True)
```

If validation fails, DRF automatically raises a `ValidationError`, which API views can handle and return as an appropriate HTTP 400 response.

## 9. Complete Serialization and Deserialization Summary

### GET Request – Serialization

When another application requests existing database records:

```text
Partner Application
        |
        | GET Request
        v
Django REST Framework
        |
        v
Retrieve Model / QuerySet
        |
        v
DRF Serializer
        |
        v
Python Native Data Types
        |
        v
JSON Response
        |
        v
Partner Application
```

### POST / PUT Request – Deserialization

When another application sends data to create or update a record:

```text
Partner Application
        |
        | POST / PUT Request
        v
JSON Request Data
        |
        v
DRF Parser
        |
        v
Python Native Data Types
        |
        v
DRF Serializer
        |
        v
Validation
        |
        v
validated_data
        |
        v
create() / update()
        |
        v
Database
```

## 10. Final Summary

- Serialization converts complex objects such as Model objects and QuerySets into Python native data types.
- `JSONRenderer` converts Python native data types into JSON.
- Deserialization processes incoming data and converts validated data into objects suitable for database operations.
- `create()` is used to create new records.
- `update()` is used to update existing records.
- `serializer.save()` calls either `create()` or `update()` depending on whether an existing instance is provided.
- Field-Level Validation validates individual fields.
- Object-Level Validation validates multiple fields together.
- Validators allow us to attach reusable validation functions to fields.
- `serializer.is_valid()` checks whether incoming data is valid.
- `serializer.validated_data` contains the validated data.
- `serializer.errors` contains validation errors.

**Remember this simple concept:**

```text
GET Request  = Serialization
POST Request = Deserialization + Create
PUT Request  = Deserialization + Update
PATCH Request = Partial Deserialization + Update
```

