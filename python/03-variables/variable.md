# 3. VARIABLES

Variables are names that store a reference to a value in memory.

## Best Practices

- Use `snake_case` for variable names
- Use descriptive names that reflect the value's purpose
- Variables can be reassigned to any type at any time (Python is dynamically typed)
- Avoid single-letter names except in short loops (`i`, `x`, `y`)

## Naming Rules

- Must start with a letter or underscore `_`
- Can contain letters, numbers, and underscores
- Case-sensitive — `myVar` and `myvar` are different variables
- Cannot use Python reserved keywords (`if`, `for`, `class`, `return`, ...)

## Syntax:

```python
variable_name = value

x, y = value1, value2          # multiple assignment
a = b = c = value              # same value to multiple variables
```

- `variable_name`: use `snake_case`
- `=`: assignment operator (not equality)

## Examples

```python
# Assign values
name = "Jayce"
age = 20
height = 1.85
is_active = True
shopping_list = ["apple", "egg", "beef"]

# Reassign (type can change)
height = 1.83
height = "tall"

# Assign multiple variables in one line
x, y = 10, 20

# Assign same value to multiple variables
a = b = c = 0
```

## Naming Conventions

| Style | Example | Use For |
|-------|---------|---------|
| `snake_case` | `user_name` | Variables, functions |
| `UPPER_SNAKE_CASE` | `MAX_RETRIES` | Constants |
| `PascalCase` | `UserProfile` | Classes |
