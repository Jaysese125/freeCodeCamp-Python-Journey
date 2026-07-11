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

Accessing an invalid index raises:

``` python
IndexError
```

------------------------------------------------------------------------

# 9. Advanced Loop Utilities: `enumerate()` and `zip()`

These built-in functions make loops cleaner, more readable, and more
Pythonic.

## The `enumerate()` Function

`enumerate()` automatically keeps track of the index while iterating
over an iterable.

### Syntax

``` python
enumerate(iterable, start=0)
```

### Returns

An **enumerate object** that yields tuples in the form:

``` text
(index, value)
```

### Example

``` python
languages = ["Spanish", "English", "Russian"]

for index, language in enumerate(languages):
    print(index, language)
```

Output

``` text
0 Spanish
1 English
2 Russian
```

### Starting the Count

Use the optional `start` parameter to begin counting from another value.

``` python
for index, language in enumerate(languages, start=1):
    print(f"{index}: {language}")
```

Output

``` text
1: Spanish
2: English
3: Russian
```

### Why Use `enumerate()`?

Instead of:

``` python
index = 0

for language in languages:
    print(index, language)
    index += 1
```

Use:

``` python
for index, language in enumerate(languages):
    print(index, language)
```

It is shorter, cleaner, and avoids manually updating an index variable.

------------------------------------------------------------------------

## The `zip()` Function

`zip()` combines two or more iterables element-by-element.

### Syntax

``` python
zip(iterable1, iterable2, ...)
```

### Returns

An iterator that yields tuples.

Example:

``` python
developers = ["Naomi", "Dario"]
ids = [101, 102]

print(list(zip(developers, ids)))
```

Output

``` python
[("Naomi", 101), ("Dario", 102)]
```

### Looping with `zip()`

``` python
developers = ["Naomi", "Dario"]
ids = [101, 102]

for name, emp_id in zip(developers, ids):
    print(f"ID {emp_id} belongs to {name}")
```

Output

``` text
ID 101 belongs to Naomi
ID 102 belongs to Dario
```

### Different Length Iterables

`zip()` stops when the shortest iterable is exhausted.

``` python
names = ["Anna", "Ben", "Chris"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)
```

Output

``` text
Anna 90
Ben 85
```

`"Chris"` is ignored because there is no matching score.

------------------------------------------------------------------------

## Combining `enumerate()` and `zip()`

You can number rows while looping through multiple iterables.

``` python
names = ["Anna", "Ben", "Chris"]
scores = [90, 80, 95]

for index, (name, score) in enumerate(zip(names, scores), start=1):
    print(index, name, score)
```

Output

``` text
1 Anna 90
2 Ben 80
3 Chris 95
```

------------------------------------------------------------------------

## Quick Comparison

  -----------------------------------------------------------------------
  Function                  Purpose                Returns
  ------------------------- ---------------------- ----------------------
  `enumerate()`             Loop with both index   `(index, value)`
                            and value              tuples

  `zip()`                   Loop through multiple  Tuples containing one
                            iterables              item from each
                            simultaneously         iterable
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Key Takeaways

-   `enumerate()` automatically provides both the index and value while
    looping.
-   Use `start=` to change the starting index.
-   `zip()` pairs elements from multiple iterables together.
-   `zip()` stops at the shortest iterable.
-   Both functions produce tuples that can be unpacked directly in a
    `for` loop.
-   `enumerate()` and `zip()` can be combined for clean, numbered
    iteration across multiple collections.
