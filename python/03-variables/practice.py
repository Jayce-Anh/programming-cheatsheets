###################### PRACTICE ######################

# 1. Declare a first, last and full name variable and assign a value to it
first_name = "Jayce"
last_name = "Anh"
full_name = first_name + " " + last_name

# 2. Declare a country variable and assign a value
country = "Viet Nam"

# 3. Declare a year variable and assign a value
year = 2026

# 4. Declare is_married and assign a value
is_married = False

# 5. Declare is_true and assign a value
is_true = True

# 6. Declare multiple variables on one line
x, y = 10, 20

# 7. Check data types with type()
print(type(x), type(y))
print(type(country))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(full_name))

# 8. Use len() for the length of your first name
print(len(first_name))

# 9. Compare length of first name vs last name
if len(first_name) > len(last_name):
    print("First name is longer than last name")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name")
else:
    print("Both equal length")

# 10. num_one and num_two, then print their sum
num_one = 5
num_two = 4
print(num_one + num_two)  # 9
