# 14. ERROR HANDLING

A **runtime error** is a problem that happens while the program is running. Python stops the program and shows an **exception** unless you handle it.

## Best Practices

- Catch specific exceptions, not bare `except:`
- Keep the `try` block small
- Use `raise` when input is invalid
- Use `finally` for cleanup like closing files
- Print or log the real error message while debugging

## Error types

| Error | Meaning | Example |
|------|---------|---------|
| `SyntaxError` | Invalid Python syntax | missing `:` |
| `NameError` | Variable not defined | `print(x)` |
| `TypeError` | Wrong type used | `"2" + 2` |
| `ValueError` | Right type, wrong value | `int("abc")` |
| `IndexError` | List index out of range | `nums[10]` |
| `KeyError` | Dictionary key not found | `user["age"]` |
| `ZeroDivisionError` | Divide by zero | `10 / 0` |
| `FileNotFoundError` | File does not exist | `open("x.txt")` |

## Syntax:

```python
try:
    risky_code
except SomeError:
    handle_error
except AnotherError as e:
    print(e)
else:
    run_if_no_error
finally:
    always_run

raise ValueError("message")
```

- `try`: code that may fail
- `except`: handles the error
- `else`: runs only if no error happens
- `finally`: runs no matter what
- `raise`: manually stops the function with an error and print out custom message

## Examples

```python
# try / except
def clean_text(text):
  # Attempt to clean the text
  try:
    return text.replace(" ", "_").lower()
  # Run this code if an error occurs
  except:
    print("The clean_text() function expects a string as an argument")
    
clean_text(187) 

# else and finally
file = None
try:                        # try to open the file  
    file = open("data.txt")
except FileNotFoundError:   # run if file not found
    print("File not found")
else:                       # run if file founded
    print(file.read()) 
finally:                    # always run this block (error or no error)
    if file:                # close file only if it was opened successfully
        file.close()
    print("Done")           # always print Done

# raise your own error
def clean_text(text):
  # Check the data type
  if type(text) == str:
    return text.replace(" ", "_").lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The clean_text() function expects a string as an argument, please check the data type provided!")
    
clean_text(123)
```

## Debugging tips

- Read the **last line** of the traceback first
- Check the **error type** and message
- Add `print()` to inspect variable values
- Test small parts of the code one by one
- Use `help()`, docs, or the traceback line number to find the problem
- Check the **line number** shown in the traceback
- Print the **type** of a value with `type(x)` if you are unsure
- Use `repr(x)` when `print(x)` is not clear enough
- Confirm your function inputs before debugging deeper logic
- Reproduce the bug with the **smallest example** possible
- Do not hide errors with bare `except:` while learning
- If needed, add `breakpoint()` to pause and inspect values