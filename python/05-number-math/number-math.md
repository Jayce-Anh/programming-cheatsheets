# 5. NUMBER & MATH

Python supports integers, floats, and complex numbers with built-in math operations.

## Best Practices

- Use `//` for integer (floor) division to avoid accidental floats
- Use `**` for exponentiation instead of `pow()` for simple cases
- Use `round()` carefully — Python uses banker's rounding (rounds to even)
- Import `math` module for advanced operations

## Arithmetic Operators

| Operator | Syntax | Example | Result | Description |
|----------|--------|---------|--------|-------------|
| `+` | `a + b` | `10 + 3` | `13` | Addition |
| `-` | `a - b` | `10 - 3` | `7` | Subtraction |
| `*` | `a * b` | `10 * 3` | `30` | Multiplication |
| `/` | `a / b` | `10 / 3` | `3.333...` | Division (float) |
| `//` | `a // b` | `10 // 3` | `3` | Floor division (int) |
| `%` | `a % b` | `10 % 3` | `1` | Modulo (remainder) |
| `**` | `a ** b` | `2 ** 3` | `8` | Exponentiation |

## Comparison Operators

Return `True` or `False`. Commonly used in conditionals and loops.

| Operator | Syntax | Meaning | Example | Result |
|----------|--------|---------|---------|--------|
| `==` | `a == b` | Equal to | `5 == 5` | `True` |
| `!=` | `a != b` | Not equal to | `5 != 3` | `True` |
| `<` | `a < b` | Less than | `5 < 3` | `False` |
| `<=` | `a <= b` | Less than or equal | `5 <= 5` | `True` |
| `>` | `a > b` | Greater than | `7 > 3` | `True` |
| `>=` | `a >= b` | Greater than or equal | `5 >= 6` | `False` |

## Augmented Assignment Operators

Shorthand for updating a variable using an arithmetic operation.
```python
x = 2

# Instead of:
x = x + 1      # x = 3

# Use shorthand:
x += 1          # x = 3
```
| Operator | Equivalent | Example `x = 9` | Result |
|----------|------------|---------|--------|
| `+=` | `a = a + b` | `x += 3` | `12` |
| `-=` | `a = a - b` | `x -= 3` | `6` |
| `*=` | `a = a * b` | `x *= 3` | `27` |
| `/=` | `a = a / b` | `x /= 3` | `3.0` |
| `//=` | `a = a // b` | `x //= 3` | `3` |
| `%=` | `a = a % b` | `x %= 3` | `0` |
| `**=` | `a = a ** b` | `x **= 3` | `729` |

## Built-in Functions

```python
abs(-5)              # 5              # Absolute value
round(3.7)           # 4              # Round to nearest integer
round(3.14159, 2)    # 3.14           # Round to 2 decimal places
min(3, 1, 2)         # 1              # Minimum value
max(3, 1, 2)         # 3              # Maximum value
sum([1, 2, 3])       # 6              # Sum of iterable
pow(2, 3)            # 8              # Same as 2 ** 3
```

## Format as Percentage

```python
ratio = 0.125
f"{ratio:.2%}"       # "12.50%"       # 2 decimal places
f"{0.5:.1%}"         # "50.0%"        # 1 decimal place
f"{0.3333:.0%}"      # "33%"          # No decimal places
```
