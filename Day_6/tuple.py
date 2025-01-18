
#Create an empty tuple
emt_tpl = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
#Join brothers and sisters tuples and assign it to siblings

sisters = ("Asha", "Fariha", "Tasnim")
brothers = ("Rafi", "Saif", "Sajid")
siblings = sisters + brothers

#How many siblings do you have?
print(len(siblings))


#Modify the siblings tuple and add the name of your father and mother and assign it to family_members

siblings = list(siblings)
siblings.insert(0, "Ayesha")
siblings.insert(1, "Rakib")
family_members = tuple(siblings)
print(family_members)

#Unpack siblings and parents from family_members
father, mother, *siblings = family_members
print(father, mother, siblings)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "cherry")
vegetables = ("tomato", "potato", "carrot")
animal =  ("dog", "cat", "mouse")
food_stuff_tp = fruits + vegetables + animal

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[1:-1])# output: ['banana', 'cherry', 'tomato', 'potato', 'carrot', 'dog', 'cat']

#Slice out the first three items and the last three items from food_staff_lt list

print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
print("apple" in food_stuff_tp)

# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
