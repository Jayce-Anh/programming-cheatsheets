###################### PRACTICE #######################
tech_companies = {'Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Find the length of the set tech_companies
print(len(tech_companies))

# 2. Add 'Open AI' to tech_companies
tech_companies.add('Open AI')
print(tech_companies)

# 3. Insert multiple companies at once to the set tech_companies
tech_companies.update(['NVIDIA', 'SpaceX', 'TSMC'])
print(tech_companies)

# 4. Remove one of the companies from the set tech_companies
tech_companies.remove('SpaceX')
print(tech_companies)

# 5. Join A and B
print(A.union(B))

# 6. Find A intersection B
print(A.intersection(B))

# 7. Join A with B and B with A
print(A|B)
print(B|A)

# 8. Check if s A subset of B
print(A.issubset(B))
