import pickle

with open('recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print("Recipe details - ")
print("Name: " + recipe['name'])
print("Ingredients: ", recipe['ingredients'])
print("Cooking time (mins): " + str(recipe['cooking_time']))
print("Difficulty: " + recipe['difficulty'])
