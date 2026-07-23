# 12. FUNCTION

**Built-in functions** (e.g. `print()`, `len()`, `sum()`) are provided by Python; you import or call them
**Custom function** is a reusable block of code that performs a specific task, defined with `def`.

## Best Practices

- Use descriptive function names in `snake_case`
- Keep functions small — each function should do one thing
- Use default parameters instead of handling `None` inside the function
- Always use `return` explicitly; avoid relying on implicit `None`
- Write a docstring for non-obvious functions

## Syntax:

```python
def function_name(parameter, optional=default):
    action
    return value

# Call function: 
function_name(arguments) # arguments - value you pass when you call a function

lambda parameter: expression    # anonymous one-line function
```

- `def`: defines a named function
- `return`: sends back a value (returns `None` if omitted)
- `lambda`: for short, simple operations inline

## Examples

```python
def greet():
    return "Hello!"

greet()                     # Output "Hello!"

def greet_person(name):
    return f"Hello, {name}!"

greet_person("Jayce")       # Output: "Hello, Jayce!"

def add(x, y=10):           # Default parameter
    return x + y

add(5, 3)                   # Output: 8
add(7)                      # Output: 17
```

## Return Values

```python
# No return (implicitly returns None)
def print_message():
    print("Hello!")

# Single return
def square(x):
    return x ** 2

# Multiple return values (as a tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)
low, high, total = get_stats([1, 2, 3, 4, 5])

# Early return (guard clause)
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```

## Arguments (defaults, positional & keyword)

**Parameter** = name in `def`; **argument** = value you pass when you call.

Parameters can have **defaults** in the `def` line. When you **call** the function:

- **Positional arguments** are matched **by order** (`average(nums, True, 2)` → `do_round=True`, `ndigits=2`).
- **Keyword arguments** use `name=value` so the call is clear and you can skip parameters that keep their default (`average(nums, do_round=False)`).

Note: Do not name a parameter like `round` — it **shadows** the built-in `round()` function.

```python
# Average numbers:
nums = [9.2, 21.12, 32.5, 40, 67.6969]  

# Define the function with default arguments
def average(numbers, do_round=True, ndigits=3):
    avg = sum(numbers) / len(numbers)
    if do_round:
        avg = round(avg, ndigits)
    return avg

print(f"Average: {average(nums)}")                    # defaults → 34.103
print(f"Average: {average(nums, True, 2)}")           # positional → 34.1
print(f"Average: {average(nums, do_round=False)}")    # keyword → no rounding (ndigits unused)
print(f"Average: {average(nums, False, 4)}")          # positional False; 4 ignored if not rounding

# PC discount
original_price = 899.99

# Define the function with default arguments
def pc_discount(price, discount_percent=15, round_result=True):
    discounted_price = price - (price * (discount_percent / 100))
    
    if round_result == True:
        # Round the result to two decimal places
        return round(discounted_price, 2)
    else:
        return discounted_price
# Call the function with default keyword arguments:
print(f"PC discount price: ${pc_discount(original_price)}") # Output: $764.99
# Call the function with keyword arguments changes:
print(f"PC discount price: ${pc_discount(price=original_price, discount_percent=25, round_result=False)}") # Output: $674.9925000000001
```

### Arbitrary arguments (`*args` and `**kwargs`)

- Arbitray arguments allow function to accepts any number of arguments
- `***args**` — positionals argument for a **tuple**.
- `****kwargs`** — keywords argument for a **dictionary**.
- Use these when function input is dynamic or flexible.

```python
# *args:
# Average function only except one argument call "values"
def average(values):
    average_value = sum(values) / len(values)
    return round(average_value, 2)
print(average([1, 2, 3, 4, 5]))  # OK: one argument
# print(average(1, 2, 3, 4, 5)) # Error: 5 arguments -> Too many arguments

# Fix:
# *args: packs many positional arguments into a tuple named args.
def average_many(*args):
    average_value = sum(args) / len(args)
    return round(average_value, 2)

print(average_many(1, 2, 3, 4, 5))  # OK: five separate ints → args is (1, 2, 3, 4, 5)

# average(values) → strict, expects 1 iterable
# average_many(*args) → flexible, accepts multiple values

# **kwargs:
# Function expects one argument: a dictionary
def average_dict(nums):
    average_value = sum(nums.values()) / len(nums)
    return round(average_value, 2)

print(average_dict({"a": 1, "b": 2, "c": 3}))  # OK: one argument (dict)
# print(average_dict(a=1, b=2, c=3)) # Error: Unexpected keyword arguments -> TypeError

# Fix:
# **kwargs: packs many keyword arguments into a dict named kwargs
def average_many_kwargs(**kwargs):
    average_value = sum(kwargs.values()) / len(kwargs)
    return round(average_value, 2)

print(average_many_kwargs(a=1, b=2, c=3))  # OK → kwargs = {'a':1, 'b':2, 'c':3}
```

## Lambda Functions

Anonymous one-line functions. Use for short, simple operations.

### Syntax:

```python
lambda parameters: expression

lambda x: x * 2
lambda x, y: x + y
```

### Example:

```python
square = lambda x: x ** 2
print(square(5))             # Output: 25

add = lambda x, y: x + y
print(add(3, 4))      # Output: 7             

avg = lambda x: sum(x) / len(x)
print(avg([1,2,3,4])) # Output: 2.5
 
# Common use with map(), filter(), sorted()
numbers = [1, 2, 3, 4, 5]
# Use map() and filter() to applies the lambda to each item in numbers.
# So x becomes 1, then 2, then 3, etc.
squared = list(map(lambda x: x ** 2, numbers))       # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# map() returns the result of the lambda for each item.
# filter() keeps only items where the lambda returns True.

users = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
sorted_users = sorted(users, key=lambda x: x["age"])  # Check the key of the dictionary
print(sorted_users) # Output: [{'name': 'Jane', 'age': 25}, {'name': 'John', 'age': 30}]
```

## Docstrings

Documentation string placed right after `def`, `class`, or at the top of a **module**. It describes what the code does; tools and `help()` can read it. It is not a separate file unless you generate docs (e.g. Sphinx) from it.
Use `**"""`** `**"""`** to create a Docstring
Read with `**help(fn)`** or `**fn.__doc__`**.
Update with `**fn.__doc__ = "..."**` at runtime (rare; tests or dynamic wrappers).

```python
# One-line docstring:
def square(x):
    """Return x squared."""
    return x * x

# Multi-line docstring:
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The area as a number.
    """
    return width * height

# Access the docstring:
print(calculate_area.__doc__)

# Update at runtime (changes what help() / __doc__ show until process ends):
calculate_area.__doc__ = "Return width * height (rectangle area)."
print(calculate_area.__doc__)
```

## Scope

Where a name is visible: **local** (inside function) vs **global** (module). Lookup order: **LEGB** — Local → Enclosing → Global → Built-in. Use `**global x`** to assign a global; `**nonlocal x`** in a nested function to assign an outer (non-global) variable.

```python
global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    print(global_var)       # Can access global
    print(local_var)

# print(local_var)          # Error: not accessible outside function

# Modify a global variable inside a function
counter = 0
def increment():
    global counter
    counter += 1
```

