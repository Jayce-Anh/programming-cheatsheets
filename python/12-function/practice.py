################## PRACTICE ##################

# 1. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    for value in args:
        if not isinstance(value, (int, float)):
            return f"Error: '{value}' is not a number"
    return sum(args)

print(add_all_nums(1,2,6,7,12,-5,4.5))
print(add_all_nums(1,2,4,"hello",53,2.4))

# 2. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to_fahrenheit (use underscores, not hyphens).

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print(f"-> °F: {convert_celsius_to_fahrenheit(float(input('°C: ')))}")

# 3. Write a function called check_season (no hyphens). Month 1-12; returns the season (Northern hemisphere).
# Winter: Dec–Feb  |  Spring: Mar–May  |  Summer: Jun–Aug  |  Autumn: Sep–Nov

def check_season(month):
    m = int(month)
    if m in (12, 1, 2):
        return "Winter"
    elif m in (3, 4, 5):
        return "Spring"
    elif m in (6, 7, 8):
        return "Summer"
    elif m in (9, 10, 11):
        return "Autumn"
    else:
        return "Invalid month"


print(f"Season: {check_season(input('Enter month (1-12): '))}")

# 4. Write a function called calculate_slope which return the slope of a linear equation
# For points (x1, y1) and (x2, y2):
# m = (y2 − y1) / (x2 − x1)
# If x1 == x2, the line is vertical, slope is undefined → the function raises ValueError.

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        raise ValueError("Vertical line: x1 == x2, slope undefined")
    return (y2 - y1)/(x2 - x1)

print(calculate_slope(3,4,2,4))

# 5. Declare a function named evens_and_odds.
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
'''
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
'''
def evens_and_odds(num):
    num = int(num)
    even = 0
    odd = 0
    for i in range(num+1):
        if i % 2 == 0:
            even += 1 
        if i % 2 != 0:
            odd += 1
    return f"The number of odds are {odd}.\nThe number of evens are {even}."

print(evens_and_odds(input(f"Enter number: ")))   
