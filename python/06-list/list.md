# 6. LIST

An ordered, mutable collection that allows duplicate values, created with `[]`.

## Best Practices

- Use `append()` to add a single item, `extend()` to add multiple
- Use `list.copy()` or `list[:]` for shallow copies — avoid `list2 = list1` (same reference)
- Prefer list comprehensions over `map()`/`filter()` for readability
- Use `in` for membership checks instead of looping manually

## Syntax:

```python
my_list = [item1, item2, item3]

my_list[index]                  # access by index
my_list[start:end]              # slice (end is exclusive)
my_list[start:end:step]         # slice with step
```
- `[]`: create a list or access by index
- Negative index: `-1` is last, `-2` is second to last

## Example

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
empty = []
nested_list = [[1, 2], [3, 4], [5, 6]]

numbers[0]           # 1              # First element
numbers[-1]          # 5              # Last element
numbers[1:3]         # [2, 3]         # Slice
numbers[:2]          # [1, 2]         # From start
numbers[2:]          # [3, 4, 5]      # To end
numbers[::2]         # [1, 3, 5]      # Every 2nd element
numbers[::-1]        # [5, 4, 3, 2, 1] # Reverse

len(numbers)         # 5
```

## Method

```python
lst = [4, "hi", -2, True]

# Add
lst.append("bye")              # Add to end                         # Output: [4, "hi", -2, True, "bye"]
lst.insert(0, 6)               # Insert at index 0                  # Output: [6, 4, "hi", -2, True, "bye"]
lst.extend([7, "yo"])          # Add multiple items                 # Output: [6, 4, "hi", -2, True, "bye", 7, "yo"]

# Remove (must match a value that exists — not index)
lst.remove(4)                  # Remove first occurrence of value 4  # Output: [6, "hi", -2, True, "bye", 7, "yo"]
lst.pop()                      # Remove and return last item         # Output: [6, "hi", -2, True, "bye", 7]
lst.pop(0)                     # Remove and return item at index 0   # Output: ["hi", -2, True, "bye", 7]
del lst[0]                     # Delete by index                     # Output: [-2, True, "bye", 7]
lst.clear()                    # Remove all elements                 # Output: []

# Change
lst = [1, 2, 3]
lst[0] = 10                    # [10, 2, 3]
lst[1:3] = [20, 30]            # [10, 20, 30]
```

## Built-in function

```python
# min, max, sorted, abs — built-ins. sort, reverse, count, index, copy — list methods.
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - Sort in place (ascending). Returns None — do not assign: x = numbers.sort()
numbers.sort() # Output: [1, 1, 2, 3, 4, 5, 9]

# sort(reverse=True) - Sort in place (descending)
numbers.sort(reverse=True) # Output: [9, 5, 4, 3, 2, 1, 1]

# min() / max() — smallest and largest item (list does not need to be sorted)
print(numbers)                      # Output: [9, 5, 4, 3, 2, 1, 1]
print(min(numbers), max(numbers))   # Output: 1 9

# sorted() - sort and returns a NEW list; the original list is unchanged
original = [3, 1, 4, 1, 5, 9, 2]
sorted(original)                    # Output: [1, 1, 2, 3, 4, 5, 9]  (original still [3, 1, 4, ...])
sorted(original, reverse=True)      # Output: [9, 5, 4, 3, 2, 1, 1]

# reverse() - Reverse order in place. Returns None — do not assign
numbers.reverse()                   # Output: numbers is now [1, 1, 2, 3, 4, 5, 9]

# count(value) - How many times value appears in the list
numbers.count(1)                    # Output: 2

# index(value) - Index of first occurrence of value (error if not found)
numbers.index(4)                    # Output: 4

# copy() - Shallow copy (new list, same items)
numbers_copy = numbers.copy()       # Output: [1, 1, 2, 3, 4, 5, 9]  (separate list from numbers)

# abs(x) - Absolute value: distance from zero (drops the sign). Built-in, not a list method.
abs(-5)                             # Output: 5
abs(5)                              # Output: 5
abs(0)                              # Output: 0
abs(3 - 10)                         # Output: 7
abs(10 - 3)                         # Output: 7   # same distance the other way
```

## Comprehension

```python
squares = [x**2 for x in range(5)]                     # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]           # [0, 2, 4, 6, 8]
result = [x if x > 0 else 0 for x in [-1, 2, -3, 4]]  # [0, 2, 0, 4]
matrix = [[i*j for j in range(3)] for i in range(3)]   # [[0,0,0],[0,1,2],[0,2,4]]
```

## Operations

```python
# Membership
1 in [1, 2, 3]           # True

# Concatenation (creates new list)
[1, 2] + [3, 4]          # [1, 2, 3, 4]

# Repetition
[1, 2] * 3               # [1, 2, 1, 2, 1, 2]

# Unpacking
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2, 3, 4]

# Built-in functions
min([1, 2, 3])           # 1
max([1, 2, 3])           # 3
sum([1, 2, 3])           # 6
all([True, True])        # True   # All elements truthy
any([False, True])       # True   # Any element truthy
```

## Nested List

Nested lists are lists that contain other lists. Use `[i][j]` to access elements.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix[0]            # [1, 2, 3]     # First row
matrix[1][2]         # 6             # Row 1, column 2
matrix[-1][-1]       # 9             # Last element

# Modify
matrix[0][0] = 10
matrix[1] = [0, 0, 0]

# Iterate
for row in matrix:
    for cell in row:
        print(cell, end=" ")

for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        print(f"[{i}][{j}] = {cell}")
```
