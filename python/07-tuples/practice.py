########################## Practice #########################

# 1. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Maria", "Suzy", "Mia", "Caitlyn")
brothers = ("Joe", "Max")

# 2. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

# 3. How many siblings do you have?
print(len(siblings))

# 4. Add father and mother; assign to family_members
parents = ("Tom", "Laura")
family_members = siblings + parents
print(family_members)

# 5. Unpack siblings and parents from family_members
# Last two items are parents; everything before that is siblings (* captures a list of the rest)
*all_siblings, father, mother = family_members
print("siblings:", all_siblings)
print("parents:", father, mother)
