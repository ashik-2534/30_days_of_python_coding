[<<Day 2](../Day_2/) | **Day 3** | [Day 4>>](../Day_4/)

# 30 Days of Python Coding
==========================

## Day 3: Operators
--------------------

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


## Contributions

Feel free to contribute to this repository by adding more code snippets and examples from your own Python coding journey!


[<<Day 2](../Day_2/) | **Day 3** | [Day 4>>](../Day_4/)
