[<<Day 9](../Day_9/) | **Day 10** | [Day 11>>](../Day_11/)

# 30 Days of Python Coding

## Day 10 - Loops

Welcome to Day 10 of the **30 Days of Python Coding**! Today, we explore the versatile and powerful concept of **loops** in Python. Loops enable programmers to execute blocks of code multiple times, making tasks like data processing, automation, and complex calculations much simpler.

---

## Overview

Loops are fundamental constructs in programming that allow repetitive execution of code. Python provides two main types of loops:

- **While Loops**: Ideal for scenarios where the repetition depends on a condition being true.
- **For Loops**: Used to iterate over sequences such as lists, strings, tuples, and dictionaries.

This tutorial offers a step-by-step guide to Python loops with examples and practical use cases. Whether you're a beginner or refining your skills, this content has something for everyone.

---

## Usage Guide

### While Loop

The `while` loop runs as long as the specified condition is `True`.

**Syntax**:

```python
while condition:
    # Code to execute
```

**Example**:

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop ended naturally.")
```

### For Loop

The `for` loop is used to iterate over items in a sequence.

**Syntax**:

```python
for item in iterable:
    # Code to execute
```

**Example**:

```python
for char in "Python":
    print(char)
```

### Range Function

The `range()` function generates sequences of numbers, commonly used with `for` loops.

**Syntax**:

```python
range(start, stop, step)
```

**Example**:

```python
for num in range(1, 10, 2):
    print(num)  # Prints odd numbers from 1 to 9
```

### Nested Loops

Loops can be nested to handle complex structures like matrices or tables.

**Example**:

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

### Break and Continue

These statements alter the flow of loops.

**Example (While Loop)**:

```python
count = 0
while count < 10:
    if count == 5:
        break
    count += 1
    if count % 2 == 0:
        continue
    print(count)
```

### Summary

- **While Loops**: Repeat based on conditions.
- **For Loops**: Iterate over sequences.
- **Range**: Generate numeric sequences.
- **Break**: Exit loops prematurely.
- **Continue**: Skip iterations.
- **Nested Loops**: Use loops inside loops for complex data handling.

---

## Best Practices

- Use meaningful variable names (e.g., `item`, `index`) for clarity.
- Avoid infinite loops by ensuring conditions are properly updated.
- Prefer `for` loops over `while` loops when iterating over sequences.
- Use built-in functions like `enumerate()` for cleaner and more efficient code.
- Limit the nesting of loops to two levels to maintain readability.
- Employ `break` and `continue` judiciously to avoid confusing logic.

---

## Exercises

1. **Exercise 1**: Write a `while` loop to print numbers from 1 to 10, but skip numbers divisible by 3.
2. **Exercise 2**: Use a `for` loop with `range()` to generate the first 10 square numbers.
3. **Exercise 3**: Create a nested loop that prints a multiplication table (1 to 5).
4. **Exercise 4**: Write a `for` loop that iterates over a dictionary and prints keys and values.
5. **Exercise 5**: Modify a `while` loop to terminate early if a certain condition is met.

---

## Running the Code

To run this code, simply execute the 'Loops.py' file using Python (e.g., python Loops.py).

---

## Contributions

Feel free to contribute to this repository by adding more code snippets and examples from your own Python coding journey!

---

Thank you for being part of the **30 Days of Python Coding** challenge. Keep practicing, and don't hesitate to experiment with loops to solidify your understanding! 🚀

[<<Day 9](../Day_9/) | **Day 10** | [Day 11>>](../Day_11/)
