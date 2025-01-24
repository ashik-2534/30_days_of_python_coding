[<<Day 4](../Day_4/) | **Day 5** | [Day 6>>](../Day_6/)

# 30 Days of Python Coding
=====================================

## Day 5: Lists

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

## Contributions
Feel free to contribute to this repository by adding more code snippets and examples from your own Python coding journey!

[<<Day 4](../Day_4/) | **Day 5** | [Day 6>>](../Day_6/)
