
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    
    return a + b
print(add_two_numbers(3, 5)) # Output: 8

# Area of a circle is calculated as follows: area = π x r x r.
# Write a function that calculates area_of_circle.
def area_of_circle(r):
    Area = 3.1416 * r * r
    
    return Area
print(area_of_circle(5)) # Output: 78.5


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
temp_celsius = 0
def convert_celsius_to_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    temp_celsius += temp_fahrenheit
    return temp_celsius
print(convert_celsius_to_fahrenheit(32))


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    """
    This function takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
    """
    seasons = {
        "September": "Autumn",
        "October": "Autumn",
        "November": "Autumn",
        "December": "Winter",
        "January": "Winter",
        "February": "Winter",
        "March": "Spring",
        "April": "Spring",
        "May": "Spring",
        "June": "Summer",
        "July": "Summer",
        "August": "Summer"
    }
    return seasons[month]
print(check_season("September"))

#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(2, 2, 6, 10))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(input_list):
    if type(input_list) == list:
        for item in input_list:
            print(item)
    else:
        print("Input is not a list")
my_list = [1 ,2 ,3]
print_list(my_list)

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(input_list):
    reverse_list = []
    for mod_list in input_list:
        reverse_list.insert(0, mod_list)
    return reverse_list
my_list = [1 ,2 ,3]
print(reverse_list(my_list))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(input_list):
    list = []
    for item in input_list:
        list.append(item.capitalize())
    return list
my_list = ['a', 'b', 'c']
print(capitalize_list_items(my_list))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(input_list, item):
    input_list.append(item)
    return input_list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(input_list, item):
    input_list.remove(item)
    return input_list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(input_num):
    sum = 0 
    for i in range(input_num + 1):
        sum += i
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odd(input_num):
    sum = 0
    for i in range(input_num + 1):
        if i % 2 != 0:
            sum += i
    return sum
print(sum_of_odd(5))  # 9

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_ever(input_num):
    sum = 0 
    for i in range(input_num + 1):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_ever(10))  # 30

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds (num):
    evn_num = 0
    odd_num = 0
    for i in range(num + 1):
        if i % 2 == 0:
            evn_num += 1
        else:
            odd_num += 1
    return evn_num,odd_num
    
evn_num, odd_num = evens_and_odds(100)
print(f"The number of evens are {evn_num}\nThe number of odds are {odd_num}")
    # The number of odds are 50.
    # The number of evens are 51.

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    if num < 0:
        print ("Please enter a positive number.")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5)) # 120

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(num):
    if num == None:
        return True
    elif isinstance(num, (str, list, tuple, dict, set)):
        return len(num) == 0
    else:
        return False

print(is_empty(None))  # True
print(is_empty([]))    # True
print(is_empty(" "))   # False
print(is_empty({}))    # True
print(is_empty(set())) # True

# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num < 2 :
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(2)) # True
print(is_prime(7)) # True
print(is_prime(8)) # False

# Write a functions which checks if all items are unique in the list.
def all_unique(my_list):
    return len(my_list) == len(set(my_list))

print(all_unique([1, 2, 3, 4, 5]))       # True
print(all_unique([1, 2, 2, 3, 4, 5, 1])) # False

# Write a function which checks if all the items of the list are of the same data type.
def same_type(input_list):
    if not input_list:
        return True
    check_type = type(input_list[0])
    for item in input_list:
        if isinstance(item, check_type):
            return True
    return False
print(same_type([]))           # True
print(same_type([1, 2, 3]))    # True
print(same_type([1, 2, "3"]))  # False

# Write a function which check if provided variable is a valid python variable
def is_valid(input_var):
    if isinstance(input_var, str) and input_var.isidentifier():
        return True
    return False

print(is_valid("name"))      # True
print(is_valid(1))           # False
print(is_valid("1name"))     # False
print(is_valid("variable"))  # True
print(is_valid("123"))       # False
print(is_valid("_valid"))    # True


