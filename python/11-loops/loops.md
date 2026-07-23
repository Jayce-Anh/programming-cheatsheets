# 11. LOOPS
Loops repeat a block of code — `for` iterates over a sequence, `while` runs until a condition is false.

## Best Practices
- Use `for` when the number of iterations is known; use `while` when it is not
- Use `enumerate()` instead of manually tracking an index
- Always update the condition in `while` loops to avoid infinite loops
- Use `break` to exit early, `continue` to skip an iteration

## Syntax:
```python
# FOR LOOP:
for value in sequence:
    action
```
- `value`: the current item in each iteration, can give any name, `i` is common
- `sequence`: any iterable (list, range, string, tuple, ...)
- `action`: the code block to run on each iteration (must be indented)
- `for` each `value` in this `sequence`, perform this `action`

```python
# WHILE LOOP:
while condition:
    action
```
- `condition`: runs the loop as long as this condition is `True`
- Always update the condition inside the loop to avoid infinite loops

## For Loop 
```python
# Loop through a range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8, 2):   # 2, 4, 6 (start at 2, stop at 8, each 2 step)
    print(i)

# Loop through a collection
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# With index using enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")  # "0: apple", "1: banana", ...
```

## While Loop
```python
# Count confirmations using a while loop
count = 0
while count < 5:
    print(count)
    count += 1  # add +1 value at every loop until it's unmet the condition (count >=5 -> Failed -> Stop the loop)           
# Output: 0, 1, 2, 3, 4

total_guest = 10
guest_count = 0
while guest_count < total_guest:
    guest_count += 1
    print(guest_count, "guests so far!")
print("We have", guest_count, "guests coming!")
# => Output: 1 guests so far!; 2 guests so far!; ... 10 guests so far!; We have 10 guests coming!

# Loop until user input
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
```

## Loop Control
```python
for i in range(10):
    if i == 3:
        continue            # Skip this iteration
    if i == 7:
        break               # Exit loop entirely
    print(i)                # Prints: 0, 1, 2, 4, 5, 6
```

## Useful Patterns
```python
# use loop with condition
score = [10, 20, 50, 100, 5, 70]
for i in score:
    if i > 50:
        print("pass")
    elif 20 <= i <= 50:
        print("retake exam")
    else:
        print("retake course")
# Output: retake course, retake exam, retake exam, pass, retake course, pass

# Loop with zip (parallel iteration)
names = ["Alice", "Bob"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 90
# Bob: 85

# Loop with dict items
person = {"name": "John", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")
# name: John
# age: 30

# List comprehension (preferred for simple transformations)
squares = [x**2 for x in range(5)]   # [0, 1, 4, 9, 16]
```

