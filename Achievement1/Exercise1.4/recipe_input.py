import pickle

# take_recipe function for user input
def take_recipe():
    name = input('Enter recipe name: ')
    cooking_time = int(input('Enter cooking time (mins): '))
    ingredients =  set(input('Enter ingredients: ').split(', '))
    recipe = {
      'name': name, 
      'cooking_time': cooking_time, 
      'ingredients': ingredients,
      'difficulty': ""
    }
    # calculate recipe diffulty
    def calc_difficulty():
        if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
            recipe['difficulty'] = 'Easy'

        elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
            recipe['difficulty'] = 'Medium'

        elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
            recipe['difficulty'] = 'Intermediate'

        elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
            recipe['difficulty'] = 'Hard'
    calc_difficulty()

    return recipe

# Prompt to open user defined filename
filename = input("Enter filename of your stored recipes: ") + '.bin'

# Loads file if exists
try:
   file = open(filename, 'rb')
   data = pickle.load(file)
   print("Recipe added.")

# Creates new binary file if file not found
except FileNotFoundError:
   print("File doesn't exist - creating new file.")
   data = {
        'recipes_list': [],
        'all_ingredients': set()
  }

# Creates new binary file if other error occurs
except:
   print("An unknown error occurred - creating new file.")
   data = {
        'recipes_list': [],
        'all_ingredients': set()
  }

# Closes file (opened in try block) if no errors
else:
   file.close()

# Extracts values from dictionary into recipe and ingredient lists 
finally:
   recipes_list = data['recipes_list']
   all_ingredients = data['all_ingredients']

# prompt for user defined recipe number(s) to input
n = int(input('How many recipes would you like to enter?: '))

# iterate through recipe numbers (n)
for i in range(n):
    recipe = take_recipe()

    # check if ingredient to be added to ingredient list
    for ingredient in recipe['ingredients']:
      # adds ingredient if not in list
        all_ingredients.add(ingredient)

    # adds recipe to recipe list
    recipes_list.append(recipe)

# creates updated dictionary named 'data' with recipes and ingredients
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

# Opens user defined filename and writes data to it using pickle method
updated_file = open(filename, 'wb')
pickle.dump(data, updated_file)

updated_file.close()
print('Recipes updated, goodbye.')