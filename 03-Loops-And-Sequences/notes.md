# 🔄 Study Notes: Loops and Sequences

---

# 1. Core Mechanics of Python Lists

## Definition
A **list** is an ordered, mutable collection of items enclosed in square brackets `[]`.

A list can contain elements of different data types.

```python
numbers = [1, 2, 3]
mixed = ["Alice", 25, True]
```

## Zero-Based Indexing

- The first element has an index of `0`.
- Negative indices count from the end.
- `-1` refers to the last element.

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])    # apple
print(fruits[-1])   # orange
```

Attempting to access an index outside the list raises:

```python
IndexError
```

---

# 2. Common List Operations

## Accessing Elements

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])    # apple
print(fruits[-1])   # orange
```

---

## Modifying Elements

Lists are mutable, meaning their contents can be changed after creation.

```python
fruits = ["apple", "banana", "orange"]

fruits[1] = "grape"

print(fruits)
# ['apple', 'grape', 'orange']
```

---

## Removing Elements

```python
fruits = ["apple", "banana", "orange"]

del fruits[0]

print(fruits)
# ['banana', 'orange']
```

Deleting an invalid index raises:

```python
IndexError
```

---

## Unpacking

Assign list elements directly to variables.

```python
name, age, job = ["Alice", 34, "Developer"]

print(name)
print(age)
print(job)
```

Using `*` collects the remaining values into a list.

```python
name, *remaining = ["Alice", 34, "Developer"]

print(name)
# Alice

print(remaining)
# [34, "Developer"]
```

---

## Slicing

General syntax:

```python
sequence[start:stop:step]
```

Where:

- `start` → starting index (inclusive)
- `stop` → ending index (exclusive)
- `step` → interval between elements

Example:

```python
numbers = [0, 1, 2, 3, 4, 5]

numbers[1:4]
# [1, 2, 3]

numbers[:3]
# [0, 1, 2]

numbers[3:]
# [3, 4, 5]

numbers[::2]
# [0, 2, 4]

numbers[::-1]
# [5, 4, 3, 2, 1, 0]
```

---

# 3. Essential Python List Methods

| Method | Returns | Description |
|---------|----------|-------------|
| `list.append(item)` | `None` | Adds one item to the end. |
| `list.extend(iterable)` | `None` | Adds every element from an iterable. |
| `list.insert(index, item)` | `None` | Inserts an item before the specified index. |
| `list.remove(value)` | `None` | Removes the first matching value. Raises `ValueError` if not found. |
| `list.pop(index=-1)` | Removed item | Removes and returns the specified element. |
| `list.clear()` | `None` | Removes all elements. |
| `list.sort(key=None, reverse=False)` | `None` | Sorts the list in place. |
| `sorted(iterable, key=None, reverse=False)` | New list | Returns a new sorted list. |
| `list.reverse()` | `None` | Reverses the list in place. |
| `list.index(value)` | Integer | Returns the first matching index. |
| `list.count(value)` | Integer | Counts occurrences of a value. |
| `list.copy()` | New list | Returns a shallow copy. |
| `len(list)` | Integer | Returns the number of elements. |

---

# 4. `append()` vs `extend()`

## append()

Adds the entire object as a single element.

```python
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
# [1, 2, [3, 4]]
```

---

## extend()

Adds each element individually.

```python
numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)
# [1, 2, 3, 4]
```

### Key Difference

- `append()` adds **one object**.
- `extend()` adds **each element** from an iterable.

---

# 5. In-Place Methods vs Functions That Return New Objects

## In-Place Methods

These modify the original list and return `None`.

```python
numbers.sort()
numbers.reverse()
numbers.append(5)
numbers.clear()
```

---

## Functions Returning New Objects

These leave the original unchanged.

```python
new_numbers = sorted(numbers)
```

Remember:

These methods modify the original list:

- `append()`
- `extend()`
- `insert()`
- `remove()`
- `sort()`
- `reverse()`
- `clear()`

This function returns a new list:

- `sorted()`

---

# 6. Understanding Python Tuples `()`

## Definition

A tuple is an ordered, immutable sequence enclosed in parentheses.

```python
person = ("Alice", 25, "Developer")
```

---

## Immutability

Once created, tuples cannot be modified.

```python
person = ("Alice", 25)

person[0] = "Bob"

# TypeError:
# 'tuple' object does not support item assignment
```

You cannot:

- add elements
- remove elements
- modify elements

---

## Accessing Elements

```python
numbers = (10, 20, 30)

print(numbers[0])
# 10

print(numbers[-1])
# 30
```

---

## Slicing

Tuple slicing works exactly like list slicing.

```python
numbers = (0, 1, 2, 3, 4)

numbers[1:4]
# (1, 2, 3)

numbers[::-1]
# (4, 3, 2, 1, 0)
```

---

## Tuple Unpacking

```python
name, age, job = ("Alice", 34, "Developer")
```

Using `*`:

```python
name, *remaining = ("Alice", 34, "Developer")

print(name)
# Alice

print(remaining)
# [34, "Developer"]
```

> **Note:** `*` always stores the remaining values in a **list**, even when unpacking a tuple.

---

## Tuple Methods

| Method | Returns | Description |
|---------|----------|-------------|
| `tuple.count(value)` | Integer | Counts occurrences of a value. |
| `tuple.index(value[, start[, stop]])` | Integer | Returns the first matching index. |
| `len(tuple)` | Integer | Number of elements. |
| `sorted(tuple)` | New list | Returns a sorted list. |

---

## Lists vs Tuples

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[]` | `()` |
| Mutable | ✅ Yes | ❌ No |
| Ordered | ✅ Yes | ✅ Yes |
| Supports Indexing | ✅ | ✅ |
| Supports Slicing | ✅ | ✅ |
| Can Be Modified | ✅ | ❌ |
| Common Use | Dynamic collections | Read-only or fixed collections |

---

# 7. Control Flow: Loops and Iteration

## `for` Loop

Designed for **definite iteration**.

Traverses an iterable one element at a time.

```python
for fruit in ["apple", "banana", "orange"]:
    print(fruit)
```

---

## `while` Loop

Designed for **indefinite iteration**.

Repeats while a condition remains `True`.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Loop Jump Statements

### `break`

Immediately exits the nearest loop.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

### `continue`

Skips the remainder of the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```
0
1
3
4
```

---

## The `else` Clause

A loop's `else` block executes **only if the loop finishes naturally** without encountering a `break`.

```python
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```

---

# 8. The `range()` Function

## Syntax

```python
range(start, stop, step)
```

### Parameters

- `start` *(optional)* → starting integer (default is `0`)
- `stop` *(required)* → stopping point (exclusive)
- `step` *(optional)* → increment (default is `1`)

---

## Examples

```python
range(5)
# 0 1 2 3 4

range(2, 7)
# 2 3 4 5 6

range(1, 10, 2)
# 1 3 5 7 9

range(10, 0, -2)
# 10 8 6 4 2
```

---

## Core Technical Rules

### Integer Only

Passing a float raises:

```python
TypeError
```

Example:

```python
range(5.5)
```

---

### Lazy Evaluation

`range()` creates a **range object**, not an actual list.

```python
numbers = range(5)

print(numbers)
# range(0, 5)
```

Convert to a list when needed.

```python
list(range(5))

# [0, 1, 2, 3, 4]
```

---

### Counting Down

To decrement:

- `start` must be greater than `stop`
- `step` must be negative

```python
range(40, 0, -10)

# 40 30 20 10
```

---

# ✅ Quick Summary

### Lists

- Mutable
- Use `[]`
- Can be modified
- Many built-in methods

### Tuples

- Immutable
- Use `()`
- Faster for fixed data
- Only `count()` and `index()` methods

### Loops

- `for` → definite iteration
- `while` → condition-based iteration
- `break` exits the loop
- `continue` skips an iteration
- `else` executes only if no `break` occurs

### `range()`

- Generates integer sequences
- Stop value is exclusive
- Supports positive and negative steps
- Creates a lazy `range` object

---

## 9. Advanced Loop Utilities: `enumerate()` and `zip()`

### The `enumerate()` Function
Tracks individual index positions automatically while traversing an iterable, eliminating the need for manual state tracking variables.
* **Returns:** An enumerate iterator object containing pairs of standard tuples: `(index, item)`.
* **The `start` Offset:** Use the optional second parameter to change the starting value of the index counter.

```python
languages = ['Spanish', 'English', 'Russian']
for index, lang in enumerate(languages, start=1):
    print(f"{index}: {lang}")
# Output: 1: Spanish, 2: English, 3: Russian

###The `zip()` Function
Combines multiple iterables elements downstream column-by-column, allowing you to cycle through them simultaneously.
* **Returns:** An iterator of tuples, where the $i$-th tuple contains the $i$-th element from each of the input sequences.
* **Behavior with Unequal Lengths:** Natively stops processing immediately as soon as the shortest input collection is completely exhausted.

```python
developers = ['Naomi', 'Dario']
ids = [101, 102]
for name, emp_id in zip(developers, ids):
    print(f"ID {emp_id} belongs to {name}")