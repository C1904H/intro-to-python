from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum

engine = create_engine("mysql+mysqlconnector://cf-python:password@localhost/task_database")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# Define Enum for Difficulty Levels
class Difficulty(PyEnum):
    Easy = "Easy"
    Medium = "Medium"
    Intermediate = "Intermediate"
    Hard = "Hard"

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)  
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(Enum(Difficulty), nullable=False)

    def __repr__(self):
        return f"Recipe(id={self.id}, name='{self.name}, difficulty='{self.difficulty.value}')"
    
    def __str__(self):
        return (
            f"{'='*40}\n"
            f"Recipe ID: {self.id}\n"
            f"Recipe Name: {self.name}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Ingredients: {self.ingredients}\n"
            f"Difficulty: {self.difficulty.value}\n"
            f"{'='*40}"
        )

    def calculate_difficulty(self):
        ingredient_count = len(self.ingredients.split(', '))

        if ingredient_count < 4 and self.cooking_time < 10:
            self.difficulty = Difficulty.Easy
        elif ingredient_count >= 4 and self.cooking_time < 10:
            self.difficulty = Difficulty.Medium
        elif ingredient_count < 4 and self.cooking_time >= 10:
            self.difficulty = Difficulty.Intermediate
        elif ingredient_count >= 4 and self.cooking_time >= 10:
            self.difficulty = Difficulty.Hard

    def return_ingredients_as_list(self):
        return self.ingredients.split(', ') if self.ingredients else []

#create table in database
Base.metadata.create_all(engine)

def create_recipe():
    
    while True:
      name = input("Enter recipe name (max 50 characters): ").strip()
      if len(name) <= 50:
            break
      else:
        print("Error - recipe name must not exceed 50 characters.")

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

    ingredients = set()
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ").strip()
        ingredients.add(ingredient.capitalize())
  
    # Convert ingredients set to  string
    ingredients_str = ", ".join(sorted(ingredients))  

    # Create a new Recipe object
    recipe_entry = Recipe(
        name=name,
        cooking_time=cooking_time,
        ingredients=ingredients_str,
        )

    recipe_entry.calculate_difficulty()

    # add recipe to database
    session.add(recipe_entry)
    session.commit()

    print("Recipe added successfully!")

def check_recipes_exist():
    if session.query(Recipe).count() ==0:
        print("No recipes found in database. Add some recipes!")
        return False
    return True
 
def view_all_recipes():
    if not check_recipes_exist():
        return
    
    recipes = session.query(Recipe).all()
    
    print("All Recipes:")
    for recipe in recipes:
        print(recipe)

def search_by_ingredients():
    if not check_recipes_exist():
        return 
      
    results = session.query(Recipe.ingredients).all()

    all_ingredients = set()
    
    for result in results:
        ingredients_list = result[0].split(', ')
        all_ingredients.update(ingredients_list)

    print("Available Ingredients:")
    for idx, ingredient in enumerate(sorted(all_ingredients), 1):
          print(f"{idx}. {ingredient}")

    user_input = input("Enter ingredient number(s) you'd like to search for (separate each no. with space): ")
    try:
        selected_ingredients_idx = [int(idx) for idx in user_input.split()]
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

    recipes = session.query(Recipe).filter(*conditions).all()

    if not results:
        print(f"No recipes found containing {', '.join(search_ingredients)}")
        return

    for recipe in recipes:
        print(f"Recipes containing {', '.join(search_ingredients)}:")
        print(recipe)

def edit_recipe():
    if not check_recipes_exist():
        return
        
    recipes = session.query(Recipe.id, Recipe.name).all()
    print("Available Recipes:")
    for recipe in recipes:
        print(f"ID:{recipe[0]}. {recipe[1]}")    

    recipe_id = input("Enter the ID of the recipe you want to edit: ")
    if not recipe_id.isdigit():
        print("Invalid ID.")
        return
    recipe_id = int(recipe_id)

    recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_edit:
        print("Recipe not found. Returning to main menu.")
        return None

    print(f"Recipe Details:\n{recipe_to_edit}")

    print("Recipe Edit Options:")
    print("1. Recipe Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    attribute_to_edit = input("Enter the number corresponding to the attribute you want to edit: ")

    if attribute_to_edit == "1":
        print(f"Current recipe name: {recipe_to_edit.name}")
        new_name = input("Enter new recipe name:  ")
        if len(new_name) <= 50:
            recipe_to_edit.name = new_name
        else:
            print("Error - recipe name must not exceed 50 characters.")
            return
        
    elif attribute_to_edit == "2":
        print(f"Current cooking time: {recipe_to_edit.cooking_time} minutes")
        new_cooking_time = input("Enter new cooking time (minutes): ")
        if new_cooking_time.isdigit():
            recipe_to_edit.cooking_time = int(new_cooking_time)
            recipe_to_edit.calculate_difficulty() #recalculate difficulty after cooking time updated
        else:
            print("Invalid cooking time. Please enter a positive number")
            return
    
    elif attribute_to_edit == "3":
        print(f"Current ingredients: {recipe_to_edit.ingredients}")
        new_ingredients_input = input("Enter new ingredients (separate with comma): ").strip()
        new_ingredients_list = [ingredient.strip().capitalize() for ingredient in new_ingredients_input.split(',')]
        new_ingredients_set = set(new_ingredients_list)
        sorted_ingredients_list = sorted(new_ingredients_set)
        recipe_to_edit.ingredients = ", ".join(sorted_ingredients_list)
        recipe_to_edit.calculate_difficulty() #recalculate difficulty after ingredients updated
    else:
        print("Invalid choice.")
        return

    # Commit the changes to database
    session.commit()
    print("\nRecipe successfully updated!\n")

def delete_recipe():
    if not check_recipes_exist():
        return

    recipes = session.query(Recipe.id, Recipe.name).all()

    print("Available Recipes:")
    for recipe in recipes:
        print(f"ID:{recipe[0]}. {recipe[1]}")

    recipe_id = input("Enter the ID of the recipe you want to delete: ")
    if not recipe_id.isdigit():
        print("Invalid ID.")
        return
    recipe_id = int(recipe_id)
            
    recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_delete:
        print("Recipe not found.")
        return

    print("\nRecipe Details:")
    print(recipe_to_delete)

    print(f"Are you sure you want to delete the recipe '{recipe_to_delete.name}'? Enter 'yes' or 'no': ")
    confirm_delete = input().strip().lower()
    if confirm_delete == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print(f"Recipe '{recipe_to_delete.name}' successfully deleted!")
    else:
        print("\nRecipe deletion cancelled. Returning to main menu.\n")

def main_menu():
    while True:
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
            session.close()  
            engine.dispose()  
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()            

        