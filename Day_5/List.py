#Declare an empty list
my_list = []

#Declare a list with more than 5 items
#Find the length of your list
my_list = [1,2,3,4,5,6]
print(len(my_list))

#Get the first item, the middle item and the last item of the list
print(f"The first item {my_list[0]}, middle items {my_list[2]},{my_list[3]} and last item {my_list[-1]}")

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Ashik", 20, 5.7, True, "Dhaka"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
#Print the list using print()


it_companies = [ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first company, middle and last company
print(f"The first company {it_companies[0]}, middle company {it_companies[3]} and last company {it_companies[-1]}")

#Print the list after modifying one of the companies
# Add a new IT company to it_companies
#Insert an IT company in the middle of the companies list
#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = [ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]
it_companies.append("TCS")
it_companies.insert(3, "Infosys")
it_companies[1] = it_companies[1].upper()
print(it_companies)

#Join the it_companies with a string '#;  '
it_companies = [ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]
print("#; ".join(it_companies))

#Sort the list using sort() method
#Reverse the list in descending order using reverse() method
it_companies = [ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

#Slice out the first 3 companies from the list
#Slice out the last 3 companies from the list
#Slice out the middle IT company or companies from the list
it_companies = [ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]
print(it_companies[:3])
print(it_companies[-3:])
print(it_companies[1:-1])

#Remove the first IT company from the list
#Remove the middle IT company or companies from the list
#Remove the last IT company from the list
#Remove all IT companies from the list
#Destroy or delete the IT companies list


it_companies.pop(0)
print(it_companies)

it_companies = it_companies[1:-1]
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
# After joining the list. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
joined_list = front_end + back_end
full_stack = joined_list.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
print(ages)
print(min(ages), max(ages))

# Add the min age and the max age again to the end of the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)

#Find the median age (one middle item or two middle items divided by two)
#Find the average age (sum of all items divided by their number)

ages.sort()
print(ages)
med_age = len(ages)/2
print(ages[med_age])
avg = sum(ages)/len(ages)
print(avg)
rng_ages = max(ages) - min(ages)
print(rng_ages)





