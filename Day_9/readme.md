[<<Day 8](../Day_8/) | <b>Day 9</b> | [Day 10>>](../Day_10/)


# 30 Days of Python Coding

#### ======================================

## Day 9: Conditionals

Welcome to **Day 9** of the **30 Days of Python Coding** challenge! Today, we'll dive deep into one of the most crucial concepts in programming: **Conditional Statements**. Conditional statements allow your programs to make decisions and execute different code depending on specific conditions.

## Learning Objectives

By the end of this tutorial, you'll be able to:

1. Use `if` statements to execute code based on a condition.
2. Use `if-else` to handle binary decisions.
3. Use `if-elif-else` for handling multiple conditions.
4. Write shorter conditional statements with shorthand techniques.
5. Handle complex logic with nested conditions.
6. Combine conditions using logical operators (`and`, `or`, `not`).

Let’s get started!

---

## Topics Covered

### 1. If Condition

The simplest form of conditional statement:

```python
# Example
age = 20
if age >= 18:
    print("You are an adult.")
```

- **Explanation**: If the condition `age >= 18` is true, the indented block of code is executed.

### 2. If-Else

Handle binary decisions with `if-else`:

```python
# Example
number = 10
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

- **Explanation**: If the condition `number % 2 == 0` is true, the first block runs; otherwise, the block under `else` runs.

### 3. If-Elif-Else

For multiple conditions:

```python
# Example
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

- **Explanation**: Conditions are checked sequentially, and the first one that evaluates to true is executed.

### 4. Shorthand

Write shorter conditions:

```python
# Example
x = 5
y = 10
print("x is smaller") if x < y else print("x is larger or equal")
```

- **Explanation**: This is a compact way to write conditional expressions.

### 5. Nested Conditions

Place conditions inside other conditions:

```python
# Example
age = 25
if age >= 18:
    if age >= 21:
        print("You can drink and vote.")
    else:
        print("You can vote but cannot drink.")
```

- **Explanation**: Use nested conditions for complex logic.

### 6. If Condition and Logical Operators

Combine multiple conditions using logical operators:

```python
# Example
x = 7
y = 15
if x > 5 and y > 10:
    print("Both conditions are true.")
if x < 10 or y < 5:
    print("At least one condition is true.")
if not (x > 10):
    print("x is not greater than 10.")
```

- **Explanation**: Logical operators like `and`, `or`, and `not` help combine or invert conditions.

---

## Interactive Examples

Try the following code snippets and see how they behave with different inputs:

### Example 1: Leap Year Checker

```python
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

### Example 2: Grading System

```python
score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is {grade}.")
```

---

## Practice Exercises

### Level 1: Easy

1. Write a program to check if a number is positive, negative, or zero.
2. Check if a given string contains the letter "a".

### Level 2: Intermediate

1. Write a program to determine if a triangle is valid based on its angles.
2. Create a program that takes a temperature in Celsius and categorizes it as "cold", "warm", or "hot".

### Level 3: Advanced

1. Develop a basic chatbot using nested conditions to respond to user inputs.
2. Write a program to validate a password based on conditions like length, inclusion of numbers, and special characters.

---

## Running the Code

To run this code, simply execute the 'Conditionals.py' file using Python (e.g., python Conditionals.py).

---

## Contributions

Feel free to contribute to this repository by adding more code snippets and examples from your own Python coding journey!

---

Happy coding! 🎉

[<<Day 8](../Day_8/) | <b>Day 9</b> | [Day 10>>](../Day_10/)
