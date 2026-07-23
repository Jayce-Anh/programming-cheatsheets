# 7. TUPLES

An ordered, immutable collection. Faster than lists and used for fixed data.

## Best Practices

- Use tuples for data that should not change (coordinates, RGB colors, DB records, ...)
- Always include a trailing comma for single-element tuples: `(1,)`
- Prefer tuples as dictionary keys (they are hashable, lists are not)
- Use tuple unpacking instead of index access for clarity

## Syntax:

```python
my_tuple = (item1, item2, item3)
single = (item,)                # trailing comma required
no_parens = item1, item2        # also creates a tuple

my_tuple[index]                 # access by index
my_tuple[start:end]             # slice
x, y, z = my_tuple              # unpacking
```

- `()`: create a tuple (immutable — cannot be modified after creation)
- Trailing `,` is required for single-element tuples

## Example

```python
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", True, 3.14)
single = (1,)            # Trailing comma required for single element
empty = ()
no_parens = 1, 2, 3      # Also creates a tuple
nested_tuple = ((1, 2), (3, 4))

numbers[0]           # 1              # First element
numbers[-1]          # 5              # Last element
numbers[1:3]         # (2, 3)
len(numbers)         # 5
```

## Methods

```python
numbers = (1, 2, 3, 2, 4, 2)

numbers.count(2)     # 3              # Count occurrences
numbers.index(3)     # 2              # Index of first occurrence
```

## Operations

```python
a = ("rock", 10)
b = (-2, "9.5")

# Joining
a + b                        # ("rock", 10, -2, "9.5")

# Unpacking
x, y, z = (1, 2, 3)
first, *rest = (1, 2, 3, 4)  # first=1, rest=[2, 3, 4]

# Membership
-2 in b                      # True

# Convert to list (to modify)
list(a)              # ["rock", 10]

# Convert to tuple
c = [1, 3, "hello"]
tuple(c)             # (1, 3, "hello")

# Sort (returns a new list, tuples are immutable)
nums = (3, 1, 4, 1, 5)
sorted(nums)                             # [1, 1, 3, 4, 5]
tuple(sorted(nums))                      # (1, 1, 3, 4, 5)
tuple(sorted(nums, reverse=True))        # (5, 4, 3, 1, 1)
```

## Nested Tuples

```python
coordinates = ((0, 0), (1, 1), (2, 2))
example = ("python", 6, (6, 7), ("java", 67))

example[2]            # (6, 7)
example[3][0]         # "java"
coordinates[1][0]     # 1

# Unpack nested tuples
(x1, y1), (x2, y2) = ((0, 0), (1, 1))  # x1=0, y1=0, x2=1, y2=1

# Iterate
for x, y in coordinates:
    print(f"Point: ({x}, {y})")
```

## When to Use Tuples

```python
# Fixed data that shouldn't change
coordinates = (10.0, 20.0)
rgb_color = (255, 128, 0)

# Return multiple values from a function
def get_user():
    return "John", 25, "Engineer"
name, age, job = get_user()

# Dictionary keys (tuples are hashable, lists are not)
locations = {(0, 0): "origin", (1, 1): "point"}
```
