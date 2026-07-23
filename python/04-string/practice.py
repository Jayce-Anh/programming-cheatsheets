###################### PRACTICE ######################
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string1 = 'Thirty' + " " + 'Days' + " " + 'Of' + " " + 'Python'
print(string1)

# 2. Declare a variable named str1 and assign it to an initial value "Coding For All".
str1 = "Coding For All"

# 3. Print the variable using print().
print(str1)

# 4. Print the length of the company string using len() method and print().
print(len(str1))

# 5. Change all the characters to uppercase letters using upper() method.
print(str1.upper())

# 6. Change all the characters to lowercase letters using lower() method.
print(str1.lower())

# 7. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(str1.capitalize())
print(str1.title())
print(str1.swapcase())

# 8. Cut(slice) out the first word of Coding For All string.
print(str1[0:6])

# 9. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(str1.find("Coding"))

# 10. Replace the word Coding in the string 'Coding For All' with Python.
print(str1.replace("Coding", "Python"))

# 11. Change "Coding for All" to "Python for All" using replace (use the string that actually appears).
print(str1.replace("Coding for Everyone", "Python for All"))

# 12. Split the string 'Coding For All' using space as the separator (split()).
print(str1.split(" "))

# 13. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
faang = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(faang.split(", "))

# 14. What is the character at index 0 in the string Coding For All.
print(str1[0])

# 15. What is the last index of the string Coding For All.
print(len(str1) - 1)

# 16. What character is at index 10 in "Coding For All" string.
print(str1[10])

# 17. Create an acronym or an abbreviation for the name 'Python For Everyone'.
str2 = 'Python For Everyone'
print((str2[0]) + (str2[7]) + (str2[11]))

# 18. Create an acronym or an abbreviation for the name 'Coding For All'.
print((str1[0]) + (str1[7]) + (str1[11]))

# 19. Use index to determine the position of the first occurrence of C in Coding For All.
print(str1.index("C"))

# 20. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = 'You cannot end a sentence with because because because is a conjunction'
print(text.find("because"))
