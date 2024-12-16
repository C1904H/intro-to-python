#import packages and methods
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create import 
engine = create_engine("mysql+mysqlconnector://cf-python:password@localhost/task_database")

#create declarative base
Base = declarative_base()

#create session
Session = sessionmaker(bind=engine)
session = Session()

# Declare Recipe class
class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)  
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=False)

    def __repr__(self):
        return f"Recipe(id={self.id}, name='{self.name}, difficulty='{self.difficulty}')"
    
    def __str__(self):
        return (
            f"{'='*40}\n"
            f"Recipe ID: {self.id}\n"
            f"Recipe Name: {self.name}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Ingredients: {self.ingredients}\n"
            f"Difficulty: {self.difficulty}\n"
            f"{'='*40}"
        )

    def calculate_difficulty(self):
        ingredient_count = len(self.ingredients.split(', '))

        if ingredient_count < 4 and self.cooking_time < 10:
            self.difficulty = "Easy"
        elif ingredient_count >= 4 and self.cooking_time < 10:
            self.difficulty = "Medium"
        elif ingredient_count < 4 and self.cooking_time >= 10:
            self.difficulty = "Intermediate"
        elif ingredient_count >= 4 and self.cooking_time >= 10:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if self.ingredients:
            return self.ingredients.split(", ")
        else:
          return []

#create table in database
Base.metadata.create_all(engine)

#Function 1 - create_recipe
def create_recipe():
    
    while True:
      name = input("Enter recipe name (max 50 characters): ").strip()
      if len(name) <= 50:
            break
      else:
        print("Error - recipe name must not exceed 50 characters.")
        return

    while True:
        cooking_time = input("Enter the cooking time (in minutes): ").strip()
        if cooking_time.isnumeric() and not cooking_time.isalpha():  
            cooking_time = int(cooking_time)
            if cooking_time > 0:
              break
            else:
              print("Cooking time must be greater than 0.")
        else:
          print("Invalid input. Please enter a valid numeric value.")

          
    # Collect number of ingredients user wants to input
    while True:
        num_ingredients = input("How many ingredients would you like to enter? ").strip()
        if num_ingredients.isnumeric():  
          num_ingredients = int(num_ingredients)
          if num_ingredients > 0:
            break
          else:
              print("Error - at least one ingredient must be entered.")
        else:
              print("Invalid input. Please enter a numeric value.")

    # Collect ingredients
    ingredients = set()
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ").strip()
        # Capitalize the first letter of each ingredient
        ingredients.add(ingredient.capitalize())
  
    # Convert ingredients set to a string
    ingredients_str = ", ".join(sorted(ingredients))  

    # Create a new Recipe object
    recipe_entry = Recipe(
        name=name,
        cooking_time=cooking_time,
        ingredients=ingredients_str,
        )

    # calculate difficulty
    recipe_entry.calculate_difficulty()

    # add recipe to database
    session.add(recipe_entry)
    session.commit()

    print("Recipe added successfully!")

#Function 2 - view_all_recipes  
def view_all_recipes():
    recipes = session.query(Recipe).all()

    if not recipes:
        print("No recipes in database. Add some recipes!")
        return None
    
    print("All Recipes:")
    for recipe in recipes:
        print(recipe)

#Function 3 - search_by_ingredients
def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes in database. Add some recipes!")
        return None
      
    results = session.query(Recipe.ingredients).all()

    all_ingredients = set()
    
    for result in results:
        ingredients_list = result[0].split(', ')
        all_ingredients.update(ingredients_list)

    print("Available Ingredients:")
    for idx, ingredient in enumerate(sorted(all_ingredients), 1):
          print(f"{idx}. {ingredient}")


  # Ask user to select ingredients
    user_input = input("Enter ingredient number(s) you'd like to search for (separate with space): ")
    try:
        selected_ingredients_idx = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Build a list of ingredients to search for
    search_ingredients = []
    for idx in selected_ingredients_idx:
        if 1 <= idx <= len(all_ingredients):
            search_ingredients.append(sorted(all_ingredients)[idx - 1])
        else:
            print("Invalid selection.")
            return

    # Create LIKE conditions for the query
    conditions = []
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%" 
        conditions.append(Recipe.ingredients.like(like_term))


    # Query the database for recipes matching the ingredients
    recipes = session.query(Recipe).filter(*conditions).all()

    # Display the results
    if not results:
        print(f"No recipes found containing {', '.join(search_ingredients)}")
        return

    for recipe in recipes:
        print(f"Recipes containing {', '.join(search_ingredients)}:")
        print(recipe)

# Function 4 - edit_recipe
def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes in database. Add some recipes!")
        return None
        
    # Retrieve the id and name of all recipes
    recipes = session.query(Recipe.id, Recipe.name).all()
    print("Available Recipes:")
    for recipe in recipes:
        print(f"ID:{recipe[0]}. {recipe[1]}")    

    #User to input recipe ID
    recipe_id = input("Enter the ID of the recipe you want to edit: ")
    if not recipe_id.isdigit():
        print("Invalid ID.")
        return
    recipe_id = int(recipe_id)

    recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_edit:
        print("Recipe not found. Returning to main menu.")
        return None

           
    # Display current values of the recipe
    print(f"Recipe Details:\n{recipe_to_edit}")

    # Ask which attribute the user wants to edit
    print("Recipe Edit Options:")
    print("1. Recipe Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    attribute_to_edit = input("Enter the number corresponding to the attribute you want to edit: ")

    # Edit name
    if attribute_to_edit == "1":
        print(f"Current recipe name: {recipe_to_edit.name}")
        new_name = input("Enter new recipe name:  ")
        if len(new_name) <= 50:
            recipe_to_edit.name = new_name
        else:
            print("Error - recipe name must not exceed 50 characters.")
            return
        
    # Edit cooking time
    elif attribute_to_edit == "2":
        print(f"Current cooking time: {recipe_to_edit.cooking_time} minutes")
        new_cooking_time = input("Enter new cooking time (minutes): ")
        if new_cooking_time.isdigit():
            recipe_to_edit.cooking_time = int(new_cooking_time)
        else:
            print("Invalid cooking time. Please enter a positive number")
            return
    
    # Edit ingredients
    elif attribute_to_edit == "3":
        print(f"Current ingredients: {recipe_to_edit.ingredients}")
        new_ingredients_input = input("Enter new ingredients (separate with comma): ").strip()
        new_ingredients_list = [ingredient.strip().capitalize() for ingredient in new_ingredients_input.split(',')]
        new_ingredients_set = set(new_ingredients_list)
        sorted_ingredients_list = sorted(new_ingredients_set)
        recipe_to_edit.ingredients = ", ".join(sorted_ingredients_list)
    else:
        print("Invalid choice.")
        return

    # Recalculate the difficulty
    recipe_to_edit.calculate_difficulty()

    # Commit the changes to database
    session.commit()
    print("\nRecipe successfully updated!\n")

# Function 5 - delete_recipe
def delete_recipe():
    # Check if any recipes exist in the database
    if session.query(Recipe).count() == 0:
        print("No recipes in database. Returning to main menu.\n")
        return None

    # Retrieve the id and name of all recipes
    recipes = session.query(Recipe.id, Recipe.name).all()

    # Display recipes 
    print("Available Recipes:")
    for recipe in recipes:
        print(f"ID:{recipe[0]}. {recipe[1]}")

    # Ask the user to select recipe by ID
    recipe_id = input("Enter the ID of the recipe you want to delete: ")
    if not recipe_id.isdigit():
        print("Invalid ID.")
        return
    recipe_id = int(recipe_id)
            
    recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).first()
    # checks if recipe in database
    if not recipe_to_delete:
        print("Recipe not found.")
        return

    # Display recipe details
    print("\nRecipe Details:")
    print(recipe_to_delete)

    # Confirm deletion
    print(f"Are you sure you want to delete the recipe '{recipe_to_delete.name}'? Enter 'yes' or 'no': ")
    confirm_delete = input().strip().lower()
    if confirm_delete == 'yes':
        # Delete the recipe and commit the change
        session.delete(recipe_to_delete)
        session.commit()
        print(f"Recipe '{recipe_to_delete.name}' successfully deleted!")
    else:
        print("\nRecipe deletion cancelled. Returning to main menu.\n")

 # Main menu function
def main_menu():
    while True:
        # Display menu options
        print("\n" + "=" * 40 )
        print(" -------------- Main Menu --------------")
        print("=" * 40 )
        print("\nMenu options:")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit")

        # User input
        choice = input("\nSelect an option: ").strip().lower()

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            print("Exiting program ... Goodbye!")
            session.close()  # Close the session
            engine.dispose()  # Dispose of the engine
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()            


        