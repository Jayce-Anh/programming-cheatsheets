################## PRACTICE ##################

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
i = 0
while i < 10: 
    i += 1
    print(i)

# 2. Iterate 10 to 0 using for loop, do the same using while loop.

while i > 0:
    i -= 1
    print(i)


# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

for e in range(1,8):
    print('#'*e)
 

# 4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for e in range(1,9):
    print('# '*8)

# 5. Print the following pattern:
'''
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''
for n in range(11):
    print(f'{n} x {n} = {n * n}')


# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for x in lst:
    print(x)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
# range(0, 101) → 0 through 100 (the end value 101 is excluded)
for y in range(0, 101):
    if y % 2 == 0:
        print(y)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for y in range(0, 101):
    if y % 2 != 0:
        print(y)

# 9. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
total = 0
for z in range(0, 101):
    total += z
print(f'Sum: {total}')

# 10. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum_even = 0
sum_odd = 0
for v in range(0, 101):
    if v % 2 == 0:
        sum_even += v
    else:
        sum_odd += v
print(f'The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}')

