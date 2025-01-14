# 30 days of python coding

# Day 2 : Variables, Builtin Functions


# Variables
# Valid names for declaring variables
first_name = "Ashik" # first name
last_name = "Ridwan" # last name
full_name = "Ashik Ridwan" # full name
country = "Bangladesh" # country
city = "Dhaka" # city
age = 20 # age
year = 2025 # year
is_married = "yes" # is married
is_true = True # boolean
is_light_on = False # boolean
name, age, country = "Ashik", 20, "Bangladesh" # multiple assignment


# Some built in function

# type()
# Checking data types of variables
print(type(first_name))  # str
print(type(last_name))   # str
print(type(full_name))   # str
print(type(country))     # str
print(type(city))        # str
print(type(age))         # int
print(type(year))        # int
print(type(is_married))  # str
print(type(is_true))     # bool
print(type(is_light_on)) # bool
print(type(name))        # str
print(type(age))         # int
print(type(country))     # str

#len()
print(len(first_name)) # length of the string 5
print(len(last_name)) # length of the string 6

##Arithmetic operations using variables

num_one = 5
num_two = 4

# Arithmetic operations
total = num_one + num_two          # 9
diff = num_one - num_two           # 1
mul = num_one * num_two            # 20
div = num_one / num_two            # 1.25
remainder = num_one % num_two      # 1
exp = num_one ** num_two           # 625
floor_div = num_one // num_two     # 1


## Input()


# Calculating area of a circle with radius of 30
radius = float(input("Enter the radius of a circle: "))
area_of_circle = 3.14 * (radius ** 2) # area = pi * r^2
print(area_of_circle) # 2826.0


# Circumference of a circle with radius of 30
radius = float(input("Enter the radius of a circle: "))
circum_of_circle = 2 * 3.14 * radius # circumference = 2 * pi * r
print(circum_of_circle) # 188.4

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("Full name:",first_name, last_name, ", Country:",country, ", Age:", age)




