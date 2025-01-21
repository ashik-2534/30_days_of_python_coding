
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
        # Enter your age: 30
        # You are old enough to learn to drive.
        # Output:
        # Enter your age: 15
        # You need 3 more years to learn to         drive.                    

user = int(input("Enter your age: "))
if user >= 18:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")
    print(f"Please wait for {18 - user} more years.")


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
        # Enter your age: 30
        # You are 5 years older than me.

my_age = 20
your_age = int(input("Enter your age: "))
if your_age != my_age:
    if my_age+1 == your_age:
        print("You are one year older than me.")
    elif my_age-1 == your_age:
        print("You are one year younger than me.")
    elif your_age > my_age:
        print(f"You are {your_age - my_age} years older than me.")
    else:
        print(f"You are {my_age - your_age} years younger than me.")
else:
    print("We are the same age.")



# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
    # Enter number one: 4
    # Enter number two: 3
    # 4 is greater than 3\

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{b} is greater than {a}.")
else:
    print(f"{a} and {b} are equal.")


# Write a code which gives grade to students according to theirs scores:
        # 80-100, A
        # 70-89, B
        # 60-69, C
        # 50-59, D
        # 0-49, F

stu_scr = int(input("Enter your score: "))
if stu_scr<100 and stu_scr>0:
        if stu_scr>=80:
            print("Your grade is A")
        elif stu_scr>=70:
            print("Your grade is B")
        elif stu_scr>=60:
            print("Your grade is C")
        elif stu_scr>=50:
            print("Your grade is D")
        else:
            print("Your grade is F.\nYou failed the exam.")
else:
    print("Invalid score.\nPlease enter a score between 0 and 100.")


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
sesn_atmn = ["september", "october ", "november"]
sesn_win = ["december", "january", "february"]
sesn_spr = ["march", "april", "may"]
sesn_smr = ["june", "july", "august"]

mnth = input("Enter a month to check the season: ").lower()

if mnth in sesn_atmn:
    print("The season is Autumn.")
elif mnth in sesn_win:
    print("The season is Winter.")
elif mnth in sesn_spr:
    print("The season is Spring.")
elif mnth in sesn_smr:
    print("The season is Summer.")
else:
    print("Invalid month.")


# ```
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
usr_frt = input("Enter a fruit name: ").lower()

if usr_frt in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(usr_frt)
    print(fruits)

# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node','MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
        #Asabeneh Yetayeh lives in Finland. He is married.

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(skills[middle_index])


if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill")
    else:
        print("The person does not have Python skill")

if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif set(skills) == {'Node', 'Python', 'MongoDB'}:
        print("He is a backend developer")
    elif set(skills) == {'React', 'Node', 'MongoDB'}:
        print("He is a fullstack developer")
    else:
        print("unknown title")

if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")


