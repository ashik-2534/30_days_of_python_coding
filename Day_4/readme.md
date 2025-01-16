# 30 Days of Python Coding
## -------------------------------
## -------------------------------

## Day 4: Strings

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

## Contributions
Feel free to contribute to this repository by adding more code snippets and examples from your own Python coding journey!