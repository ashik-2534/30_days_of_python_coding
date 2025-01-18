[<<Day 5](../Day_5/) | <b>Day 6</b> | [Day 7>>](../Day_7)

# 30 Days of Python Coding
### ===============================



## Day 6: Tuples

Welcome to Day 6 of the **30 Days of Python Coding** series! Today, we'll be diving into **Tuples** in Python. Tuples are an essential data structure that allows you to store multiple values in a single variable. They are similar to lists, but with some key differences. By the end of today’s lesson, you'll have a strong understanding of how to work with tuples and how they can be applied in your code.

---

## Table of Contents

- [Introduction to Tuples](#introduction-to-tuples)
- [Creating Tuples](#creating-tuples)
- [Tuple Operations](#tuple-operations)
  - [Accessing Tuple Items](#accessing-tuple-items)
  - [Slicing Tuples](#slicing-tuples)
  - [Changing Tuples to Lists](#changing-tuples-to-lists)
  - [Checking for Items in Tuples](#checking-for-items-in-tuples)
  - [Joining Tuples](#joining-tuples)
  - [Deleting Tuples](#deleting-tuples)
- [Exercises](#exercises)
  - [Exercise Level 1](#exercise-level-1)
  - [Exercise Level 2](#exercise-level-2)

---

## Introduction to Tuples

A **tuple** is a collection of objects in Python that is ordered and immutable. Unlike lists, tuples cannot be changed after they are created. This makes them an excellent choice for fixed data, which ensures that the values in a tuple cannot be altered accidentally.

### Properties of Tuples:
- **Ordered**: The items in a tuple are indexed, meaning their order is maintained.
- **Immutable**: Once a tuple is created, you cannot modify its content (no appending, removing, or changing values).
- **Allows duplicates**: A tuple can have multiple instances of the same value.
- **Supports multiple data types**: A tuple can hold items of different data types (e.g., integers, strings, lists).
- **Can be nested**: Tuples can contain other tuples.

### Common Tuple Methods:
- **count()**: Returns the number of occurrences of a specified value.
- **index()**: Returns the index of the first occurrence of a specified value.

Example:
```python
my_tuple = (1, 2, 3, 4, 1, 2)
print(my_tuple.count(2))  # Output: 2
print(my_tuple.index(3))  # Output: 2
```

---

## Creating Tuples

In Python, tuples are created by placing the items inside parentheses `()`, separated by commas. You can create a tuple with or without initial values.

### 1. Creating an empty tuple:
```python
empty_tuple = ()
print(empty_tuple)  # Output: ()
```

### 2. Creating a tuple with initial values:
```python
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
```

### 3. Creating a tuple with different data types:
```python
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)  # Output: (1, 'hello', 3.14, True)
```

### 4. Creating a tuple with one item:
```python
single_item_tuple = (5,)
print(single_item_tuple)  # Output: (5)
```
**Note**: A tuple with a single item must include a trailing comma.

---

## Tuple Operations

### Accessing Tuple Items

You can access elements of a tuple by indexing, just like you would with a list. Indexing starts at 0.

Example:
```python
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # Output: banana
```

### Slicing Tuples

You can also slice a tuple to get a range of values. The syntax is `[start:end]`.

Example:
```python
my_tuple = ("apple", "banana", "cherry", "date", "elderberry")
print(my_tuple[1:4])  # Output: ('banana', 'cherry', 'date')
```

### Changing Tuples to Lists

While tuples are immutable, you can convert them into lists if you need to modify their contents. After changing the list, you can convert it back into a tuple.

Example:
```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3, 4)
```

### Checking for Items in Tuples

You can check if a value exists in a tuple using the `in` keyword.

Example:
```python
my_tuple = (1, 2, 3, 4)
print(3 in my_tuple)  # Output: True
print(5 in my_tuple)  # Output: False
```

### Joining Tuples

You can join two or more tuples using the `+` operator.

Example:
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)
```

### Deleting Tuples

You can delete a tuple entirely using the `del` statement. However, since tuples are immutable, you cannot delete individual items from a tuple.

Example:
```python
my_tuple = (1, 2, 3)
del my_tuple
# print(my_tuple)  # This will raise an error because my_tuple is deleted.
```

---

## Exercises

### Exercise Level 1

1. **Create a tuple** with five of your favorite fruits.
2. **Access the third element** in the tuple.
3. **Create a tuple** containing mixed data types (integers, strings, and booleans).
4. **Slice the tuple** to get the first three items.

### Exercise Level 2

1. **Create two tuples**: One with the numbers 1-5, and another with the numbers 6-10. **Combine** them into a single tuple.
2. **Check if a specific number** exists in the combined tuple (e.g., check if 7 exists).
3. Convert a tuple of numbers into a **list**, add 11 to the list, and then convert it back into a tuple.
4. **Count the number of occurrences** of a specific item in a tuple (e.g., count how many times the number 3 appears).
5. **Delete the tuple** once you are done using it.

---

### Conclusion

Today, you learned about **tuples** in Python, their characteristics, how to create and manipulate them, and how to perform operations such as slicing, checking items, and joining tuples. The exercises will help you apply these concepts in practice. Make sure to complete them to get a better understanding!

Happy coding, and see you tomorrow for Day 7!

---

## Running the Code
To run this code, simply execute the 'Tuple.py' file using Python (e.g., python Tuple.py).

## Contributions
Feel free to contribute to this repository by adding more code snippets and examples from your own Python coding journey!

---