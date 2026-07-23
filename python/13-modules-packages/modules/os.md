# Standard library: `os`

The [os](https://docs.python.org/3/library/os.html) module talks to the **operating system**: working directory, environment variables, and file/folder operations. Use [os.path](https://docs.python.org/3/library/os.path.html) for portable path strings (or prefer [pathlib](https://docs.python.org/3/library/pathlib.html) for new code).

## When to use

- Change or read the **current working directory**
- List/create/remove **directories** and **files**
- Read **environment variables** (`PATH`, API keys, config)
- Build paths that work on **Windows and Unix** (`os.path.join`)

## Import

```python
import os
```

## Working directory

```python
os.getcwd()           # current folder (str)
os.chdir("/tmp")      # change cwd (path must exist); returns None
print("Current working directory:", os.getcwd())
```

## Environment

```python
os.environ                       # current evirontment variables
os.environ.get("HOME")           # or os.environ["HOME"] — KeyError if missing
os.getenv("PATH", default="")    # safe get with default
# os.environ["KEY"] = "value"    # set for child processes only (this process)

# Note: spelling is environ (not "eviron")
print("Environment variables:", os.environ)   # full mapping — can be large; avoid logging in production
print("PATH:", os.environ.get("PATH"))
```

## List & walk

```python
os.listdir(".")                  # names in folder (not full paths)
os.walk("myproject")             # (dirpath, dirnames, filenames) — recurse
```

## Files & directories

```python
os.mkdir("new_folder")           # one level; fails if exists
os.makedirs("a/b/c", exist_ok=True)   # nested dirs

os.remove("file.txt")            # delete file (same as os.unlink)
os.rmdir("empty_folder")         # folder must be empty

os.rename("old.txt", "new.txt")
```

## `os.path` (common)

```python
os.path.join("data", "out", "x.csv")   # "data/out/x.csv" (correct separators)
os.path.abspath("rel/path")            # absolute path
os.path.basename("/a/b/file.txt")      # "file.txt"
os.path.dirname("/a/b/file.txt")       # "/a/b"
os.path.exists("readme.md")
os.path.isfile("readme.md")
os.path.isdir("src")
os.path.splitext("photo.jpg")          # ("photo", ".jpg")
```

## Best practices

- Prefer **`os.getenv("KEY")`** over raw `os.environ["KEY"]` when the key may be missing
- For new projects, consider **`pathlib.Path`** instead of string paths
- Avoid **`os.system()`** — use **`subprocess`** for running shell commands

[Official docs: os](https://docs.python.org/3/library/os.html) · [os.path](https://docs.python.org/3/library/os.path.html)
