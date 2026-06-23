# 📝 Study Notes: Introduction & Variables

## 🏢 Module 1: Introduction to Python

### Core Characteristics
* **Popularity:** It is currently the most popular programming language due to its simplicity, readability, and ease of use.
* **Versatility:** Used for everything from simple automation scripts to large-scale, industrial-level applications.

### Key Industry Fields & Tools
* 📊 **Data Science & Machine Learning:**
  * *Data Analysis:* **Pandas** and **NumPy** make data analysis less tedious.
  * *AI/Machine Learning:* **TensorFlow** and **Scikit-learn** make AI models highly accessible.
* 🌐 **Web Development (Back-End Systems):**
  * Frameworks like **Django**, **FastAPI**, and **Flask** allow developers to build secure, scalable backends with minimal effort.
* 🛡️ **Cybersecurity & Ethical Hacking:**
  * Used to detect malware/viruses, build automated security scans, and analyze active network threats.
* ⚙️ **DevOps & System Administration:**
  * Used for writing CI/CD infrastructure pipelines, server monitoring, and automated log management.
* 🤖 **Embedded Systems & IoT:**
  * Runs exceptionally well on microcomputers like the **Raspberry Pi** and MicroPython-compatible boards.
* 🚀 **Automation & Web Scraping:**
  * Tools like **Selenium** and **BeautifulSoup** allow users to scrape public data and automate repetitive browser tasks.

---

## 🛠️ Module 2: Understanding Variables and Data Types

### 📦 Variable Declaration
* Python variables act as **labeled boxes** for storing data references.
* **Syntax:** `variable_name = value` (No keywords like `let`, `const`, or `var` are used).
* **Example:** `age = 25`

### 🛑 Strict Variable Naming Rules (Breaking these causes a `SyntaxError`)
1. Must start **only** with a letter or an underscore (`_`). It **cannot** start with a number.
2. Can only contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and underscores.
3. Are strictly **case-sensitive** (`age`, `Age`, and `AGE` are three completely unique variables).
4. Cannot be a Python **reserved keyword** (like `if`, `class`, or `def`).

### 🐍 Naming Conventions (Best Practices)
* **Snake Case:** Multi-word variables should be lowercase and separated by underscores (`my_variable_name`).
* **Descriptive Names:** Always use intentional names instead of abbreviations (`user_age = 30`).
* **Avoid Single Letters:** Do not use names like `x = 56` because they fail to communicate purpose.

### 💬 Code Comments
* Comments start with a pound symbol (`#`). Python ignores everything after the `#` on that line.
* Multi-line comments are built using consecutive lines of single comments.
* **Rule of Thumb:** Use comments to explain complex logic, *never* to explain a poorly named variable.

### 🖨️ How the `print()` Function Works
* **Purpose:** A built-in function used to output data directly to the terminal console stream.
* **Strings:** Text arguments must be wrapped in matching quotation marks (`'` or `"`).
* **Multiple Arguments:** You can pass multiple values separated by commas. Python automatically inserts a **single empty space** (` `) between each item.

### 🔄 Dynamic vs. Static Typing
* **Python is Dynamically Typed:** You do not explicitly declare variable types. Python automatically determines the data type at **runtime** based on the value assigned to it.
* **Catching Errors:** Statically-typed languages check types during a compile step before running. Because Python evaluates types line-by-line during execution, type-related bugs will only reveal themselves when that specific line of code is run.

### 🗂️ Core Python Data Types
| Data Type | Description | Example Code |
|:---|:---|:---|
| **Integer (`int`)** | A whole number without decimals (positive or negative). | `my_int = 10` |
| **Float (`float`)** | A number containing a decimal point. | `my_float = 4.51` |
| **String (`str`)** | A sequence of text characters wrapped in quotes. | `my_str = 'hello'` |
| **Boolean (`bool`)**| A binary logic state evaluating to `True` or `False`. | `my_bool = True` |
| **List (`list`)** | An ordered, mutable collection of elements. | `my_list = [22, 'text', 3.14]` |
| **Tuple (`tuple`)** | An ordered, **immutable** (unchangeable) collection. | `my_tuple = (7, 'hello', 8.5)` |
| **Set (`set`)** | An unordered collection of **unique** elements. | `my_set = {7, 'hello', 8.5}` |
| **Dictionary (`dict`)**| A collection of custom key-value pairs wrapped in `{}`. | `my_dict = {'name': 'Alice'}` |
| **Range (`range`)** | A sequence of numbers generated typically for loops. | `my_range = range(5)` |
| **NoneType (`None`)**| A special value representing the absence of a value. | `my_none = None` |

### 🔍 Type Inspection & Verification (`type()` vs `isinstance()`)

#### 1. The `type()` Function
* **Purpose:** Returns the exact data type/class of the passed object.
* **Requirement:** Must take exactly **1 argument** (running `type()` empty throws a `TypeError`).
* **Terminal Outputs:**
  * `type('Devin')` $\rightarrow$ `<class 'str'>`
  * `type(None)` $\rightarrow$ `<class 'NoneType'>`

#### 2. The `isinstance()` Function
* **Purpose:** Checks if an object matches a specific data type and returns a boolean (`True` or `False`).
* **Syntax:** `isinstance(object, class_or_tuple)`
* **Defensive Coding:** Essential for preventing run-time execution errors. For example, trying to divide a string string `account_balance = '12'` by an integer crashes the program with a `TypeError`. Checking it first prevents this:
  ```python
  account_balance = '12'
  isinstance(account_balance, int)  # Returns False (Safe to handle before a crash occurs)
* **Multi-Type Check:** You can pass a tuple of multiple types to check if an object matches any of them.
  ```python
  account_balance = 12
  isinstance(account_balance, (int, float))  # Returns True (Matches int)