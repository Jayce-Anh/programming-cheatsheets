# 13. MODULES & PACKAGES

A **module** is a `.py` file with functions, classes, and variables you can reuse. A **package** is a folder of modules (often with `__init__.py`) that groups related code.

## Best Practices

- Prefer `import module` and use `module.name` — keeps namespaces clear
- Use `from module import item` only for short, well-known names
- Pin versions in `requirements.txt` for reproducible installs
- Put reusable code in modules; keep scripts thin
- Use `if __name__ == "__main__":` for code that should run only when the file is executed directly

## Syntax:

```python
# Modules
import module_name
import module_name as alias
from module_name import item
from module_name import item1, item2
from module_name import *                    # avoid — pollutes namespace

# Package / submodule
import package.submodule
import package as alias
from package.submodule import function_name
```

- `import`: loads the module; access members with `module.member`
- `from ... import`: brings specific names into the current namespace
- `as`: renames the imported module or symbol

## Examples

```python
# Modules
import math                   
math.sqrt(16)                 # 4.0
math.pi                       # 3.14159...

import random
random.randint(1, 6)          # random int 1–6
random.choice(["a", "b"])     # pick one item

from datetime import datetime
datetime.now()                # current date-time

import os
os.getcwd()                   # current working directory
os.path.join("a", "b.txt")    # cross-platform path

import sys
sys.argv                      # command-line arguments (list)

import string
string.ascii_letters          # 'abc...xyzABC...XYZ' — all letters
string.digits                 # '0123456789'
string.punctuation            # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
string.hexdigits              # 0-9, a-f, A-F (for hex literals)

# Packages
import pandas as pd                 # Import pandas package as pd
sales_df = pd.DataFrame(sales)      # Convert sales to a pandas DataFrame
print(sales_df.head(5))             # Preview the first five rows
sales_df = pd.read_csv("sales.csv") # Read in sales.csv
print(sales_df.info())              # Display the DataFrame info
```

### Common standard library modules

| Module | Purpose | Example |
|--------|---------|---------|
| [math](https://docs.python.org/3/library/math.html) | Math functions & constants | `math.sqrt(16)`, `math.pi` |
| [random](https://docs.python.org/3/library/random.html) | Random numbers & sampling | `random.randint(1, 6)`, `random.choice(seq)` |
| [datetime](https://docs.python.org/3/library/datetime.html) | Dates & times | `from datetime import datetime` → `datetime.now()` |
| [os](https://docs.python.org/3/library/os.html) | OS paths & env | `os.getcwd()`, `os.path.join("a", "b.txt")` |
| [sys](https://docs.python.org/3/library/sys.html) | Interpreter & CLI | `sys.argv`, `sys.exit(0)` |
| [string](https://docs.python.org/3/library/string.html) | String constants | `string.ascii_letters`, `string.digits` |
| [re](https://docs.python.org/3/library/re.html) | Regular expressions | `re.findall(r"\d+", text)` |
| [json](https://docs.python.org/3/library/json.html) | JSON read/write | `json.loads(s)`, `json.dumps(obj)` |
| [csv](https://docs.python.org/3/library/csv.html) | CSV files | `csv.reader(open("f.csv"))` |
| [pathlib](https://docs.python.org/3/library/pathlib.html) | Paths as objects | `from pathlib import Path` → `Path("a") / "b.txt"` |
| [collections](https://docs.python.org/3/library/collections.html) | Extra containers | `defaultdict`, `Counter`, `namedtuple` |
| [itertools](https://docs.python.org/3/library/itertools.html) | Iterator tools | `itertools.chain`, `combinations` |

### Module notes

Short guides for commonly used standard library modules:

- [math](./modules/math.md) — trig, roots, `pi` / `e`, `gcd`, `factorial`
- [os](./modules/os.md) — cwd, env vars, files/dirs, `os.path`
- [sys](./modules/sys.md) — `argv`, `exit`, streams, version / platform
- [string](./modules/string.md) — character-set constants, `Template`

## Create your module

**File `helpers.py`:**

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Runs only when you execute: python helpers.py
    print(greet("World"))
```

**Another file:**

```python
import helpers
helpers.greet("Jayce")

from helpers import greet
greet("Jayce")
```

## Packages (folder layout)

```
myproject/
  mypackage/
    __init__.py      # optional in Python 3.3+ (namespace packages); often used for exports
    core.py
    utils.py
```

```python
from mypackage import core
from mypackage.utils import helper
```

## Installing Third-Party Packages

| Command | Purpose |
|---------|---------|
| `pip install package` | Install a package from PyPI |
| `pip install -r requirements.txt` | Install all listed packages |
| `pip uninstall package` | Remove a package |
| `pip list` | Show installed packages |
| `pip show package` | Show version, dependencies, location |
| `python -m pip install package` | Use pip for the current Python (recommended if `pip` is ambiguous) |

```bash
pip install requests
pip install -r requirements.txt
```

**`requirements.txt` example:**

```
requests>=2.28.0
numpy==1.24.0
```

```python
# After pip install requests
import requests
response = requests.get("https://example.com")
```

## Relative Imports (inside a package)

```python
from . import sibling_module          # same package
from ..parent_pkg import something    # parent package
```

Use these only inside a package context (not in a top-level script you run directly).

---

## Common Pitfalls

| Issue | Tip |
|-------|-----|
| `ModuleNotFoundError` | Check `pip install`, virtual env, and `PYTHONPATH` |
| Circular imports | Move shared code to a third module or lazy-import inside a function |
| Name clashes | Use `import module` + `module.name` instead of `from x import *` |
