# empty lists
recipes_list = []
ingredients_list = set()

# take_recipe function for user input
def take_recipe():
    name = input('Recipe name: ')
    cooking_time = int(input('Cooking time (mins): '))
    ingredients =  list(input('Ingredients: ').split(', '))
    recipe = {
      'name': name, 
      'cooking_time': cooking_time, 
      'ingredients': ingredients
    }
    return recipe

# prompt for user recipe number
n = int(input('How many recipes would you like to enter?: '))

# iterate through recipe numbers
for i in range(n):
    recipe = take_recipe()

    # check if ingredient to be added to ingredient list
    for ingredient in recipe['ingredients']:
      ingredients_list.add(ingredient)

    recipes_list.append(recipe)

# Iterate through ingredients and cooking time in recipe list to determine difficulty
for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Easy'

    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Medium'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Intermediate'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Hard'

# Prints recipe using values from Recipe Dictionary and difficulty level
for recipe in recipes_list:
  print('Recipe: ', recipe['name'])
  print('Cooking time (mins): ', recipe['cooking_time'])
  print('Ingredients: ')
  for ingredient in recipe['ingredients']:
    print(ingredient)
  print('Difficulty level: ', recipe['difficulty'])

# Sorts and prints ALL ingredients in alphabetical order
def all_ingredients():
  print('Ingredients Available Across All Recipes')
  print('========================================')
  new_ingredients_list_sorted = sorted(ingredients_list)
  for ingredient in new_ingredients_list_sorted:
    print(ingredient)

all_ingredients()


