# Standard library: `sys`

The [sys](https://docs.python.org/3/library/sys.html) module exposes **the running Python interpreter**: command-line arguments, exit codes, standard streams, import path, and version info.

## When to use

- Read **CLI arguments** (`python script.py arg1 arg2`)
- **Exit** the program with a status code
- Adjust **`sys.path`** so Python finds your modules (usually avoid; prefer packages / venv)
- Print debug info: **Python version**, **platform**, **executable** path

## Import

```python
import sys
```

## Command line & exit

```python
sys.argv              # list: script path + arguments, e.g. ['main.py', 'foo']
sys.argv[1]           # first user argument (IndexError if missing — check len)

sys.exit(0)           # success (optional in scripts)
sys.exit(1)           # error (convention)
```

## Streams

```python
sys.stdout.write("hi\n")    # like print without extra features
sys.stderr.write("error\n") # errors / diagnostics
line = sys.stdin.readline() # rare in scripts; use input() for interactive
```

## Interpreter info

```python
sys.version           # long version string
sys.version_info      # (major, minor, micro, releaselevel, serial)
sys.platform          # e.g. 'darwin', 'linux', 'win32'
sys.executable        # path to python binary
```

## Import path

```python
sys.path              # list of dirs searched for imports
# sys.path.insert(0, "/custom")  # use only when you know why (testing / legacy)
```

## Best practices

- Prefer **`argparse`** for real CLIs instead of parsing `sys.argv` by hand
- Use **`logging`** to file instead of only `print` / `stdout` for apps
- Avoid changing **`sys.path`** in libraries — fix package layout instead

[Official docs: sys](https://docs.python.org/3/library/sys.html)
