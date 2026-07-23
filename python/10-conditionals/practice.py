################## PRACTICE ####################
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 
age = int(input("Enter your age: "))
print(age)
if age >= 18:
    print("You are old enough to drive")
else:
    print(f'You need {18 - age} more years to drive')


# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 25
your_age = int(input("Enter your age: "))
print(your_age)
if your_age > my_age:
    if your_age - my_age != 1:
        print(f'You are {your_age - my_age} years older than me')
    else: 
        print(f'You are 1 year older than me')
elif your_age < my_age:
    if my_age - your_age != 1:
        print(f'You are {my_age - your_age} years younger than me')
    else: 
        print(f'You are 1 year younger than me')
else:
    print('We are the same age')

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b.
# If a is less b return a is smaller than b, else a is equal to b.
a = int(input('Enter number one: '))
b = int(input('Enter number two '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

# 4. Write a code which gives grade to students according to theirs scores:
'''
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''

score = int(input("Your scores: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if 90 <= score <= 100:
        print(f'{score}, A')
    elif 80 <= score < 90:
        print(f'{score}, B')
    elif 70 <= score < 80:
        print(f'{score}, C')
    elif 60 <= score < 70:
        print(f'{score}, D')
    else: 
        print(f'{score}, F')
