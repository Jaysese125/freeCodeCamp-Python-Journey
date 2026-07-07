# 🔄 Study Notes: Loops and Sequences

## 1. Core Mechanics of Python Lists

* **Definition:** A **list** is an ordered, mutable collection of items enclosed in square brackets `[]`. A list can contain elements of different data types.

* **Zero-Based Indexing:** The first element has an index of `0`. Negative indices access elements from the end of the list, where `-1` refers to the last element.

---

## 2. Common List Operations

### Accessing Elements

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])   # apple
print(fruits[-1])  # orange
```

Attempting to access an index outside the list raises an `IndexError`.

### Modifying Elements

```python
fruits[1] = "grape"
```

Lists are **mutable**, meaning their elements can be changed after creation.

### Removing Elements

```python
del fruits[0]
```

The `del` statement removes an element by index. Attempting to delete an index that does not exist raises an `IndexError`.

### Unpacking

List unpacking assigns elements directly to variables.

```python
name, age, job = ["Alice", 34, "Developer"]
```

Use `*` to collect the remaining elements into a new list.

```python
name, *remaining = ["Alice", 34, "Developer"]

print(name)       # Alice
print(remaining)  # [34, "Developer"]
```

### Slicing

General syntax:

```python
sequence[start:stop:step]
```

Where:

* `start` → starting index (inclusive)
* `stop` → ending index (exclusive)
* `step` → interval between elements

Examples:

```python
numbers = [0, 1, 2, 3, 4, 5]

numbers[1:4]   # [1, 2, 3]
numbers[:3]    # [0, 1, 2]
numbers[3:]    # [3, 4, 5]
numbers[::2]   # [0, 2, 4]
numbers[::-1]  # [5, 4, 3, 2, 1, 0]
```

---

## 3. Essential Python List Methods

| Method / Function                           | Returns      | Description                                                                                                            |
| ------------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| `list.append(item)`                         | `None`       | Adds a single item to the end of the list.                                                                             |
| `list.extend(iterable)`                     | `None`       | Appends every element from an iterable to the list.                                                                    |
| `list.insert(index, item)`                  | `None`       | Inserts an item before the specified index.                                                                            |
| `list.remove(value)`                        | `None`       | Removes the first matching value. Raises `ValueError` if the value is not found.                                       |
| `list.pop(index=-1)`                        | Removed item | Removes and returns the element at the specified index (last by default). Raises `IndexError` if the index is invalid. |
| `list.clear()`                              | `None`       | Removes all elements from the list.                                                                                    |
| `list.sort(key=None, reverse=False)`        | `None`       | Sorts the list in place.                                                                                               |
| `sorted(iterable, key=None, reverse=False)` | New list     | Returns a new sorted list without modifying the original iterable.                                                     |
| `list.reverse()`                            | `None`       | Reverses the list in place.                                                                                            |
| `list.index(value)`                         | Index        | Returns the index of the first occurrence. Raises `ValueError` if the value is not found.                              |
| `list.count(value)`                         | Count        | Returns the number of times a value appears in the list.                                                               |
| `list.copy()`                               | New list     | Returns a shallow copy of the list.                                                                                    |
| `len(list)`                                 | Integer      | Returns the number of elements in the list.                                                                            |

---

## 4. `append()` vs `extend()`

```python
numbers = [1, 2]

numbers.append([3, 4])
print(numbers)
# [1, 2, [3, 4]]

numbers = [1, 2]

numbers.extend([3, 4])
print(numbers)
# [1, 2, 3, 4]
```

**Key Difference**

* `append()` adds the entire object as a single element.
* `extend()` adds each element from an iterable individually.

---

## 5. In-Place Methods vs Functions That Return a New Object

### In-Place Methods

These modify the original list and return `None`.

```python
numbers.sort()
numbers.reverse()
numbers.append(5)
```

### Functions That Return a New Object

These leave the original list unchanged.

```python
new_numbers = sorted(numbers)
```

Remember:

* `append()`, `extend()`, `insert()`, `remove()`, `sort()`, `reverse()`, and `clear()` modify the original list and return `None`.
* `sorted()` returns a new sorted list.

---

## 6. Understanding Python Tuples `()`

### Definition

A **tuple** is an ordered, **immutable** sequence enclosed in parentheses `()`. Like lists, tuples can store multiple data types.

```python
person = ("Alice", 25, "Developer")
```

### Immutability

Once created, a tuple cannot be modified.

```python
person = ("Alice", 25)

person[0] = "Bob"
# TypeError: 'tuple' object does not support item assignment
```

Elements cannot be added, removed, or reassigned.

### Accessing Elements

Tuples support indexing just like lists.

```python
numbers = (10, 20, 30)

print(numbers[0])   # 10
print(numbers[-1])  # 30
```

### Slicing

Tuple slicing follows the same syntax as list slicing and returns a **new tuple**.

```python
numbers = (0, 1, 2, 3, 4)

numbers[1:4]
# (1, 2, 3)

numbers[::-1]
# (4, 3, 2, 1, 0)
```

### Unpacking

Tuple unpacking works exactly like list unpacking.

```python
name, age, job = ("Alice", 34, "Developer")

name, *remaining = ("Alice", 34, "Developer")

print(name)
# Alice

print(remaining)
# [34, "Developer"]
```

> **Note:** Using `*` during unpacking always stores the remaining values in a **list**, even when unpacking a tuple.

### Tuple Methods

| Method                                | Returns  | Description                                                                               |
| ------------------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `tuple.count(value)`                  | Integer  | Returns the number of occurrences of a value.                                             |
| `tuple.index(value[, start[, stop]])` | Index    | Returns the index of the first occurrence. Raises `ValueError` if the value is not found. |
| `len(tuple)`                          | Integer  | Returns the number of elements.                                                           |
| `sorted(tuple)`                       | New list | Returns a new sorted **list** without modifying the original tuple.                       |

### Lists vs Tuples

| Feature           | List                | Tuple                              |
| ----------------- | ------------------- | ---------------------------------- |
| Syntax            | `[]`                | `()`                               |
| Mutable           | ✅ Yes               | ❌ No                               |
| Ordered           | ✅ Yes               | ✅ Yes                              |
| Supports Indexing | ✅                   | ✅                                  |
| Supports Slicing  | ✅                   | ✅                                  |
| Can Be Modified   | ✅                   | ❌                                  |
| Common Use        | Dynamic collections | Fixed collections / read-only data |

---

## 7. Control Flow: Loops and Iteration

### For Loops vs While Loops
* **`for` Loop:** Natively designed for definite iteration. It traverses an entire iterable sequence (lists, tuples, strings) element by element until exhausted.
* **`while` Loop:** Designed for indefinite iteration. It continuously runs a block of code based on a conditional statement, repeating until that predicate evaluates to `False`.

### Loop Jump Statements
* **`break`:** Instantly terminates the inner loop scope completely, shifting program execution to the immediate next line outside the loop block.
* **`continue`:** Short-circuits the rest of the current block iteration code, jumping directly back up to evaluate the next cycle element or condition.

### The Unique `else` Clause
Python loops support a trailing `else:` code block. This block executes **only if** the loop completes its full natural run without hitting a single explicit `break` statement.
