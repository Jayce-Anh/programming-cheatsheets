# 8. DICTIONARY

An ordered collection of key-value pairs, created with `{}`. Keys must be unique and immutable.

## Best Practices

- Use `.get(key, default)` instead of `dict[key]` to avoid `KeyError`
- Use `.items()` when you need both keys and values in a loop
- Use dict comprehensions for transforming data
- Keys must be immutable types: strings, numbers, or tuples

## Syntax:

```python
my_dict = {"key": value, "key2": value2}

my_dict["key"]                  # access (raises KeyError if missing)
my_dict.get("key", default)     # safe access with default

{key: value for item in iterable}   # comprehension
```

- `{}`: create a dictionary
- Keys must be immutable (strings, numbers, or tuples)

## Example

```python
person = {"name": "John", "age": 30, "city": "NYC"}
empty_dict = {}
from_constructor = dict(name="John", age=30)
from_pairs = dict([("a", 1), ("b", 2)])

# Access values
person["name"]               # "John"             # Raises KeyError if missing
person.get("age")            # 30
person.get("job", "N/A")     # "N/A"              # Default if key not found

# Get keys, values, items
person.keys()                # dict_keys(['name', 'age', 'city'])
person.values()              # dict_values(['John', 30, 'NYC'])
person.items()               # dict_items([('name', 'John'), ...])
```

## Modify

```python
person["email"] = "john@email.com"             # Add new key
person["age"] = 31                             # Update existing value
person.update({"job": "Engineer", "age": 32})  # Update multiple

del person["city"]                             # Delete key
person.pop("email")                            # Remove and return value
person.pop("missing", "default")               # "default" — safe remove
person.popitem()                               # Remove and return last item
person.clear()                                 # Remove all items
```

## Methods

```python
person = {"name": "John", "age": 30}

"name" in person                 # True
"email" in person                # False
person.setdefault("age", 25)     # 30    # Returns existing value
person.setdefault("city", "NYC") # "NYC" # Sets and returns if key missing
person.copy()                    # Shallow copy
```

## Comprehension

```python
squares = {x: x**2 for x in range(5)}          # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
evens = {x: x**2 for x in range(10) if x % 2 == 0}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict(zip(keys, values))                         # {"a": 1, "b": 2, "c": 3}

# Swap keys and values
original = {"a": 1, "b": 2}
swapped = {v: k for k, v in original.items()}  # {1: "a", 2: "b"}
```

## Iterate Dictionary

```python
person = {"name": "John", "age": 30, "city": "NYC"}

for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

## Nested Dictionaries

```python
users = {
    "user1": {"name": "John", "age": 30},
    "user2": {"name": "Jane", "age": 25}
}

users["user1"]["name"]    # "John"
users["user1"]["age"] = 31
```
