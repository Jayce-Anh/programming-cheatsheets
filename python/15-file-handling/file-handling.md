# 15. FILE HANDLING

File handling lets your program **read**, **write**, **append**, and **manage** files on your computer. In Python, the safest pattern is usually `with open(...)` because it closes the file automatically.

## Best Practices

- Use `with open(...)` files close automatically
- Prefer `encoding="utf-8"` for text files
- Use `"r"` for reading and `"w"` only when you want to replace the file
- Use `"a"` to add new content without deleting old content
- Check file paths carefully before writing
- Use `pathlib.Path` for cleaner path handling
- Handle errors like `FileNotFoundError` when needed

## Syntax:

```python
# Basic
path = "./downloads/data.txt"

file = open(path)
print(file.read())
file.close()

file = open(path, "a", encoding="utf-8")
print(file.write("/nNew data"))
file.close()

# Recommended: auto-close file
with open(path, encoding="utf-8") as file:
    content = file.read()

new_path = "./new_path/new-file.txt"

with open(new_path, x encoding="utf-8") as file:
    content = file.write("Hello mf")

# With pathlib
from pathlib import Path

path = Path("data.txt")
text = path.read_text(encoding="utf-8")
path.write_text("Hello", encoding="utf-8")
```

- `open()`: opens a file, default mode is reading so no need to specify 'r' or 'rt'
- First argument: file name or file path
- Second argument: file mode like `"r"` or `"w"`
- `encoding="utf-8"`: helps read and write text safely
- `file.close()`: closes the file manually
- `with`: closes the file automatically

## File modes

| Mode   | Meaning                              | File must exist? |
| ------ | ------------------------------------ | ---------------- |
| `"r"`  | Read text                            | Yes              |
| `"w"`  | Write text, overwrite old content    | No               |
| `"a"`  | Append text at the end               | No               |
| `"x"`  | Create new file, fail if file exists | No               |
| `"rb"` | Read binary                          | Yes              |
| `"wb"` | Write binary                         | No               |


## Common methods

| Method | Purpose | Example output |
|--------|---------|----------------|
| `file.read()` | Read the whole file | `"Hello\nPython"` |
| `file.readline()` | Read one line | `"Hello\n"` |
| `file.readlines()` | Read all lines into a list | `["Hello\n", "Python"]` |
| `content.split()` | Split text into words | `["Hello", "Python"]` |
| `content.splitlines()` | Split text into lines | `["Hello", "Python"]` |
| `file.write(text)` | Write text to file | `5` |
| `file.writelines(lines)` | Write a list of strings | `None` |
| `file.close()` | Close the file manually | `None` |


## Examples

```python
# Read the whole file
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Read one line at a time
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
    print(first_line)
    print(second_line)

# Loop through each line
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Write new content (overwrites old content)
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello\n")
    file.write("Python\n")

# Append content (keep old conntent)
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("New line\n")

# Create a file only if it does not exist
with open("new_file.txt", "x", encoding="utf-8") as file:
    file.write("Created successfully")

# Delete file:
import os
os.remove("old_file.txt")
```

## `pathlib` example

`pathlib` is a modern and cleaner way to work with paths.

```python
from pathlib import Path

file_path = Path("notes.txt")

# Check if file exists
print(file_path.exists())

# Read text
if file_path.exists():
    print(file_path.read_text(encoding="utf-8"))

# Write text
file_path.write_text("Hello from pathlib", encoding="utf-8")

# Build paths
folder = Path("data")
new_path = folder / "report.txt"
print(new_path)

# Delete file 
Path("data.txt").unlink()
```

## Working with JSON

Use the `json` module when the file stores structured data.

```python
import json

user = {"name": "Jayce", "age": 20}

# Write JSON
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=2)

# Read JSON
with open("user.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data["name"])
```

## Working with CSV

Use the `csv` module for comma-separated values.

```python
import csv

# Write CSV
with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["Jayce", 20])
    writer.writerow(["Anna", 22])

# Read CSV
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## Error handling

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

## Notes

- Text files use `str`
- Binary files use `bytes`
- `read()` is simple, but large files are better read line by line
- `"w"` deletes old content before writing new content
- `newline=""` is commonly used when writing CSV files
- Use `file.closed` to check whether a file is open or closed

## Common Pitfalls


| Issue                           | Tip                                           |
| ------------------------------- | --------------------------------------------- |
| File not found                  | Check the path and current working directory  |
| Wrong encoding                  | Try `encoding="utf-8"`                        |
| Old content removed             | Do not use `"w"` if you need to keep old data |
| File left open                  | Use `with open(...)`                          |
| Large file uses too much memory | Loop through the file instead of `read()`     |


