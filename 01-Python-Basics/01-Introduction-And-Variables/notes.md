# 📝 Study Notes: Introduction & Variables

---

# 🏢 Module 1: Introduction to Python

## Core Characteristics

* **Popularity:** Python is currently the most popular programming language due to its simplicity, readability, and ease of use.
* **Versatility:** Used for everything from simple automation scripts to large-scale, industrial-level applications.

## Key Industry Fields & Tools

### 📊 Data Science & Machine Learning

* **Data Analysis:** `Pandas` and `NumPy` make data analysis less tedious.
* **AI/Machine Learning:** `TensorFlow` and `Scikit-learn` make AI models highly accessible.

### 🌐 Web Development (Back-End Systems)

* Frameworks like `Django`, `FastAPI`, and `Flask` allow developers to build secure, scalable backends with minimal effort.

### 🛡️ Cybersecurity & Ethical Hacking

* Used to detect malware and viruses.
* Build automated security scans.
* Analyze active network threats.

### ⚙️ DevOps & System Administration

* Writing CI/CD infrastructure pipelines.
* Server monitoring.
* Automated log management.

### 🤖 Embedded Systems & IoT

* Runs exceptionally well on microcomputers like the **Raspberry Pi** and MicroPython-compatible boards.

### 🚀 Automation & Web Scraping

* Tools like `Selenium` and `BeautifulSoup` allow users to scrape public data and automate repetitive browser tasks.

---

# 🛠️ Module 2: Understanding Variables and Data Types

## 📦 Variable Declaration

* Python variables act as **labeled boxes** for storing data references.
* **Syntax:** `variable_name = value`

  * No keywords like `let`, `const`, or `var` are used.
* **Example:**

```python
age = 25
```

---

## 🛑 Strict Variable Naming Rules

Breaking these causes a `SyntaxError`.

1. Must start only with a letter or an underscore (`_`).
2. Cannot start with a number.
3. Can only contain:

   * Letters (`a-z`, `A-Z`)
   * Numbers (`0-9`)
   * Underscores (`_`)
4. Variables are case-sensitive.

```python
age
Age
AGE
```

These are three different variables.

5. Cannot use Python reserved keywords such as:

```python
if
class
def
```

---

## 🐍 Naming Conventions (Best Practices)

### Snake Case

Multi-word variables should use lowercase letters separated by underscores.

```python
my_variable_name
```

### Descriptive Names

Use meaningful variable names.

```python
user_age = 30
```

### Avoid Single Letters

Avoid unclear names such as:

```python
x = 56
```

Instead, use descriptive alternatives.

---

## 💬 Code Comments

Comments begin with the pound symbol (`#`).

```python
# This is a comment
```

Python ignores everything after the `#` on that line.

### Multi-Line Comments

```python
# First comment line
# Second comment line
# Third comment line
```

### Rule of Thumb

Use comments to explain complex logic, not poorly named variables.

---

## 🖨️ How the `print()` Function Works

### Purpose

Outputs data directly to the terminal console.

### Strings

Text must be enclosed in quotes.

```python
print("Hello")
print('Hello')
```

### Multiple Arguments

```python
print("Age:", 25)
```

Output:

```text
Age: 25
```

Python automatically inserts a single space between arguments.

---

## 🔄 Dynamic vs. Static Typing

### Python is Dynamically Typed

Python automatically determines the data type during runtime.

```python
name = "John"
age = 25
```

No explicit type declaration is required.

### Error Detection

* **Statically Typed Languages:** Check types before execution.
* **Python:** Checks types while executing code.

As a result, type-related bugs only appear when the problematic line is executed.

---

## 🗂️ Core Python Data Types

| Data Type               | Description                              | Example Code                   |
| ----------------------- | ---------------------------------------- | ------------------------------ |
| **Integer (`int`)**     | Whole numbers without decimals.          | `my_int = 10`                  |
| **Float (`float`)**     | Numbers with decimal points.             | `my_float = 4.51`              |
| **String (`str`)**      | Text enclosed in quotes.                 | `my_str = 'hello'`             |
| **Boolean (`bool`)**    | `True` or `False`.                       | `my_bool = True`               |
| **List (`list`)**       | Ordered, mutable collection.             | `my_list = [22, 'text', 3.14]` |
| **Tuple (`tuple`)**     | Ordered, immutable collection.           | `my_tuple = (7, 'hello', 8.5)` |
| **Set (`set`)**         | Unordered collection of unique elements. | `my_set = {7, 'hello', 8.5}`   |
| **Dictionary (`dict`)** | Key-value pairs.                         | `my_dict = {'name': 'Alice'}`  |
| **Range (`range`)**     | Sequence of generated numbers.           | `my_range = range(5)`          |
| **NoneType (`None`)**   | Represents the absence of a value.       | `my_none = None`               |

---

## 🔍 Type Inspection & Verification

### 1. The `type()` Function

**Purpose:** Returns the exact data type of an object.

```python
type('Devin')
```

Output:

```python
<class 'str'>
```

```python
type(None)
```

Output:

```python
<class 'NoneType'>
```

**Note:** `type()` requires exactly one argument.

---

### 2. The `isinstance()` Function

**Purpose:** Checks whether an object belongs to a specific data type.

**Syntax:**

```python
isinstance(object, class_or_tuple)
```

### Defensive Coding Example

```python
account_balance = '12'

isinstance(account_balance, int)
```

Output:

```python
False
```

This helps prevent runtime errors.

### Multi-Type Check

```python
account_balance = 12

isinstance(account_balance, (int, float))
```

Output:

```python
True
```

---

# 🧵 Module 3: Introduction to Strings

## 📝 Core Mechanics & Anatomy

### Enclosure

Single and double quotes are treated equally.

```python
'Hello'
"Hello"
```

### Multiline Strings

```python
"""
This is a
multiline string.
"""
```

### Escape Characters

```python
'It\'s a sunny day'
```

### Membership Testing

```python
"sun" in "sunny day"
```

Output:

```python
True
```

### Length Assessment

```python
len("Python")
```

Output:

```python
6
```

---

## 📊 Indexing & Slicing Mechanics

### Zero-Based Indexing

```python
word = "Python"

word[0]
```

Output:

```python
'P'
```

### Negative Indexing

```python
word[-1]
```

Output:

```python
'n'
```

### String Slicing

**Syntax:**

```python
string[start:stop:step]
```

Example:

```python
word = "Python"

word[0:3]
```

Output:

```python
'Pyt'
```

### Non-Inclusive Stop Index

The stop index is excluded.

```python
word[0:3]
```

Includes indexes:

```text
0, 1, 2
```

### Default Values

```python
word[:3]
word[2:]
```

### Reverse a String

```python
word[::-1]
```

Output:

```python
'nohtyP'
```

---

## 🛑 Object Immutability

Strings are immutable.

### Reassignment (Allowed)

```python
greeting = 'hi'
greeting = 'hello'
```

### Direct Modification (Not Allowed)

```python
greeting[0] = 'H'
```

Output:

```python
TypeError
```

---

## ➕ Concatenation & Interpolation

### Concatenation (`+`)

```python
first = "Hello"
second = "World"

first + " " + second
```

Output:

```python
Hello World
```

### Explicit Type Conversion

```python
"Age: " + str(25)
```

### Augmented Assignment (`+=`)

```python
message = "Hello"
message += " World"
```

### String Interpolation (F-Strings)

```python
f"Total sum: {5 + 10}"
```

Output:

```python
Total sum: 15
```

---

## 🧰 Built-in Diagnostic & Manipulation Methods

Because strings are immutable, every modification method returns a new string.

| Method                 | Behavior                                     | Example Output                         |
| ---------------------- | -------------------------------------------- | -------------------------------------- |
| `upper()`              | Converts all letters to uppercase.           | `'hi'.upper()` → `'HI'`                |
| `lower()`              | Converts all letters to lowercase.           | `'HI'.lower()` → `'hi'`                |
| `strip()`              | Removes leading and trailing whitespace.     | `' x '.strip()` → `'x'`                |
| `replace(old, new)`    | Replaces occurrences of a substring.         | `'hi'.replace('h', 'b')` → `'bi'`      |
| `split(separator)`     | Splits a string into a list.                 | `'a b'.split()` → `['a', 'b']`         |
| `separator.join(list)` | Joins a list into a string.                  | `' '.join(['a', 'b'])` → `'a b'`       |
| `startswith(prefix)`   | Checks starting characters.                  | `'hi'.startswith('h')` → `True`        |
| `endswith(suffix)`     | Checks ending characters.                    | `'hi'.endswith('i')` → `True`          |
| `find(substring)`      | Returns first matching index.                | `'hi'.find('i')` → `1`                 |
| `count(substring)`     | Counts occurrences.                          | `'hi'.count('h')` → `1`                |
| `capitalize()`         | Capitalizes first character only.            | `'hi yall'.capitalize()` → `'Hi yall'` |
| `title()`              | Capitalizes each word.                       | `'hi yall'.title()` → `'Hi Yall'`      |
| `isupper()`            | Returns `True` if all letters are uppercase. | `'HI'.isupper()` → `True`              |
| `islower()`            | Returns `True` if all letters are lowercase. | `'HI'.islower()` → `False`             |

---

# 📌 Key Takeaways

* Python is simple, readable, and highly versatile.
* Variables are dynamically typed and require no explicit type declaration.
* Use descriptive snake_case variable names.
* Strings are immutable objects.
* String slicing uses non-inclusive stop indexes.
* F-strings are the preferred method for formatting output.
* `type()` identifies an object's exact type.
* `isinstance()` safely validates data types before operations.
* Built-in string methods simplify text manipulation while preserving immutability.

---

## 🔢 Module 4: Numbers & Mathematical Operations

### ⚖️ Core Numeric Data Types
* **Integer (`int`):** Positive or negative whole numbers without decimal points (e.g., `-4`, `56`).
* **Floating-Point (`float`):** Numbers containing explicit decimal indicators (e.g., `0.0`, `-12.0`, `3.14`).
* **Implicit Float Casting:** Whenever an operation mixes an `int` and a `float`, Python automatically promotes the result to a `float`.
  * *Example:* `56 + 5.4` $\rightarrow$ `61.4` (Type: `<class 'float'>`)

### 🧮 Advanced Arithmetic Operators
| Operator | Operation | Description / Behavior | Example |
|:---:|:---|:---|:---|
| `/` | **True Division** | Always outputs a float, even if the division is perfectly even. | `56 / 12` $\rightarrow$ `4.666...` |
| `//` | **Floor Division**| Divides numbers and drops the fraction, returning the greatest integer less than or equal to the result. | `56 // 12` $\rightarrow$ `4`<br>`12.0 // 5.4` $\rightarrow$ `2.0` |
| `%` | **Modulo** | Extracts the fractional arithmetic remainder left over after a division operation. | `56 % 12` $\rightarrow$ `8` |
| `**` | **Exponentiation**| Raises the left operand to the power of the right operand. | `2 ** 3` $\rightarrow$ `8` |

### ⚠️ Floating-Point Precision Constraints (Floating-Point Arithmetic)
* **The Problem:** Operations like `0.1 + 0.2` output `0.30000000000000004` instead of an exact `0.3`.
* **The Cause:** 
  Computers process calculations using base-2 binary structures. Fractional values that cleanly divide in base-10 (like $1/10$ or $1/5$) turn into repeating, infinite fractions in binary, forcing a microscopic rounding adjustment.

### 🔧 Native Conversion & Core Math Functions
* `int(value)`: Truncates a float toward zero (drops the decimal point completely without rounding). Converts numeric text strings like `'45'` into integers.
* `float(value)`: Appends `.0` to integers. Parses float-format strings like `'7.8'` into usable values.
* `round(number, digits)`: Rounds to the nearest whole integer by default. If a precision argument is added, it limits trailing decimals (`round(4.253, 1)` $\rightarrow$ `4.3`).
* `abs(number)`: Drops directional signage, delivering the absolute structural distance from zero (`abs(-15)` $\rightarrow$ `15`).
* `pow(base, exp, mod)`: `pow(2, 3)` matches `2 ** 3`. Adding a third argument performs accelerated modular exponentiation: `pow(2, 3, 5)` $\rightarrow$ $(2^3) \pmod 5 = 3$.

---

# ⚡ Module 5: Augmented Assignment Syntax

## 🧩 Structural Purpose

* A syntactic shortcut that performs a calculation and assigns the result back to the original variable.
* **Syntax conversion:**

```python
x += y
```

is equivalent to

```python
x = x + y
```

* **Benefit:** Reduces repetition, minimizes typing mistakes, and improves readability.

---

## 🎛️ Operator Reference Grid

| Assignment | Equivalent       | Example (`x = 10`) |
| ---------- | ---------------- | ------------------ |
| `+=`       | `x = x + value`  | `x += 5` → `15`    |
| `-=`       | `x = x - value`  | `x -= 3` → `7`     |
| `*=`       | `x = x * value`  | `x *= 2` → `20`    |
| `/=`       | `x = x / value`  | `x /= 4` → `2.5`   |
| `//=`      | `x = x // value` | `x //= 3` → `3`    |
| `%=`       | `x = x % value`  | `x %= 3` → `1`     |
| `**=`      | `x = x ** value` | `x **= 2` → `100`  |

---

## 🧵 String Behavior Compatibility

### Concatenation (`+=`)

Extends a string by creating a new string object (strings are immutable).

```python
greeting = "Hello"
greeting += " World"

print(greeting)
```

Output:

```text
Hello World
```

### String Multiplication (`*=`)

Repeats a string multiple times.

```python
greet = "Hi"
greet *= 3

print(greet)
```

Output:

```text
HiHiHi
```

Attempting to use other arithmetic assignment operators on strings (`-=`, `/=`, `//=`, etc.) raises a `TypeError`.

---

## 🛑 The `++` and `--` Myth in Python

Unlike C, C++, Java, or JavaScript, Python **does not** support increment (`++`) or decrement (`--`) operators.

The following code is invalid:

```python
x++
```

or

```python
x--
```

Python raises a **SyntaxError**.

### Unary Plus Behavior

Interestingly, multiple plus signs are legal syntax because Python interprets them as repeated unary positive operators.

```python
x = 5

++x
+++x
```

Output:

```text
5
5
```

The value **does not change**.

### Correct Way to Increment

```python
x += 1
```

or

```python
x = x + 1
```

### Correct Way to Decrement

```python
x -= 1
```

or

```python
x = x - 1
```

---

# 📌 Key Takeaways

* Augmented assignment combines an operation and assignment into one statement.
* Strings support only `+=` and `*=`.
* Other augmented arithmetic operators are invalid for strings.
* Python does **not** have `++` or `--` operators.
* Use `+= 1` and `-= 1` to increment or decrement values.
