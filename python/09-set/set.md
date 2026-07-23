# 9. SET

An unordered collection of unique elements. Ideal for removing duplicates and membership checks.

## Best Practices

- Use `set()` to create an empty set — `{}` creates an empty dict, not a set
- Use `discard()` instead of `remove()` to avoid errors on missing elements
- Sets are unordered — do not rely on insertion order
- Use `frozenset` when you need an immutable set (e.g., as a dict key)

## Syntax:

```python
my_set = {item1, item2, item3}
empty_set = set()               # {} would create an empty dict

item in my_set                  # membership check (O(1))

{expression for item in iterable if condition}  # comprehension
```

- `{}`: creates a set only when non-empty
- No indexing — sets are unordered

## Example

```python
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", True, 3.14}
empty = set()                       # {} would create an empty dict
from_list = set([1, 2, 2, 3])       # {1, 2, 3} — duplicates removed

# No indexing (sets are unordered)
1 in numbers            # True
6 in numbers            # False
len(numbers)            # 5
```

## Modify

```python
numbers.add(6)                 # Add single element
numbers.update([7, 8, 9])      # Add multiple elements
numbers.update({10, 11})       # Add from another set

numbers.remove(6)              # Raises KeyError if not found
numbers.discard(7)             # No error if not found (safer)
numbers.pop()                  # Remove and return a random element
numbers.clear()                # Remove all elements
```

## Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (join)
a | b  # or a.union(b)                  # {1, 2, 3, 4, 5, 6}    

 # Intersection
a & b  # or a.intersection(b)           # {3, 4}                

# Difference
a - b  # or a.difference(b)             # {1, 2}               

# Symmetric difference
a ^ b  # or a.symmetric_difference(b)   # {1, 2, 5, 6}          

# Subset / superset
{1, 2}.issubset({1, 2, 3})     # True
{1, 2, 3}.issuperset({1, 2})   # True
{1, 2}.isdisjoint({3, 4})      # True   # No common elements
```

## Comprehension

```python
squares = {x**2 for x in range(5)}             # {0, 1, 4, 9, 16}
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
```

## Operations

```python
numbers = {-2, 0, 12, 5, 7}

list(numbers)                        # [-2, 0, 5, 7, 12]   # Order may vary
tuple(numbers)                       # (-2, 0, 5, 7, 12)   # Order may vary
sorted(numbers)                      # [-2, 0, 5, 7, 12]   # Returns a sorted list
sorted(numbers, reverse=True)        # [12, 7, 5, 0, -2]   # Descending

numbers.copy()                       # Shallow copy

# Frozen set (immutable, can be used as dict key)
frozen = frozenset([1, 2, 3])
# frozen.add(4)                      # Error: frozensets are immutable
```

## When to Use

```python
# Remove duplicates from a list
words = ["apple", "banana", "apple", "cherry"]
unique = set(words)             # {"apple", "banana", "cherry"}

# Fast membership check (O(1) vs O(n) for lists)
valid_ids = {101, 102, 103}
if user_id in valid_ids:
    print("Valid user")

# Find common/missing items between two collections
required = {"numpy", "pip", "python", "aws-cli"}
installed = {"numpy", "git", "pip", "python"}
missing = required - installed    # {"aws-cli"}
extra = installed - required      # {"git"}
common = required & installed     # {"numpy", "pip", "python"}
```

