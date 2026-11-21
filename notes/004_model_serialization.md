# ModelSerializer in Django REST Framework (DRF)

## 1. What is ModelSerializer?

If the objects we want to serialize are Django Model objects, then it is highly recommended to use **ModelSerializer**.

`ModelSerializer` is a special type of Serializer class provided by Django REST Framework.

It works similarly to a regular `Serializer` class, but it provides some additional features.

### Differences Between Serializer and ModelSerializer

| Regular Serializer | ModelSerializer |
|---|---|
| We have to declare fields explicitly. | Fields are automatically generated based on the model. |
| We have to implement `create()` manually. | Provides a default implementation of `create()`. |
| We have to implement `update()` manually. | Provides a default implementation of `update()`. |
| Fields and their validations are defined manually. | Model fields and their default validations are automatically considered. |

**Important:** With ModelSerializer, we still have to specify which fields should be included using `fields` or `exclude` in the `Meta` class.

## 2. Basic Example of ModelSerializer

Suppose we have the following Django model:

```python
from django.db import models


class information(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
```

Now, let's create a ModelSerializer for this model.

```python
from rest_framework import serializers
from app_003_serialization.models import information


class informationSerializer(serializers.ModelSerializer):

    class Meta:
        model = information
        fields = '__all__'
```

### Explanation

**1. `serializers.ModelSerializer`**

We inherit from `ModelSerializer` instead of the regular `Serializer` class.

**2. `model = information`**

We specify the Django model for which we want to create the serializer.

**3. `fields = '__all__'`**

It tells DRF to include all fields from the specified model.

### Important Points

- We don't need to declare every model field manually.
- ModelSerializer automatically generates serializer fields based on the model.
- We don't need to implement `create()` and `update()` methods for normal model operations because ModelSerializer provides default implementations.
- We can still override these methods when we need custom behavior.

## 3. Defining Custom Field-Level Validation in ModelSerializer

If we want to define custom validation for a particular field, we can declare that field explicitly inside the ModelSerializer class.

This works similarly to Django ModelForm.

### Example

```python
from rest_framework import serializers
from app_003_serialization.models import information


# Validation function using validators
def validate_name(value):

    if value.lower() == 'shiv':
        raise serializers.ValidationError(
            'Name should not be Shiv.'
        )

    return value


class informationSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        max_length=100,
        validators=[validate_name]
    )

    class Meta:
        model = information
        fields = '__all__'
```

### Explanation

- `name` is explicitly declared inside the serializer.
- We can define custom validation using the `validators` argument.
- `validate_name()` is called automatically while validating the name field.
- If the name is `Shiv`, a validation error is raised.
- Other model fields are still generated automatically.

**Remember:** We only need to declare a field explicitly when we want to customize its behavior, such as adding custom validators, changing its options, or modifying its representation.

## 4. Three Ways to Specify Fields in ModelSerializer

There are three commonly used ways to specify fields in the ModelSerializer `Meta` class.

### 4.1 Include All Fields

If we want to include all fields from the model, we can use:

```python
class informationSerializer(serializers.ModelSerializer):

    class Meta:
        model = information
        fields = '__all__'
```

**Explanation:**

- `fields = '__all__'` includes all fields from the model.
- If we add a new field to the model, it will also be included automatically.

**When to use it?**

When we want to include all model fields in the serializer.

### 4.2 Include Only Some Fields

If we want to include only selected fields, we can specify their names.

```python
class informationSerializer(serializers.ModelSerializer):

    class Meta:
        model = information
        fields = ('name', 'description')
```

**Explanation:**

- Only `name` and `description` fields will be included.
- Other model fields will not be included in the serializer output.

We can also use a list:

```python
fields = ['name', 'description']
```

**When to use it?**

This approach is helpful when we want to include only a few fields from the model.

### 4.3 Exclude Some Fields

If we want to include most model fields but exclude a few fields, we can use `exclude`.

```python
class informationSerializer(serializers.ModelSerializer):

    class Meta:
        model = information
        exclude = ('phone',)
```

**Explanation:**

- `exclude` specifies the fields that should not be included.
- In this example, the `phone` field will be excluded.
- All other model fields will be included.

We can also exclude multiple fields:

```python
exclude = ('phone', 'description')
```

**When to use it?**

This approach is helpful when we want to include most of the model fields and exclude only a few.

**Important:** Use a comma when creating a tuple with only one element:

```python
exclude = ('phone',)
```

Without the comma, `('phone')` is just a string, not a tuple.

### Comparison of the Three Approaches

| Approach | Example | Result |
|---|---|---|
| All fields | `fields = '__all__'` | Includes every model field |
| Selected fields | `fields = ('name', 'description')` | Includes only the specified fields |
| Exclude fields | `exclude = ('phone',)` | Includes all fields except the specified fields |

**Important DRF Rule:** We must use either `fields` or `exclude` in the `Meta` class. We cannot use both together.

## 5. Complete ModelSerializer Example

```python
from rest_framework import serializers
from app_003_serialization.models import information


def validate_name(value):

    if value.lower() == 'shiv':
        raise serializers.ValidationError(
            'Name should not be Shiv.'
        )

    return value


class informationSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        max_length=100,
        validators=[validate_name]
    )

    class Meta:
        model = information
        fields = '__all__'
```

## 6. Important Points to Remember

1. ModelSerializer is recommended when we are working with Django Model objects.
2. ModelSerializer automatically generates serializer fields based on the model.
3. We must specify `fields` or `exclude` inside the `Meta` class.
4. `fields = '__all__'` includes all model fields.
5. `fields = ('name', 'description')` includes only selected fields.
6. `exclude = ('phone',)` excludes the specified field.
7. ModelSerializer provides default implementations of `create()` and `update()`.
8. We can override `create()` and `update()` when custom behavior is required.
9. We can declare individual fields explicitly when we need custom validation or field configuration.
10. We can use Field-Level Validation, Object-Level Validation, and Validators with ModelSerializer.

## 7. Final Summary

```text
                 ModelSerializer
                       |
                       v
              Specify Django Model
                       |
                       v
             Specify fields / exclude
                       |
                       v
         Automatically Generate Fields
                       |
              +--------+--------+
              |                 |
              v                 v
         Serialization    Deserialization
                                |
                                v
                           Validation
                                |
                                v
                       Default create()
                       Default update()
                                |
                                v
                            Database
```

**Remember:** Regular Serializer requires us to define more things manually, whereas ModelSerializer automatically handles many operations based on the Django model.