# 30-Day Python Coding Challenge
=====================================

Welcome to the 30-Day Python Coding Challenge! This repository contains code snippets and examples from a 30-day journey through the world of Python programming.

## Table of Contents
-----------------

### Day 1-5: Fundamentals

* [Day 1: Basic Operations and Data Types](./Day_1/)
* [Day 2: Variables, Built-in Functions](./Day_2/)
* [Day 3: Operators](./Day_3/)
* [Day 4: Strings](./Day_4/)
* [Day 5: Lists](./Day_5/)

### Day 6-15: Data Structures and Control Flow

* [Day 6: Tuples](./Day_6/)
* [Day 7: Sets](#day-7-sets)
* [Day 8: Dictionaries](#day-8-dictionaries)
* [Day 9: Conditionals](#day-9-conditionals)
* [Day 10: Loops](#day-10-loops)
* [Day 11: Functions](#day-11-functions)
* [Day 12: Modules](#day-12-modules)
* [Day 13: List Comprehension](#day-13-list-comprehension)
* [Day 14: Higher Order Functions](#day-14-higher-order-functions)
* [Day 15: Python Type Errors](#day-15-python-type-errors)

### Day 16-25: Advanced Topics

* [Day 16: Python Date time](#day-16-python-date-time)
* [Day 17: Exception Handling](#day-17-exception-handling)
* [Day 18: Regular Expressions](#day-18-regular-expressions)
* [Day 19: File Handling](#day-19-file-handling)
* [Day 20: Python Package Manager](#day-20-python-package-manager)
* [Day 21: Classes and Objects](#day-21-classes-and-objects)
* [Day 22: Web Scraping](#day-22-web-scraping)
* [Day 23: Virtual Environment](#day-23-virtual-environment)
* [Day 24: Statistics](#day-24-statistics)
* [Day 25: Pandas](#day-25-pandas)

### Day 26-30: Web Development and APIs

* [Day 26: Python web](#day-26-python-web)
* [Day 27: Python with MongoDB](#day-27-python-with-mongodb)
* [Day 28: API](#day-28-api)
* [Day 29: Building API](#day-29-building-api)
* [Day 30: Conclusions](#day-30-conclusions)

## Interactive Code Snippets
---------------------------

## Day 1: Basic Operations and Data Types
#### [click here to open the <b>Helloworld.py</b> file](./Day_1/)

This file (`Helloworld.py`) covers basic arithmetic operations and data types in Python.

### Arithmetic Operations

* Addition: `2 + 3`
* Subtraction: `3 - 1`
* Multiplication: `2 * 3`
* Division: `3 / 2`
* Exponentiation: `3 ** 2`
* Modulus/Remainder: `3 % 2`
* Floor Division: `3 // 2`

### Data Types

* Integer: `10`
* Float: `3.14`
* Complex Number: `1 + 3j`
* String: `"HelloWorld"`
* List: `[1, 2, 3]`
* Tuple: `(1, 2, 3)`
* Dictionary: `{"name": "John", "age": 36, "country": "Norway"}`
* Set: `{1, 2, 3}`
* Boolean: `True`

## Running the Code

To run this code, simply execute the `Helloworld.py` file using Python (e.g., `python Helloworld.py`).

=====================================



## Day 2: Variables and Built in Functions
--------------------------------------
#### [click here to open the <b>Variables.py</b> file](./Day_2/)

### Variables

This file demonstrates the use of variables in Python, including:

* Valid names for declaring variables
* Assigning values to variables
* Multiple assignment

### Built-in Functions

This file uses the following built-in Python functions:

* `type()`: to check the data type of a variable
* `len()`: to get the length of a string

### Arithmetic Operations

This file demonstrates various arithmetic operations using variables, including:

* Addition: `num_one + num_two`
* Subtraction: `num_one - num_two`
* Multiplication: `num_one * num_two`
* Division: `num_one / num_two`
* Modulus/Remainder: `num_one % num_two`
* Exponentiation: `num_one ** num_two`
* Floor Division: `num_one // num_two`

### User Input

This file uses the `input()` function to get user input for various variables, including:

* First name
* Last name
* Country
* Age

#### [click here to open the <b>Variables.py</b> file](./Day_2/)


### Calculations

This file performs calculations using variables, including:

* Calculating the area of a circle given the radius
* Calculating the circumference of a circle given the radius

### Example Use Cases

This file provides example use cases for the concepts demonstrated, including:

* Printing the data type of a variable
* Printing the length of a string
* Performing arithmetic operations using variables
* Getting user input for variables
* Performing calculations using variables

### Code Structure

This file is structured into the following sections:

* Variables
* Built-in Functions
* Arithmetic Operations
* User Input
* Calculations
* Example Use Cases

### Additional Examples

This file also includes the following additional examples:

* Declaring and using multiple variables
* Performing arithmetic operations with user input
* Calculating the area and circumference of a circle with user input

## Running the Code

To run this code, simply execute the `variables.py` file using Python (e.g., `python variables.py`).

=====================================

## Day 3: Operators
--------------------
#### [click here to open the <b>Operators.py</b> file](./Day_3/)
This file (`Operators.py`) covers Operators in Python.
### Introduction

In Python, operators are special symbols that perform operations on variables and values. In this section, we will explore the different types of operators in Python, including arithmetic, comparison, logical, and assignment operators.

### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication, and division.

#### Example

```python
# Addition
a = 5
b = 3
print(a + b)  # Output: 8

# Subtraction
a = 5
b = 3
print(a - b)  # Output: 2

# Multiplication
a = 5
b = 3
print(a * b)  # Output: 15

# Division
a = 5
b = 3
print(a / b)  # Output: 1.6666666666666667
```

### Comparison Operators
Comparison operators are used to compare values and variables.

Example
```python
# Equal
a = 5
b = 5
print(a == b)  # Output: True

# Not Equal
a = 5
b = 3
print(a != b)  # Output: True

# Greater Than
a = 5
b = 3
print(a > b)  # Output: True

# Less Than
a = 5
b = 3
print(a < b)  # Output: False
```

### Logical Operators
Logical operators are used to combine conditional statements.

Example

```python
# And
a = 5
b = 3
print(a > 2 and b < 4)  # Output: True

# Or
a = 5
b = 3
print(a > 2 or b < 2)  # Output: True

# Not
a = 5
print(not a > 2)  # Output: False
```
### Assignment Operators
Assignment operators are used to assign values to variables.

Example
```python
# Assign
a = 5
print(a)  # Output: 5

# Add and Assign
a = 5
a += 3
print(a)  # Output: 8

# Subtract and Assign
a = 5
a -= 3
print(a)  # Output: 2
```
### Interactive Examples

###### Try running the following code in your Python interpreter:

```python
# Ask the user for their name
name = input("What is your name? ")

# Print out a greeting
print("Hello, " + name + "!")

# Ask the user for their age
age = int(input("How old are you? "))

# Print out a message based on their age
if age > 18:
    print("You are an adult!")
else:
    print("You are a minor!")
```

##### This code uses the input() function to get user input, and the print() function to output messages to the user. It also uses conditional statements to print out different messages based on the user's age.

### Additional Examples
Here are some additional examples that demonstrate the use of operators:

##### Calculating the area and circumference of a circle
```python
# Prompt the user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area and circumference
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius

# Print the results
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
```
#### Checking if a string contains a specific substring
```python
# Prompt the user for a string
string = input("Enter a string: ")

# Check if the string contains the substring "hello"
if "hello" in string:
    print("The string contains the substring 'hello'")
else:
    print("The string does not contain the substring 'hello'")

```
### Conclusion
In this section, we have explored the different types of operators in Python, including arithmetic, comparison, logical, and assignment operators. We have also seen how to use these operators in interactive examples and additional examples.

## Running the Code

To run this code, simply execute the `Operators.py` file using Python (e.g., `python Operators.py`).

=====================================

## Day 4: Strings
### [click here to open the <b>Strings.py</b> file](./Day_4/)
This file, "Day 4 - Strings", is on Python strings. It covers various topics, including creating strings, string concatenation, escape sequences, string formatting, accessing and slicing strings, and string methods. It also includes exercises to practice string manipulation in Python.

### Creating Strings

Strings in Python are immutable sequences of characters enclosed in quotes. You can create strings using single quotes, double quotes, or triple quotes. Here are a few examples:

```python
# Creating strings using single quotes
my_string1 = 'Hello, World!'
print(my_string1)

# Creating strings using double quotes
my_string2 = "Hello, World!"
print(my_string2)

# Creating strings using triple quotes
my_string3 = '''Hello,
World!'''
print(my_string3)
```
## String Concatenation
You can concatenate strings using the + operator. Here are a few examples:
```python
# Concatenating strings using the + operator
my_string1 = 'Hello, '
my_string2 = 'World!'
my_string3 = my_string1 + my_string2
print(my_string3)

# Concatenating strings using the * operator
my_string4 = 'Hello' * 3
print(my_string4)
```

## Escape Sequences
In Python, certain characters have special meanings and cannot be used directly in strings. To include these characters in a string, you can use escape sequences. Here are a few examples:

```python
# Using escape sequences in strings
my_string = 'This is a string with a newline\nand a tab\t'
print(my_string)
```

## String Formatting
Python provides several ways to format strings. One common method is to use the format() method. Here are a few examples:

```python
# Formatting strings using the format() method
name = 'John'
age = 36
my_string = 'My name is {} and I am {} years old.'.format(name, age)
print(my_string)

# Formatting strings using f-strings (Python 3.6+)
name = 'John'
age = 36
my_string = f'My name is {name} and I am {age} years old.'
print(my_string)
```

## Accessing and Slicing Strings
You can access individual characters in a string using indexing. You can also slice a string to extract a portion of it. Here are a few examples:

```python
# Accessing and slicing strings
my_string = 'Hello, World!'
print(my_string[0])  # Output: H
print(my_string[7:])  # Output: World!
print(my_string[0:5])  # Output: Hello
```


## String Methods
Python provides a wide range of string methods that you can use to manipulate strings. Here are a few examples:

```python
# Using string methods
my_string = 'Hello, World!'
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.lower())  # Output: hello, world!
print(my_string.strip())  # Output: Hello, World!
print(my_string.replace('Hello', 'Hi'))  # Output: Hi, World!
print('World' in my_string)  # Output: True
```

## Exercises
Here are some exercises to practice string manipulation in Python:

1. Write a program to reverse a string.
2. Write a program to check if a string is a palindrome (reads the same forwards and backwards).
3. Write a program to count the number of vowels in a string.
4. Write a program to remove all the vowels from a string.



## Running the Code
To run this code, simply execute the 'Strings.py' file using Python (e.g., python Strings.py).

=====================================


## Day 5: Lists
### [click here to open the <b>Lists.py</b> file](./Day_5/)


Welcome to Day 5 of the **30 Days of Python Coding** series! Today, we focus on one of Python's most versatile and widely used data structures: **Lists**. This lesson covers all the essentials and advanced techniques you'll need to master Python lists.

---

### What Are Lists?

A **list** in Python is a collection of items (or elements) that can hold a variety of data types. Lists are ordered, mutable (modifiable), and allow duplicate elements. They are defined using square brackets `[]`.

**Example:**
```python
# Creating a list of mixed data types
my_list = [1, "Hello", 3.14, True]
print(my_list)
# Output: [1, 'Hello', 3.14, True]
```

---

### Topics Covered

#### 1. **Creating Lists**
You can create lists using square brackets or the `list()` constructor.

**Examples:**
```python
# Empty list
empty_list = []

# List with initial values
numbers = [1, 2, 3, 4, 5]

# Using the list constructor
chars = list("hello")
print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']
```

---

#### 2. **Accessing List Items**
Access list elements using **positive** or **negative** indexing.

**Examples:**
```python
my_list = [10, 20, 30, 40, 50]

# Positive indexing
print(my_list[0])  # Output: 10

# Negative indexing
print(my_list[-1])  # Output: 50
```

---

#### 3. **Unpacking List Items**
Assign list elements directly to variables.

**Example:**
```python
numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)  # Output: 1 2 3
```

---

#### 4. **Slicing Lists**
Extract specific portions of a list using slicing.

**Syntax:**
```python
list[start:stop:step]
```

**Example:**
```python
numbers = [10, 20, 30, 40, 50]

# Slice from index 1 to 3
print(numbers[1:4])  # Output: [20, 30, 40]

# Reverse a list
print(numbers[::-1])  # Output: [50, 40, 30, 20, 10]
```

---

#### 5. **Modifying Lists**
Lists are mutable, allowing item updates.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

---

#### 6. **Checking Items in a List**
Use the `in` operator to check for item existence.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
```

---

#### 7. **Adding Items to a List**

- **Using `append()`:** Adds an item to the end of the list.
- **Using `extend()`:** Adds multiple items to the list.

**Examples:**
```python
# Append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Extend
my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

---

#### 8. **Inserting Items into a List**
Use `insert(index, item)` to add an item at a specific position.

**Example:**
```python
colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
print(colors)  # Output: ['red', 'yellow', 'blue', 'green']
```

---

#### 9. **Removing Items from a List**

- **Using `remove(value)`:** Removes the first occurrence of a value.
- **Using `pop(index)`:** Removes and returns the item at a specific index.
- **Using `del`:** Deletes an item or slice.

**Examples:**
```python
# Remove
nums = [1, 2, 3, 4]
nums.remove(3)
print(nums)  # Output: [1, 2, 4]

# Pop
nums.pop(1)
print(nums)  # Output: [1, 4]

# Del
del nums[0]
print(nums)  # Output: [4]
```

---

#### 10. **Clearing List Items**
Remove all items using `clear()`.

**Example:**
```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
```

---

#### 11. **Copying Lists**
Create a copy of a list using slicing or the `copy()` method.

**Examples:**
```python
original = [1, 2, 3]

# Using slicing
copy1 = original[:]

# Using copy()
copy2 = original.copy()
```

---

#### 12. **Joining Lists**
Combine two or more lists using the `+` operator or the `extend()` method.

**Examples:**
```python
list1 = [1, 2]
list2 = [3, 4]

# Using +
combined = list1 + list2

# Using extend()
list1.extend(list2)
```

---

#### 13. **Counting Items in a List**
Use `count(value)` to count occurrences of a value.

**Example:**
```python
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))  # Output: 3
```

---

#### 14. **Finding the Index of an Item**
Use `index(value)` to find the first occurrence of a value.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1
```

---

#### 15. **Reversing a List**
Reverse the order of items using `reverse()` or slicing.

**Examples:**
```python
my_list = [1, 2, 3]

# Using reverse()
my_list.reverse()

# Using slicing
reversed_list = my_list[::-1]
```

---

#### 16. **Sorting List Items**
Sort lists using the `sort()` method or the `sorted()` function.

**Examples:**
```python
nums = [3, 1, 4, 2]

# Using sort()
nums.sort()

# Using sorted()
sorted_nums = sorted(nums, reverse=True)
```

---

### Practice Exercises

1. Create a list with at least five items. Access the second and last items using both positive and negative indexing.
2. Write a Python program to reverse a list without using the `reverse()` method.
3. Count how many times the number `3` appears in the list `[1, 3, 3, 4, 3, 5]`.
4. Combine two lists `[1, 2, 3]` and `[4, 5, 6]` using two different methods.
5. Write a program to sort a list of strings alphabetically.

---

### Conclusion
Python lists are powerful and versatile tools. Mastering lists will greatly enhance your ability to solve problems and write efficient code. Practice each concept thoroughly, and you’ll be ready to tackle more advanced Python topics in the coming days!

## Running the Code
To run this code, simply execute the 'List.py' file using Python (e.g., python List.py).




## Day 6: Tuples
### [click here to open the <b>Tuple.py</b> file](./Day_6/)


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

---

## Day 7: Sets

Welcome to **Day 7** of the **30 Days of Python Coding**! Today, we dive into one of Python's most powerful and versatile data structures: **sets**.

## Introduction to Sets

A **set** is a collection data type in Python that is:

- **Unordered**: The items in a set do not have a defined order.
- **Unindexed**: You cannot access set elements using an index.
- **Immutable (for elements)**: The items in a set must be hashable and cannot be changed after being added. However, the set itself is mutable.
- **No Duplicates**: Sets automatically remove duplicate values.

Sets are particularly useful for operations involving unique elements and for performing mathematical set operations like union, intersection, and difference.

---

## Learning Objectives

By the end of this day, you will learn how to:

1. Create sets in Python.
2. Determine the length of a set.
3. Access and check for items in a set.
4. Add and remove items from a set.
5. Clear and delete sets.
6. Convert lists to sets.
7. Join sets using union and update.
8. Perform mathematical set operations, such as:
   - Intersection
   - Subset
   - Superset
   - Difference
   - Symmetric Difference
9. Practice these skills with hands-on exercises.

---

## Instructions and Examples

### 1. Creating Sets

You can create a set by using curly braces `{}` or the `set()` function.

```python
# Using curly braces
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Using the set() function
numbers = set([1, 2, 3, 4, 5])
print(numbers)
```

### 2. Getting the Length of a Set

Use the `len()` function to determine the number of items in a set.

```python
my_set = {1, 2, 3, 4, 5}
print(len(my_set))  # Output: 5
```

### 3. Accessing and Checking Items in a Set

Sets do not support indexing, but you can check if an item exists using the `in` keyword.

```python
my_set = {"Python", "Java", "C++"}
print("Python" in my_set)  # Output: True
print("Ruby" in my_set)    # Output: False
```

### 4. Adding and Removing Items

- **Add**: Use the `add()` method to add a single item to a set.
- **Update**: Use the `update()` method to add multiple items.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set.update([5, 6, 7])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}
```

- **Remove Items**:
  - `remove(item)`: Removes an item. Raises an error if the item does not exist.
  - `discard(item)`: Removes an item without raising an error.

```python
my_set = {"a", "b", "c"}
my_set.remove("a")
my_set.discard("d")  # No error, even if "d" is not in the set
```

### 5. Clearing and Deleting Sets

- **Clear a set**: Use the `clear()` method to remove all items.
- **Delete a set**: Use the `del` keyword to delete the entire set.

```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

del my_set
```

### 6. Converting Lists to Sets

Convert a list to a set to remove duplicates or perform set operations.

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4, 5}
```

### 7. Joining Sets

Use the `union()` method or the `|` operator to join two sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)  # Or use set1 | set2
print(result)  # Output: {1, 2, 3, 4, 5}
```

### 8. Mathematical Set Operations

- **Intersection**: Use `intersection()` or `&`.
- **Subset and Superset**: Use `issubset()` and `issuperset()`.
- **Difference**: Use `difference()` or `-`.
- **Symmetric Difference**: Use `symmetric_difference()` or `^`.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Intersection
print(A & B)  # Output: {3, 4}

# Subset
print({1, 2}.issubset(A))  # Output: True

# Superset
print(A.issuperset({1, 2}))  # Output: True

# Difference
print(A - B)  # Output: {1, 2}

# Symmetric Difference
print(A ^ B)  # Output: {1, 2, 5, 6}
```

---

## Exercises

### Beginner

1. Create a set containing the numbers 1 to 10.
2. Check if the number 5 exists in the set.
3. Add the number 11 to the set and remove the number 1.

### Intermediate

1. Convert a list with duplicate values into a set.
2. Perform union, intersection, and difference operations on two sets.
3. Write a function to check if a set is a subset of another set.

### Advanced

1. Given two sets, find their symmetric difference without using the `^` operator.
2. Write a program to find common elements in three sets.
3. Create a set from user input and perform various operations (e.g., add, remove, clear).

---

## Running the Code

To run this code, simply execute the 'List.py' file using Python (e.g., python List.py).

---

## Contributions

Feel free to contribute to this repository by adding more code snippets and examples from your own Python coding journey!


## Contributions

Feel free to contribute to this repository by adding more code snippets and examples from your own Python coding journey!
