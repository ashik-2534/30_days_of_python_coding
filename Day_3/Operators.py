# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
age = 18
height = 5.11
complex_number = 2 + 3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    #-->Enter base: 20
    #-->Enter height: 10
    #-->The area of the triangle is 100

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
area_of_triangle = (base * height) / 2
print(int(area_of_triangle))

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    # Enter side a: 5
    # Enter side b: 4
    # Enter side c: 3
    # The perimeter of the triangle is 12


side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(int(perimeter))



# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rec_length = int(input("Enter the length of rectangle: "))
rec_width = int(input("Enter the width of rectangle: "))
perimeter = 2 * (rec_length + rec_width)
print(int(perimeter ))


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius of a circle: "))
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = (2 / -2)
print(slope)
x_intercept = (-2 / 2)
print(x_intercept)
y_intercept = 2 * -2
print(y_intercept)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope = (10 - 2) / (6 - 2)
print(slope)
distance = ((10 - 2) ** 2 + (10 - 2) ** 2) ** 0.5
print(distance)

#compare the previous slopes
slope_1 = (10 - 2) / (6 - 2)
print(slope_1)    
slope_2 = (8 - 3) / (5 - 2)
print(slope_2)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = int(input("Enter the value of x: "))
y = x ** 2 + 6 * x + 9
print(y)

#Find the length of 'python' and 'dragon' and make a false comparison statement.
len_python = len('python')
len_dragon = len('dragon')
print(len_python == len_dragon)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on' in 'python' and 'on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print('jargon' in 'I hope this course is not full of jargon.')

#Find the length of the text python and convert the value to float and convert it to string
str_py = str(float(len('python')))
print(str_py)

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div = 7 // 3
value = int(2.7)
print(floor_div == value)

#Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10 )

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year = int(input("Enter number of years you have lived: "))
seconds = int(year * 31536000) #1year = (365 * 24 * 60 * 60)seconds






