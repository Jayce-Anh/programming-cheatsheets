# Standard library: `math`

The [math](https://docs.python.org/3/library/math.html) module provides **floating-point math** (trig, logs, rounding helpers) and constants like **`pi`** and **`e`**. For integers / combinatorics, see also **`random`**, **`statistics`**, **`fractions`**.

## When to use

- Powers, square roots, trig, logarithms
- Floor/ceil, gcd, factorial (integers)
- Constants **`math.pi`**, **`math.e`**

## Import

```python
import math
```

## Common functions

```python
math.sqrt(16)         # 4.0
math.pow(2, 3)        # 8.0  (float); for ints often use ** 
math.floor(3.9)       # 3
math.ceil(3.1)        # 4
math.trunc(-3.9)      # -3  (toward zero)

math.log(10)          # natural log
math.log(100, 10)     # log base 10
math.exp(1)           # e ** 1

math.sin(math.pi / 2) # 1.0 (radians)
math.degrees(math.pi) # 180.0
math.radians(180)     # pi

math.gcd(48, 18)      # 6
math.factorial(5)     # 120
math.isclose(a, b)    # float comparison
```

## Constants

```python
math.pi
math.e
math.inf
math.nan
```

## Best practices

- **`math.sqrt`** expects a non-negative real (or use **`cmath`** for complex)
- For **money**, prefer **`decimal.Decimal`**, not `float`
- **`statistics`** module for mean, median, stdev, etc.

[Official docs: math](https://docs.python.org/3/library/math.html)
