#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Thirty" + " " + "Days" + " " + "Of" + " " + "Python")

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Coding"+" " + "For" +" "+"All")

#Declare a variable named company and assign it to an initial value "Coding For All".
#Print the variable company using print().
company = "Coding For All"
print(company)

#Print the length of the company string using len() method and print().
print(len(company)) # length is 14

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of 'Coding For All' string.
company = "Coding For All"
print(company[:7])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company) # True

#Replace the word coding in the string 'Coding For All' to Python.
print("Coding For All".replace("Coding", "Python"))

#Change Python for Everyone to Python for All using the replace method or other methods.
var_sen = "Python for Everyone"
var_sen = var_sen.replace("Everyone", "All")
print(var_sen)

#Split the string 'Coding For All' using space as the separator (split()) .
var_str = "Coding For All"
var_str = var_str.split(" ")
print(var_str)

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
var_str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
var_str = var_str.split(",")
print(var_str)

#What is the character at index 0 in the string Coding For All.
var_str = "Coding For All"
print(var_str[0])

#What is the last index of the string Coding For All.
var_str = "Coding For All"
var_str = len(var_str)-1
print(var_str)

#What character is at index 10 in "Coding For All" string.

