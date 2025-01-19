# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# print(len(it_companies))
# add a new item to the set
it_companies.add("Twitter")
# update the set with multiple items
it_companies.update(["TCS", "Infosys"])
# remove an item from the set
it_companies.remove("Twitter")
# remove an item from the set or do nothing if it does not exist
it_companies.discard("Twitter")
# print the set
print(it_companies)


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Perform union operation between sets A and B
A_union_B = A.union(B)

# Perform intersection operation between sets A and B
A_intersection_B = A.intersection(B)

# Check if A is a subset of B
is_A_subset_B = A.issubset(B)

# Check if A and B are disjoint sets
are_A_B_disjoint = A.isdisjoint(B)

# Print the union of A and B
print(A_union_B)

# Print the union of B and A
print(B.union(A))

# Print the symmetric difference between sets A and B
print(A.symmetric_difference(B))

# Delete sets A and B
del A
del B


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(age_st)
bth_lth1 = len(age_st) > len(age)
print(f"age_st is bigger than age:{bth_lth1}")
bth_lth2 =  len(age) > len(age_st)
print(f"age is bigger than age_st:{bth_lth2}")



# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sen = "I am a teacher and I love to inspire and teach people."
wrd = sen.split()
wrd_st = set(wrd)
unc_wrd = len(wrd_st)
print(f"I have {unc_wrd} unique words")