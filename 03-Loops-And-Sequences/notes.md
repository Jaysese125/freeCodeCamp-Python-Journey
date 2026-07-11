# 🔄 Study Notes: Loops and Sequences

## 1. Core Mechanics of Python Lists

### Definition

A **list** is an ordered, mutable collection enclosed in square brackets
`[]`.

Lists can store multiple values, including different data types.

``` python
numbers = [1, 2, 3]
mixed = ["Alice", 25, True]
```

### Zero-Based Indexing

-   The first element has an index of `0`.
-   Negative indices count from the end.
-   `-1` refers to the last element.

``` python
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[-1])
```

Accessing an invalid index raises:

``` text
IndexError
```

------------------------------------------------------------------------

## 2. Advanced Loop Utilities: `enumerate()` and `zip()`

After learning `for` loops, Python provides two useful built-in
functions that make looping cleaner and more readable.

### The `enumerate()` Function

#### Definition

`enumerate()` automatically keeps track of the index while iterating
over an iterable.

Instead of manually maintaining an index variable, it returns both the
index and the value.

#### Syntax

``` python
enumerate(iterable, start=0)
```

### Without `enumerate()`

``` python
languages = ["Spanish", "English", "Russian", "Chinese"]

index = 0

for language in languages:
    print(f"Index {index} and language {language}")
    index += 1
```

### Using `enumerate()`

``` python
languages = ["Spanish", "English", "Russian", "Chinese"]

for index, language in enumerate(languages):
    print(f"Index {index} and language {language}")
```

Output

``` text
Index 0 and language Spanish
Index 1 and language English
Index 2 and language Russian
Index 3 and language Chinese
```

### What Does `enumerate()` Return?

``` python
languages = ["Spanish", "English", "Russian", "Chinese"]

print(list(enumerate(languages)))
```

Output

``` python
[(0, 'Spanish'),
 (1, 'English'),
 (2, 'Russian'),
 (3, 'Chinese')]
```

Each item is a tuple:

``` text
(index, value)
```

The `for` loop automatically unpacks each tuple into the variables
`index` and `language`.

### Using the `start` Parameter

``` python
for index, language in enumerate(languages, 1):
    print(f"Index {index} and language {language}")
```

Output

``` text
Index 1 and language Spanish
Index 2 and language English
Index 3 and language Russian
Index 4 and language Chinese
```

The optional `start` argument changes the initial value of the counter.

### When to Use `enumerate()`

-   When you need both the index and value.
-   To avoid manually incrementing an index variable.
-   To write cleaner, more Pythonic loops.

------------------------------------------------------------------------

## The `zip()` Function

### Definition

`zip()` combines two or more iterables element-by-element and returns an
iterator of tuples.

### Syntax

``` python
zip(iterable1, iterable2, ...)
```

### Viewing the Result

``` python
developers = ["Naomi", "Dario", "Jessica", "Tom"]
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))
```

Output

``` python
[('Naomi', 1),
 ('Dario', 2),
 ('Jessica', 3),
 ('Tom', 4)]
```

Each tuple contains one item from each iterable.

### Using `zip()` in a Loop

``` python
developers = ["Naomi", "Dario", "Jessica", "Tom"]
ids = [1, 2, 3, 4]

for name, emp_id in zip(developers, ids):
    print(f"Name: {name}")
    print(f"ID: {emp_id}")
```

Output

``` text
Name: Naomi
ID: 1
Name: Dario
ID: 2
Name: Jessica
ID: 3
Name: Tom
ID: 4
```

The tuples returned by `zip()` are automatically unpacked into `name`
and `emp_id`.

### Key Behavior

`zip()` stops when the shortest iterable is exhausted.

``` python
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)
```

Output

``` text
Alice 90
Bob 85
```

`"Charlie"` is ignored because there is no matching score.

------------------------------------------------------------------------

## 📝 Key Takeaways

### `enumerate()`

-   Automatically provides an index and value.
-   Returns an enumerate object.
-   Produces `(index, value)` tuples.
-   Supports the optional `start` parameter.

### `zip()`

-   Iterates over multiple iterables in parallel.
-   Returns tuples containing paired elements.
-   Stops when the shortest iterable ends.

## 💡 Cheat Sheet

  -----------------------------------------------------------------------
  Function                              Purpose
  ------------------------------------- ---------------------------------
  `enumerate(iterable)`                 Returns `(index, value)` pairs

  `enumerate(iterable, start=1)`        Starts counting from a custom
                                        number

  `zip(a, b)`                           Combines iterables into tuples

  `list(enumerate(...))`                View enumerate output

  `list(zip(...))`                      View zipped tuples
  -----------------------------------------------------------------------
