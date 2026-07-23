# 4. STRING

Strings are immutable sequences of characters, enclosed in single or double quotes.

## Best Practices

- Prefer double quotes `""` for consistency
- Use f-strings for string formatting (cleaner than `.format()`)
- Use `"""` for multi-line strings or docstrings
- Use `"\n"` for line breaks, `"\\"` for a literal backslash

## Syntax:
```python
"string"
'string'

"""
multi-line
string
"""

f"text {variable} text"         # f-string (embed expressions)
```

- `f"..."`: evaluates `{expression}` at runtime
- `""" ... """`: multi-line string or docstring

## Examples
```python
single = 'Hello'
double = "World"
multi_line = """
Line 1
Line 2
"""

# Concatenation and repetition
greeting = "me" + "ow!"   # "meow!"
repeat = "Meow!" * 3      # "Meow!Meow!Meow!"
length = len("Python")    # 6
```

## Methods

```python
"a".upper()                     # "A"              # Uppercase
"A".lower()                     # "a"              # Lowercase
" a ".strip()                   # "a"              # Remove whitespace both ends
" a ".lstrip()                  # "a "             # Remove whitespace left
" a ".rstrip()                  # " a"             # Remove whitespace right
"hello".startswith("he")        # True
"hello".endswith("lo")          # True
"abc".replace("bc", "ha")       # "aha"
"a b c".split()                 # ["a", "b", "c"]
"a:b:c".split(":")              # ["a", "b", "c"]
"-".join(["a", "b"])            # "a-b"
"hello".find("ll")              # 2                # Index of substring (-1 if not found)
"hello".count("l")              # 2                # Count occurrences
"hello".index("o")              # 4                # Index of first occurrence
```

## Indexing & Slicing

```python
text = "Hello, Python"
text[0]      # "H"               # First character
text[-1]     # "n"               # Last character
text[1:4]    # "ell"             # Slice [start:end]
text[:3]     # "Hel"             # From start
text[3:]     # "lo, Python"      # To end
text[::2]    # "Hlo yhn"         # Every 2nd character
text[::-1]   # "nohtyP ,olleH"   # Reverse
```

## F-string (Recommended)

An **f-string** is a string that starts with `f` or `F` before the quotes. Inside it, you put **expressions in curly braces** `{...}`. Python evaluates those expressions and turns the whole thing into one string.

- Use f-strings when you want to **mix text and variables** (or math, function calls, etc.) in a readable way.
- `{name}` inserts the value of `name`; `{age + 1}` can be any valid Python expression.
- Prefer f-strings over older style `.format()` for everyday formatting.

```python
name = "Jayce"
age = 20

f"Hello, {name}!"                                        # "Hello, Jayce!"
f"{name} is {age} years old"                             # "Jayce is 20 years old"
f"Debug: {age=}"                                         # "Debug: age=20"
f"Result: {7 / 2}"                                       # "Result: 3.5"      # Format as float
f"{0.125:.2%}"                                           # "12.50%"           # Format as percentage
f"{3.14159:.3f}"                                         # "3.142"            # Format as float with 3 decimal
f"The length of your name is {len(name)} characters"     # "The length of your name is 5 characters"
```

## `.format()` Method

```python
template = "Hello, {name}! You're {age}."
template.format(name="Jayce", age=20)   # "Hello, Jayce! You're 20."

"My name is {} and I am {} years old.".format("John", 16)
# "My name is John and I am 16 years old."
```
