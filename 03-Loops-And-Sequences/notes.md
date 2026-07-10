# 🔄 Study Notes: Loops and Sequences

------------------------------------------------------------------------

# 1. Core Mechanics of Python Lists

## Definition

A **list** is an ordered, mutable collection of items enclosed in square
brackets `[]`.

A list can contain elements of different data types.

``` python
numbers = [1, 2, 3]
mixed = ["Alice", 25, True]
```

## Zero-Based Indexing

-   The first element has an index of `0`.
-   Negative indices count from the end.
-   `-1` refers to the last element.

``` python
fruits = ["apple", "banana", "orange"]

print(fruits[0])   # apple
print(fruits[-1])  # orange
```

Attempting to access an index outside the list raises:

``` python
IndexError
```

------------------------------------------------------------------------

## 9. Advanced Loop Utilities: `enumerate()` and `zip()`

### The `enumerate()` Function

Tracks index positions automatically while traversing an iterable.

-   **Returns:** An enumerate iterator yielding `(index, item)` tuples.
-   **`start` parameter:** Changes the starting index.

``` python
languages = ["Spanish", "English", "Russian"]

for index, lang in enumerate(languages, start=1):
    print(f"{index}: {lang}")

# Output:
# 1: Spanish
# 2: English
# 3: Russian
```

### The `zip()` Function

Combines multiple iterables element-by-element.

-   **Returns:** An iterator of tuples.
-   Stops when the **shortest** iterable is exhausted.

``` python
developers = ["Naomi", "Dario"]
ids = [101, 102]

for name, emp_id in zip(developers, ids):
    print(f"ID {emp_id} belongs to {name}")

# Output:
# ID 101 belongs to Naomi
# ID 102 belongs to Dario
```
