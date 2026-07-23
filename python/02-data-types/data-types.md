# 2. DATA TYPES

Python is dynamically typed — no need to declare a variable's type explicitly.

## Built-in Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `5`, `-10` | Integer numbers |
| `float` | `3.14`, `-6.9` | Decimal numbers |
| `str` | `"Hello"` | Text (string) |
| `bool` | `True`, `False` | Boolean values |
| `list` | `[1, 2, "abc"]` | Ordered, mutable collection |
| `tuple` | `(1, 2, "abc")` | Ordered, immutable collection |
| `dict` | `{"key": "value"}` | Key-value pairs |
| `set` | `{1, 2, 3}` | Unordered, unique collection |
| `complex` | `2+3j` | Complex numbers |
| `None` | `None` | Represents missing/no value |

## Best Practices

- Use `None` for missing or optional values (not `0` or `""`)
- Use `type` or `isinstance()` to check type 

## Examples

```python
# Check type
x = 42
print(type(x))          # <class 'int'>
print(isinstance(x, int))   # True
print(isinstance(x, (int, float)))  # True for either type

# Type conversion (casting)
int("42")        # 42
float("3.14")    # 3.14
str(42)          # "42"
bool(1)          # True
bool(0)          # False
list("abc")      # ["a", "b", "c"]
```
