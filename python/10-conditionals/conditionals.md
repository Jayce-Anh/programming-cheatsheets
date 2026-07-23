# 10. CONDITIONALS

Conditionals control the flow of execution based on whether a condition is `True` or `False`.

## Best Practices

- Avoid comparing booleans explicitly: use `if is_active:` not `if is_active == True:`
- Use `elif` instead of multiple `if` blocks when conditions are mutually exclusive
- Use ternary expressions for simple one-line conditions
- Use `in` to check membership instead of chaining `==` comparisons

## Syntax:

```python
if condition_1:         # if condition 1 met -> perform action 1 
    action_1
elif condition_2:       # if condition 2 met -> perform action 2
    action_2
    ...
else:                   # if all action are not met -> perform action 3 
    action_3

value = true_value if condition else false_value     # ternary
```

- `if/elif/else`: control flow based on condition
- Ternary: one-line shorthand for simple `if/else`

## Example

```python
age = 18

if age < 13:
    category = "child"
elif age < 20:
    category = "teenager"
else:
    category = "adult"

# Multiple if — each condition is checked independently (not mutually exclusive)
score = 85
if score >= 60:
    print("Passed")     # runs
if score >= 80:
    print("Good")       # runs
if score >= 90:
    print("Excellent")  # skipped
# Output: "Passed" and "Good" (both run)

# Nest condition:
my_age = 25
your_age = int(input("Enter your age: "))
print(your_age)
if your_age > my_age:
    if your_age - my_age != 1:
        print(f'You are {your_age - my_age} year older than me')
    else: 
        print(f'You are 1 year older than me')
elif your_age < my_age:
    if my_age - your_age != 1:
        print(f'You are {my_age - your_age} year younger than me')
    else: 
        print(f'You are 1 year younger than me')
else:
    print('We are the same age')
```

## Logical Operators

| Operator | Meaning | Example `x = 2` | Result |
|----------|---------|---------|--------|
| `and` | Both must be `True` | 1 < x < 3 | `True` only if both are true |
| `or` | At least one must be `True` | 1 < x 0 | `True` if either is true |
| `not` | Inverts the boolean | x > 1 | Output is `Failed` so this become `True` |

```python
age = 20
has_car = True
is_weekend = False
is_holiday = True

# Combine
if age >= 18 and has_car:
    print("Roadtrip!")

if is_weekend or is_holiday:
    print("No work today.")

if not is_raining:
    print("You can go outside.")
```

## Membership & Identity Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `in` | Value exists in sequence | `"a" in "cat"` | `True` |
| `not in` | Value does not exist | `5 not in [1, 2, 3]` | `True` |
| `is` | Same object in memory | `x is None` | `True` if `x` is `None` |
| `is not` | Not the same object | `x is not None` | `True` if `x` is not `None` |

```python
"a" in "cat"                        # True
"z" in "cat"                        # False
3 in [1, 2, 3]                      # True
5 not in [1, 2, 3]                  # True

role = "admin"
if role in ("admin", "moderator"):  # preferred over chaining ==
    print("Access granted")

x = None
if x is None:
    print("No value")

if x is not None:
    print("Has value")
```

> Use `is` / `is not` for `None` checks — not `==`

## Ternary (One-line If)

```python
# value_if_true if condition else value_if_false
status = "adult" if age >= 18 else "minor"
label = "even" if x % 2 == 0 else "odd"
```
