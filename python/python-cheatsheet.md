# Python cheatsheet

## Table of contents
1. [Comments](#1-comments)
2. [Data Types](#2-data-types)
3. [Variables](#3-variables)
4. [String](#4-string)
5. [Number & Math](#5-number--math)
6. [Conditionals](#6-conditionals)
7. [Loops](#7-loops)
8. [Function](#8-function)

## 1. Comments
* Always add a space after the #
* Use comments to explain your code
* Use ''' ''' for multi block comments

```python
# This is a comment
# print("This code will not run")
print("This will run")
```
## 2. Data Types
* Python is dynamically typed
* Use None to represent missing or optional values
* Use type() to check object type
* Check for a specific type with isinstance()
* issubclass() checks if a class is a subclass

```python
int: 5, -10                         # Integer numbers
float: 3.14, -6.9                   # Floating numbers
str: "Hello, how are you ?"         # String(text)
bool: True or False                 # Boolean values
list: [1, 2, "abc"]                 # Ordered, mutable collection
tuple: (1, 2, "abc")                # Ordered, immutable collection
dict: {"key": "value"}              # Key-value pairs
set: {1, 2, 3}                      # Unordered, unique collection
complex: 2+3j                       # Complex number
```

```python
int("42")                # 42
float("3.14")            # 3.14
str(42)                  # "42"
bool(1)                  # True
list("abc")              # ["a", "b", "c"]
```
## 3. Variables
* Variables are created when first assigned
* Variables can be reassigned values and data types at any time
* Use descriptive variable names
* Follow snake_case convention

```python
# Assign values
name = "Leo"
age = 7
height = 1.85
height = 1.83
shopping_list7days = ["apple", "egg", "beef"]
# Assign multiple values
x, y = 10, 20
a = b = c = 0
```
## 4. String 
* It's recommended to use double-quotes "" for strings
* Use "\n" to create a line break
* To write a backslash in a normal string, write "\\" 

```python
single = 'Hello'
double = "World"
line_break = "This is line 1\nThis is line 2" 

greeting = "me" + "ow!"  # "meow!"
repeat = "Meow!" * 3     # "Meow!Meow!Meow!"
length = len("Python")   # 6
```

* Methods:
```python
"a".upper()                     # "A"              # Uppercase the string
"A".lower()                     # "a"              # Lowercase the string
" a ".strip()                   # "a"              # Remove whitespace from both ends
" a ".lstrip()                  # "a "             # Remove whitespace from left
" a ".rstrip()                  # " a"             # Remove whitespace from right
"hello".startswith("he")        # True             # Check if starts with substring
"hello".endswith("lo")          # True             # Check if ends with substring
"abc".replace("bc", "ha")       # "aha"            # Replace substring
"a b c".split()                 # ["a", "b", "c"]  # Split string into list
"a:b:c".split(":")              # ["a", "b", "c"]  # Split with custom delimiter
"-".join(["a", "b"])            # "a-b"            # Join list into string
```

### Indexing & Slicing:

```python
text = "Hello, Python"
text[0]      # "H" (first)
text[-1]     # "n" (last)
text[1:4]    # "ell" (slice)
text[:3]     # "Hel" (from start)
text[3:]     # "lo, Python" (to end)
text[::2]    # "Hlo yhn" (every 2nd)
text[::-1]   # "nohtyP ,olleH" (reverse)
```
### F-string
* f-string allow inline expression evaluation and formatting, making string construction concise and readable
```python
math_division = 7/2
print(f"Result: {math_division}")  # "Result: 3.5"
# or
print(f"Result: {7/2}")            # "Result: 3.5"
```
### Formatting:
```python
# f-strings
name = "Aubrey"
age = 2
f"Hello, {name}!"               # "Hello, Aubrey!"
f"{name} is {age} years old"    # "Aubrey is 2 years old"
f"Debug: {age=}"                # "Debug: age=2"

# Format method
template = "Hello, {name}! You're {age}."
template.format(name="Aubrey", age=2)    # "Hello, Aubrey! You're 2."
```

## 5. Number & Math
### Arithmetic Operators:
```python
10 + 3    # 13                        # Addition
10 - 3    # 7                         # Subtraction
10 * 3    # 30                        # Multiplication
10 / 3    # 3.3333333333333335        # Division (float)
10 // 3   # 3                         # Floor division (int)
10 % 3    # 1                         # Modulo (remainder)
2 ** 3    # 8                         # Exponentiation
```
### Functions:
```python 
abs(-5)              # 5              # Absolute value
round(3.7)           # 4              # Round to nearest integer
round(3.14159, 2)    # 3.14           # Round to 2 decimal places
min(3, 1, 2)         # 1              # Minimum value
max(3, 1, 2)         # 3              # Maximum value
sum([1, 2, 3])       # 6              # Sum of iterable
pow(2, 3)            # 8              # Power (same as 2 ** 3)
```

### Format as Percentage:
```python
ratio = 0.125
f"{ratio:.2%}"       # "12.50%"       # Format as percentage with 2 decimals
f"{0.5:.1%}"         # "50.0%"        # Format as percentage with 1 decimal
f"{0.3333:.0%}"      # "33%"          # Format as percentage with no decimals
```

## 6. Conditionals
### If-Elif-Else:

```python
if age < 13:
    category = "child"
elif age < 20:
    category = "teenager"
else:
    category = "adult"
```

### Comparison Operators
```python
x == y # Equal to
x != y # Not equal to
x < y  # Less than
x <= y # Less than or equal
x > y  # Greater than
x >= y # Greater than or equal
```

### And-Or-Not:
```python
if age >= 18 and has_car:
    print("Roadtrip!")

if is_weekend or is_holiday:
    print("No work today.")

if not is_raining:
    print("You can go outside.")
```

## 7. Loops
* range(5) generates 0 through 4
* Use enumerate() to get index and value
* "break" exits the loop, "continue" skips to next iteration
* Be careful with while loops to not create an infinite loop

### For loops: 
    - Use when you know how many times to iterate or when iterating over a collection

```python
# Loop through range
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# Loop through collection
fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)        # "apple", "banana"

# With enumerate for index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")  # "0: apple", "1: banana"
```

### While loops: 
    - Use when you need to loop until a condition becomes false

```python
count = 0
while count < 5:
    print(count)
    count += 1          # 0, 1, 2, 3, 4

# Infinite loop (be careful!)
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
```

### Loop Control:

```python
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 7:
        break     # Exit loop
    print(i)      # Prints: 0, 1, 2, 4, 5, 6
```

## 8. Function
* Define functions with def
* Always use () to call a function
* Add return to send values back
* Create anonymous functions with the lambda keyword

### Define function
```python
def greet():
    return "Hello!"

def greet_person(name):
    return f"Hello, {name}!"

def add(x, y=10):    # Default parameter
    return x + y
```

### Calling Functions:
```python
greet()                   # "Hello!"
greet_person("Bartosz")   # "Hello, Bartosz"
add(5, 3)                 # 8
add(7)                    # 17
```
