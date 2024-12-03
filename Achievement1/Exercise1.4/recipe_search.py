import pickle

# Function to take one recipe as argument and print all attributes
def display_recipe(recipe):
    print("Recipe: ", recipe['name'])
    print("Cooking time (mins): ", recipe['cooking_time'])
    print("Ingredients: ")
    for ingredient in recipe['ingredients']:
      print(ingredient)
    print("Difficulty level: ", recipe['difficulty'])
   
# Function to search for ingredient in data   
def search_ingredient(data):
    all_ingredients = enumerate(data['all_ingredients'])
    numbered_ingredients = list(all_ingredients)

    # Print ingredient with indexed number
    print('Ingredients Available Across All Recipes')
    print('========================================')
    for ingredient in numbered_ingredients:
        print(ingredient[0], ingredient[1])

    # Search user inputted number
    try:
        number = int(input("Select ingredient number to search: "))
        ingredient_searched = numbered_ingredients[number][1]
        print("Looking for ingredient selected....")
    # Informs user input incorrect if integer not entered
    except ValueError:
        print("Input incorrect, please enter a number only")
    except:
        print("An unexpected error occurred - please enter a listed number only") 
    # Prints recipe(s) containing selected ingredient    
    else:
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)

# Opens and loads user inputted filename
filename = input("Enter filename where you've stored your recipes: ") + '.bin'
        
try:
    file = open(filename, 'rb')
    data = pickle.load(file)
    print("File loaded.")

except FileNotFoundError:
    print("Filename doesn't exist")

else:
    search_ingredient(data)
    file.close()
    