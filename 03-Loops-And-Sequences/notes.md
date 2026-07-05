# 🔄 Study Notes: Loops and Sequences

## 1. Core Mechanics of Python Lists

- **Definition:** A **list** is an ordered, mutable collection of items enclosed in square brackets `[]`. A list can contain elements of different data types.

- **Zero-Based Indexing:** The first element has an index of `0`. Negative indices access elements from the end of the list, where `-1` refers to the last element.

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

The `del` statement removes an element by index. Accessing an invalid index raises an `IndexError`.

### Unpacking

List unpacking assigns elements directly to variables.

```python
name, age, job = ["Alice", 34, "Developer"]
```

Use `*` to collect any remaining elements into a list.

```python
name, *remaining = ["Alice", 34, "Developer"]

print(name)       # Alice
print(remaining)  # [34, "Developer"]
```

### Slicing

General syntax:

```python
list[start:stop:step]
```

- `start` → first index (inclusive)
- `stop` → ending index (exclusive)
- `step` → interval between elements

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

| Method / Function | Returns | Description |
|-------------------|---------|-------------|
| `list.append(item)` | `None` | Adds one item to the end of the list. |
| `list.extend(iterable)` | `None` | Appends each element from an iterable. |
| `list.insert(index, item)` | `None` | Inserts an item before the specified index. |
| `list.remove(value)` | `None` | Removes the first matching value. Raises `ValueError` if not found. |
| `list.pop(index=-1)` | Removed item | Removes and returns the element at the specified index (last by default). |
| `list.clear()` | `None` | Removes all elements from the list. |
| `list.sort(key=None, reverse=False)` | `None` | Sorts the list in place. |
| `sorted(iterable, key=None, reverse=False)` | New list | Returns a new sorted list without modifying the original. |
| `list.reverse()` | `None` | Reverses the list in place. |
| `list.index(value)` | Index | Returns the index of the first occurrence. Raises `ValueError` if not found. |
| `list.count(value)` | Count | Returns how many times a value appears. |
| `list.copy()` | New list | Returns a shallow copy of the list. |
| `len(list)` | Integer | Returns the number of elements. |

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

- `append()` adds the entire object as a single element.
- `extend()` adds each element individually.

---

## 5. In-Place vs Returning a New Object

**In-place methods** modify the original list.

```python
numbers.sort()
numbers.reverse()
numbers.append(5)
```

**Functions that return a new object** leave the original unchanged.

```python
new_numbers = sorted(numbers)
```

Remember:

- Methods like `append()`, `sort()`, and `reverse()` return `None`.
- Functions like `sorted()` create and return a new list.