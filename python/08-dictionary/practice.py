######################### PRACTICE ##########################
# 1. Create an empty dictionary called game
game = {}
# 2. Add name, types, year, rating, company, pc to the games dictionary
game = {"name": "Elden Ring", "types": "Soul", "year": 2022, "rating": 10, "company": "FromSoftware", "pc": True }
print(game)
# 3. Get the length of the game dictionary
print(len(game))
# 4. Get the value of rating and check the data type
print(game["rating"])
print(type(game["rating"]))

# 5. Modify the rating values and adding dlc key and values
game["rating"] = 9.5
game["dlc"] = True
print(game)

# 6. Get the dictionary keys as a list
print(list(game.keys()))
# 7. Get the dictionary values as a list
print(list(game.values()))