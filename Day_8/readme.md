[<<Day 7](../Day_7/) | <b>Day 8</b> | [Day 9>>](../Day_9/)

# 30 Days of Python Coding

##### ================================================

## Day 8: Dictionaries

Welcome to **Day 8** of the **30 Days of Python Coding** challenge! This segment focuses on Python dictionaries—a powerful, flexible data structure that's essential for any Python programmer.

---

## Table of Contents

1. [Introduction to Dictionaries](#introduction-to-dictionaries)
2. [Creating Dictionaries](#creating-dictionaries)
3. [Accessing Dictionary Items](#accessing-dictionary-items)
4. [Modifying Dictionary Items](#modifying-dictionary-items)
5. [Checking for Keys](#checking-for-keys)
6. [Removing Items](#removing-items)
7. [Additional Dictionary Operations](#additional-dictionary-operations)
8. [Examples](#examples)
9. [Exercises](#exercises)

---

## Introduction to Dictionaries

Dictionaries in Python are collections of key-value pairs. Unlike lists or tuples, dictionaries are:

- **Unordered**: Items have no fixed position.
- **Mutable**: You can add, modify, or delete items.
- **Indexed by keys**: Instead of numerical indices, dictionaries use keys to access values.

### Syntax

```python
my_dict = {"key1": "value1", "key2": "value2"}
```

- **Keys** must be immutable types (e.g., strings, numbers, tuples).
- **Values** can be of any data type.

---

## Creating Dictionaries

### Using Curly Braces

```python
empty_dict = {}
fruit_colors = {"apple": "red", "banana": "yellow"}
```

### Using the `dict()` Constructor

```python
person = dict(name="Alice", age=30, city="New York")
```

### From a List of Tuples

```python
pairs = [("a", 1), ("b", 2)]
converted_dict = dict(pairs)
```

---

## Accessing Dictionary Items

### Using Keys

```python
fruit_colors = {"apple": "red", "banana": "yellow"}
print(fruit_colors["apple"])  # Output: red
```

### Using `get()` Method

```python
print(fruit_colors.get("orange", "Not Found"))  # Output: Not Found
```

---

## Modifying Dictionary Items

### Adding New Items

```python
fruit_colors["orange"] = "orange"
```

### Updating Existing Items

```python
fruit_colors["banana"] = "green"
```

---

## Checking for Keys

### Using the `in` Keyword

```python
print("apple" in fruit_colors)  # Output: True
```

### Using `keys()` Method

```python
print("banana" in fruit_colors.keys())  # Output: True
```

---

## Removing Items

### Using `pop()`

```python
fruit_colors.pop("apple")
```

### Using `del`

```python
del fruit_colors["banana"]
```

### Using `clear()`

```python
fruit_colors.clear()
```

---

## Additional Dictionary Operations

### Looping Through a Dictionary

```python
for key, value in fruit_colors.items():
    print(f"{key}: {value}")
```

### Dictionary Comprehension

```python
squared_numbers = {x: x**2 for x in range(5)}
```

### Converting to List of Tuples

```python
list_of_tuples = list(fruit_colors.items())
```

---

## Examples

### Example 1: Word Frequency Counter

```python
sentence = "hello world hello"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # Output: {"hello": 2, "world": 1}
```

### Example 2: Nested Dictionary

```python
students = {
    "Alice": {"math": 90, "science": 85},
    "Bob": {"math": 70, "science": 80}
}
print(students["Alice"]["math"])  # Output: 90
```

---

## Exercises

### 1. Creating a Dictionary

Create a dictionary that maps countries to their capitals. Add, modify, and remove some entries.

### 2. Word Length Mapping

Write a program that takes a list of words and creates a dictionary where the keys are the words and the values are their lengths.

### 3. Dictionary to Tuples

Convert a dictionary into a list of tuples and sort them by key or value.

---

## Running the Code

To run this code, simply execute the 'Dictionaries.py' file using Python (e.g., python Dictionaries.py).

---

## Contributions

Feel free to contribute to this repository by adding more code snippets and examples from your own Python coding journey!

[<<Day 7](../Day_7/) | <b>Day 8</b> | [Day 9>>](../Day_9/)
