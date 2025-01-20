# Create an empty dictionary called dog
dict_dog = {}

# Add name, color, breed, legs, age to the dog dictionary

dict_dog["name"] = "Lassie"
dict_dog["color"] = "black"
dict_dog["breed"] = "collie"
dict_dog["legs"] = 4
dict_dog["age"] = 10

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

std_dct = {
    "frist_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 30,
    "marital_status": "single",
    "skills": ["Python", "SQL"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main St"
}

# Get the length of the student dictionary
std_ln = len(std_dct)
print(std_ln)

# Get the value of skills and check the data type, it should be a list
skl_typ =type(std_dct.get("skills"))
print(skl_typ)

# Modify the skills values by adding one or two skills
std_dct.get("skills").append("Java")
std_dct.get("skills").append("C++")
print(std_dct)

# Get the dictionary keys as a list
# Get the dictionary values as a list
# Change the dictionary to a list of tuples using items() method
st_key = std_dct.keys()
st_val = std_dct.values()
st_itm = std_dct.items()
print(st_key)
print(st_val)
print(st_itm)

# Delete one of the items in the dictionary
# Delete one of the dictionaries
del std_dct["frist_name"]
print(std_dct)
del std_dct

