########################## PRACTICE ##########################

# 1. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 2. Print the list using print()
print(it_companies)

# 3. Print the number of companies in the list
print(len(it_companies))

# 4. Print the first, middle and last company
middle_index = len(it_companies) // 2
print(it_companies[0], it_companies[middle_index], it_companies[-1])

# 5. Print the list after modifying one of the companies
it_companies[0] = "Meta"  
print(it_companies)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# 6. Sort the list and find the min and max age
ages.sort()  # sorts in place; returns None — do not assign to a variable
print(ages)
print(min(ages), max(ages))

# 7. Add the min age and the max age again to the list
ages.append(min(ages)) 
ages.append(max(ages))
print(ages)

# 8. Find the median age (one middle item or two middle items divided by two)
for i in ages:
    if i % 2 == 0:
        print(i)

# 9. Find the average age (sum of all items divided by their number )
avg = sum(ages)/len(ages)
print(avg)
# 10. Find the range of the ages (max minus min)
range = max(ages) - min(ages)
print(range)

# 11. Compare the value of (min - average) and (max - average), use abs() method
# abs() takes one number at a time — compute each distance from the average separately
dist_min = abs(min(ages) - avg)
dist_max = abs(max(ages) - avg)
print(dist_min, dist_max)
print(dist_min < dist_max, dist_min > dist_max, dist_min == dist_max)
