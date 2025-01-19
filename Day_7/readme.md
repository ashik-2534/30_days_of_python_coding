# 30 Days of Python Coding

#### ======================================

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
