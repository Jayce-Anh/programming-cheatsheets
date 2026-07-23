# 1. HELLO WORLD - INTRODUCTION TO PYTHON

Python is a high-level, general-purpose programming language known for its simple and readable syntax.

## What Python is Used For

| Area | Examples |
|------|---------|
| Web development | Django, Flask |
| Data science & AI | NumPy, Pandas, TensorFlow |
| Automation & scripting | File handling, web scraping |
| APIs & backend | REST APIs, microservices |
| DevOps | CI/CD scripts, infrastructure tools |

## How Python Works

```
Source code (.py)  →  Python Interpreter  →  Output
```

- No compilation step — runs line by line
- Dynamically typed — no need to declare variable types

---

## Hello World

```python
print("Hello, World!")
```

---

## Output — `print()`

```python
print("Hello")                  # Hello
print("Hi", "there")            # Hi there
print("Score:", 100)            # Score: 100
print("Line 1\nLine 2")         # Line 1
                                # Line 2
print("A", "B", sep="-")        # A-B
print("Loading", end="...")     # Loading...  (no newline)
```
* Use `print()` to display output to the console (standard output).
* It can print strings, numbers, variables, or any other object, converting them to a string before displaying.
---

## Variables

```python
name = "Jayce"          # str
age = 20                # int
height = 1.85           # float
is_active = True        # bool

x, y = 10, 20           # multiple assignment
a = b = c = 0           # same value to multiple variables
```

- Variable use to store data that your program can manipulate and use throughout its execution
- Use `snake_case` for variable names
- Variable in Python can be re-assgin

---

## Comments

```python
# single-line comment

'''
multi-line
comment
'''
```

- `#`: single-line comment
- `''' ... '''` or `""" ... """`: multi-line (also used as docstrings)

---

## Common Built-in Functions

```python
print("hello")          # Output: hello               # Output to console
len("hello")            # Output: 5                   # Length of string, list, etc.
type(42)                # Output: <class 'int'>       # Get type of a value
int("10")               # Output: 10                  # Convert to integer
float("3.14")           # Output: 3.14                # Convert to float
str(100)                # Output: "100"               # Convert to string
bool(0)                 # Output: False               # Convert to boolean
input("Enter: ")        # Output: (user's text)       # Read user input (returns str)
range(5)                # Output: range(0, 5)         # Iterator for 0, 1, 2, 3, 4
abs(-7)                 # Output: 7                   # Absolute value
round(3.567, 2)         # Output: 3.57                # Round to n decimal places
min(3, 1, 2)            # Output: 1                   # Smallest value
max(3, 1, 2)            # Output: 3                   # Largest value
sum([1, 2, 3])          # Output: 6                   # Sum of iterable
```

##  Check built-in documentation: `help()`

Pass a **function or type** (not a call with parentheses) to see its docstring and parameters:

```python
help(round)             # Shows what round() does and its arguments
help(len)
help(print)
# quit with q in the terminal pager
```
---