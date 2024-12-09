# Define new class 'Recipe'
class Recipe(object):
  all_ingredients = set()

  def __init__(self, name, cooking_time):
    self.name = name
    self.cooking_time = cooking_time
    self.ingredients = set()
    self.difficulty = None
  
  # Getter method for name
  def get_name(self):
    return self.name
  # Setter method for name    
  def set_name(self, name):
    self.name = name 

  # Getter method for cooking time
  def get_cooking_time(self):
    return self.cooking_time
  # Setter method for cooking_time
  def set_cooking_time(self, cooking_time):
    self.cooking_time = cooking_time

  # Method to add ingredients
  def add_ingredients(self, *args):
    # for ingredient in args:
    #   if ingredient not in self.ingredients:
    #     self.ingredients.append(ingredient)
    self.ingredients.update(args)
    self.update_all_ingredients()
  # Getter method for ingredients    
  def get_ingredients(self):
    return sorted(self.ingredients)
  
  # Method to calculate recipe difficulty
  def calculate_difficulty(self):
        ingredient_len = len(self.ingredients)

        if self.cooking_time < 10 and ingredient_len < 4:
            self.difficulty = 'Easy'
        elif self.cooking_time < 10 and ingredient_len >= 4:
            self.difficulty = 'Medium'
        elif self.cooking_time >= 10 and ingredient_len < 4:
            self.difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and ingredient_len >= 4:
            self.difficulty = 'Hard'

  # Getter method for recipe difficulty
  def get_difficulty(self):
     if self.difficulty is None: 
        self.calculate_difficulty()
     return self.difficulty

  # Method to search for specific ingredient
  def search_ingredient(self, ingredient):
     return ingredient in self.ingredients
  
  # Method to update all_ingredients set
  def update_all_ingredients(self):
      Recipe.all_ingredients.update(self.ingredients)

  # String representation to print entire recipe
  def __str__(self):
     self.calculate_difficulty()
     return (
            f"Recipe Name: {self.name}\n"
            f"Cooking Time: {self.cooking_time} mins\n"
            f"Ingredients: {', '.join(sorted(self.ingredients))}\n"
            f"Difficulty: {self.difficulty}\n"
     )

# Function for searching recipes by specified ingredient
def recipe_search(data, search_term):
    print(f"Searching for recipes with {search_term}...")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
            break
    else:
        print(f"No recipes found with {search_term}.")

# Recipe inputs  
tea = Recipe("Tea", 5)
tea.add_ingredients("Tea leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar, Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(banana_smoothie)

# Wrapping recipes in recipes list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Search for recipies containing specified ingredients
for ingredient in ["Water", "Sugar", "Bananas"]:
  recipe_search(recipes_list, ingredient)
