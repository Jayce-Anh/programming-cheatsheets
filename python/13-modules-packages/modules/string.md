# Standard library: `string`

The [string](https://docs.python.org/3/library/string.html) module provides **ready-made character sets** (letters, digits, punctuation) and helpers like **`Formatter`** and **`Template`**. It does **not** replace normal `str` methods — use it when you need **constants** or **simple `$placeholders`**.

## When to use

- Validate input: “only letters”, “only digits”, etc.
- Build allowed character sets for passwords or tokens
- Use **`string.Template`** for safe, simple substitution (e.g. mail templates)
- **`string.Formatter`** — advanced; most code uses **f-strings** instead

## Import

```python
import string
```

## Quick prints

```python
import string

# All ASCII lowercase letters
print(string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz

# All ASCII punctuation
print(string.punctuation)       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

## Constants (most used)

| Name | Contents |
|------|----------|
| `ascii_letters` | `a-z` and `A-Z` |
| `ascii_lowercase` | `a-z` |
| `ascii_uppercase` | `A-Z` |
| `digits` | `0-9` |
| `hexdigits` | `0-9`, `a-f`, `A-F` |
| `octdigits` | `0-7` |
| `punctuation` | Standard ASCII punctuation characters |
| `whitespace` | space, tab, newline, etc. |
| `printable` | letters + digits + punctuation + whitespace |

```python
import string

allowed = string.ascii_letters + string.digits
all(c in allowed for c in user_input)   # True if only letters/digits
```

## `string.Template` (optional)

```python
from string import Template
t = Template("Hello, $name!")
t.substitute(name="Jayce")    # "Hello, Jayce!"
# t.safe_substitute(name="Jayce")  # missing keys → left as $key
```

## Note

- **`str`** type docs (methods like `.split()`, `.strip()`) → [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- For complex patterns, use the **`re`** module

[Official docs: string](https://docs.python.org/3/library/string.html)
