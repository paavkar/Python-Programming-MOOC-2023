# Write your solution here
def search_by_name(filename: str, word: str):
    recipes_found = []
    recipe = []
    with open(filename) as file:
        for line in file:
            if(not line.isspace()):
                if (line not in recipe):
                    recipe.append(line.strip())
            else:
                if word in recipe[0].lower():
                    recipes_found.append(recipe[0])
                recipe = []
        if word in recipe[0].lower():
                    recipes_found.append(recipe[0])
    return recipes_found

def search_by_time(filename: str, prep_time: int):
    recipes_found = []
    recipe = []
    with open(filename) as file:
        for line in file:
            if(not line.isspace()):
                if (line not in recipe):
                    recipe.append(line.strip())
            else:
                if int(recipe[1]) <= prep_time:
                    recipes_found.append(f"{recipe[0]}, preparation time {int(recipe[1])} min")
                recipe = []
        if int(recipe[1]) <= prep_time:
            recipes_found.append(f"{recipe[0]}, preparation time {int(recipe[1])} min")
    return recipes_found

def search_by_ingredient(filename: str, ingredient: str):
    recipes_found = []
    recipe = []
    with open(filename) as file:
        for line in file:
            if(not line.isspace()):
                if (line not in recipe):
                    recipe.append(line.strip())
            else:
                for i in range(2, len(recipe)):
                    if(ingredient == recipe[i]):
                        recipes_found.append(f"{recipe[0]}, preparation time {int(recipe[1])} min")
                recipe = []
        for i in range(2, len(recipe)):
            if(ingredient == recipe[i]):
                recipes_found.append(f"{recipe[0]}, preparation time {int(recipe[1])} min")
    return recipes_found


### Example solution

def read_file(filename):
    with open(filename) as file:
        rows = []
        for row in file:
            rows.append(row.strip())
 
    recipes = []
    name_in_row = True
    prep_time_in_row = True
    new = { "ingredients": []}
    for row in rows:
        if name_in_row:
            new["name"] = row
            name_in_row = False
            prep_time_in_row = True
        elif prep_time_in_row:
            new["prep_time"] = int(row)
            prep_time_in_row = False
        elif len(row) > 0:
            new["ingredients"].append(row)
        else:
            recipes.append(new)
            name_in_row = True
            new = {"ingredients": []}
    recipes.append(new)
 
    return recipes
 
def search_by_name(filename: str, word: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
 
    return found
 
def search_by_time(filename: str, time: int):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if recipe["prep_time"] <= time:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found
 
def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if ingredient.lower() in recipe["ingredients"]:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found