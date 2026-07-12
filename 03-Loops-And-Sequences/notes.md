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

---

## 3. List Comprehensions and Useful List Functions

### List Comprehensions

A **list comprehension** is a concise way to create a new list by combining a loop and an optional condition into a single line.

Instead of writing a traditional `for` loop, list comprehensions allow you to write cleaner and more Pythonic code.

### Traditional Approach

```python
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
```

### Using a List Comprehension

```python
even_numbers = [num for num in range(21) if num % 2 == 0]

print(even_numbers)
```

Both examples produce:

```text
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

List comprehensions reduce boilerplate code while remaining readable.

---

### Conditional Expressions

List comprehensions can also create transformed values.

```python
numbers = [1, 2, 3, 4, 5]

result = [
    (num, "Even") if num % 2 == 0 else (num, "Odd")
    for num in numbers
]

print(result)
```

Output

```text
[(1, 'Odd'),
 (2, 'Even'),
 (3, 'Odd'),
 (4, 'Even'),
 (5, 'Odd')]
```

---

## The `filter()` Function

### Definition

`filter()` selects only the elements that satisfy a condition.

### Syntax

```python
filter(function, iterable)
```

### Example

```python
words = ["tree", "sky", "mountain", "river", "cloud", "sun"]

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))

print(long_words)
```

Output

```text
['mountain', 'river', 'cloud']
```

---

## The `map()` Function

### Definition

`map()` applies a function to every element of an iterable.

### Syntax

```python
map(function, iterable)
```

### Example

```python
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))

print(fahrenheit)
```

Output

```text
[32.0, 50.0, 68.0, 86.0, 104.0]
```

---

## The `sum()` Function

### Definition

`sum()` returns the total of all numeric values in an iterable.

### Syntax

```python
sum(iterable, start=0)
```

### Basic Example

```python
numbers = [5, 10, 15, 20]

total = sum(numbers)

print(total)
```

Output

```text
50
```

### Using the `start` Parameter

```python
numbers = [5, 10, 15, 20]

total = sum(numbers, start=10)

print(total)
```

Output

```text
60
```

The `start` argument adds an initial value before summing the iterable.

---

## 📝 Key Takeaways

### List Comprehensions

- Create lists using a single line.
- Combine loops and optional conditions.
- Often replace simple `for` loops.

### `filter()`

- Selects elements that satisfy a condition.
- Returns a filter object.
- Convert to a list using `list()`.

### `map()`

- Applies a function to every element.
- Returns a map object.
- Convert to a list using `list()`.

### `sum()`

- Calculates the total of an iterable.
- Supports the optional `start` parameter.

---

## 💡 Quick Cheat Sheet

| Function | Purpose |
|----------|---------|
| `[x for x in iterable]` | Basic list comprehension |
| `[x for x in iterable if condition]` | Conditional list comprehension |
| `filter(func, iterable)` | Keep matching elements |
| `map(func, iterable)` | Transform every element |
| `sum(iterable)` | Sum all values |
| `sum(iterable, start=10)` | Sum with an initial value |