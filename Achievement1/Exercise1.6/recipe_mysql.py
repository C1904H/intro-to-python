import mysql.connector

# initialize connection object
conn = mysql.connector.connect(
  host='localhost',
  user='cf-python',
  passwd='password')

# initialize cursor object from conn
cursor = conn.cursor()

# create task_database (if doesn't alreay exist) and script access database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

# Create Recipes Table if doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id  INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)''')

# Calculate difficulty of recipe
def calculate_difficulty(cooking_time, ingredients):
  ingredient_len = len(ingredients)

  if cooking_time < 10 and ingredient_len < 4:
    return 'Easy'
  elif cooking_time < 10 and ingredient_len >= 4:
    return 'Medium'
  elif cooking_time >= 10 and ingredient_len < 4:
    return 'Intermediate'
  elif cooking_time >= 10 and ingredient_len >= 4:
    return 'Hard'
  
# Create recipe
def create_recipe(conn, cursor):

  name = input("Enter recipe name: ")
  cooking_time = int(input("Enter cooking time (mins): "))
  ingredient_input = input("Enter ingredients (separate items with comma): ")
  ingredients = set(
          ingredient.strip().capitalize() 
          for ingredient in ingredient_input.split(","))
  ingredients_str = ", ".join(ingredients)
  
  # calculate difficulty
  difficulty = calculate_difficulty(cooking_time, ingredients)
  
  # add to database
  cursor.execute('''
  INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
  VALUES (%s, %s, %s, %s)
  ''', (name, ingredients_str, cooking_time, difficulty))
  conn.commit()   
  print(f"Recipe added successfully!")

# Search recipe function
def search_recipe(conn, cursor):
  cursor.execute("SELECT ingredients FROM Recipes")
  results = cursor.fetchall()

  if results:
    all_ingredients = set()
    for row in results:
      ingredients_list = row[0].split(", ")
      all_ingredients.update(ingredients_list)

    all_ingredients = sorted(all_ingredients)

    print("\nAvailable Ingredients: ")
    for idx, ingredient in enumerate(all_ingredients, start=1):
      print(f"{idx}. {ingredient}")

    try:
        choice = int(input("Enter the number of the ingredient to search: "))
        
        search_ingredient = all_ingredients[choice -1]
        
        cursor.execute('''
        SELECT * FROM Recipes WHERE ingredients LIKE %s
        ''', (f"%{search_ingredient}%",))
        results = cursor.fetchall()

        if results:
          print(f"\nRecipes found containing '{search_ingredient}': ")
          for recipe in results:
            print(f"ID: {recipe[0]}, Recipe Name: {recipe[1]}, Ingredients: {recipe[2]}, Cooking Time: {recipe[3]} minutes, Difficulty: {recipe[4]}")
        else:
          print(f"No recipes found containing '{search_ingredient}'.")

    except (ValueError, IndexError):
      print("Invalid input. Select valid number from list.")

  else:
    print("No ingredients in database. Add some recipes!")

# Update a Recipe
def update_recipe(conn, cursor):
  cursor.execute("SELECT id, name FROM Recipes")
  recipes = cursor.fetchall()

  if recipes:
    print("\nAll Recipes: ")
    for recipe in recipes:
      print(f"ID: {recipe[0]}, Recipe Name: {recipe[1]}")

    try:
        recipe_id = int(input("Enter the ID of the recipe to be updated: "))
        cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id,))
        recipe_details = cursor.fetchone()

        if recipe_details is None:
            raise ValueError(f"Recipe with ID {recipe_id} does not exist.")

        # Display current recipe details to the user
        print("\nCurrent Recipe Details:")
        print(f"Name: {recipe_details[1]}")
        print(f"Ingredients: {recipe_details[2]}")
        print(f"Cooking Time: {recipe_details[3]} minutes")
        print(f"Difficulty: {recipe_details[4]}")
        
        print ("Update options -")
        print("1. Recipe Name")
        print("2. Cooking Time")
        print("3. Ingredients")

        field_choice = input("Enter the number corresponding to the option you want to update: ")
        if field_choice not in {'1', '2', '3'}:
              raise ValueError("Invalid entry. Please select 1, 2, or 3.")
        
        # Update recipe name
        if field_choice == '1':
          new_name = input("Enter the new recipe name: ")
          cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (new_name, recipe_id))
    
        # Update cooking time 
        elif field_choice == '2':
          new_time = int(input("Enter the new cooking time (in mins): "))
          cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
          ingredients = cursor.fetchone()[0].split(", ")
          # recalculate difficulty
          new_difficulty = calculate_difficulty(new_time, ingredients)
          cursor.execute('''
            UPDATE Recipes 
            SET cooking_time = %s, difficulty = %s 
            WHERE id = %s
          ''', (new_time, new_difficulty, recipe_id))
          print("Cooking time and difficulty updated successfully.")
    
        # update ingredients 
        elif field_choice == '3':
          ingredient_input = input("Enter new ingredients list (separate items with comma): ").strip()
          if not ingredient_input:
            raise ValueError("Ingredient list cannot be empty.")

          new_ingredients = set(
            ingredient.strip().capitalize() 
            for ingredient in ingredient_input.split(",")
            if ingredient.strip())
          if not new_ingredients:
            raise ValueError("You must enter at least one ingredient.")
          new_ingredients_str = ", ".join(new_ingredients)
          cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
          cooking_time = cursor.fetchone()[0]
          # recalculate difficulty
          new_difficulty = calculate_difficulty(cooking_time, list(new_ingredients))
          cursor.execute('''
            UPDATE Recipes 
            SET ingredients = %s, difficulty = %s 
            WHERE id = %s
          ''', (new_ingredients_str, new_difficulty, recipe_id))
          print("Ingredients and difficulty updated successfully.")
        
        conn.commit()
        print("Recipe successfully updated!")
    except ValueError:
        print("Invalid input.")
  else:
      print("No recipes available to update.")

# Delete a recipe
def delete_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    
    if recipes:
        print("\nAll Recipes: ")
        for recipe in recipes:
            print(f"ID: {recipe[0]}, Recipe Name: {recipe[1]}")

        try:
          recipe_id = int(input("Enter the ID of the recipe you want to delete: "))
          cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
          # checks entered ID exists in database - returns error if not
          if cursor.rowcount == 0:
            print("Error: Recipe does not exist.")
          else:
              conn.commit()
              print("Recipe successfully deleted!")

        except ValueError:
          print("Invalid input. Please enter a valid recipe ID.")

    else:
        print("No recipes available to delete.")


# Main menu function
def main_menu(conn, cursor):
  while True:
    print("====================================")
    print("Main Menu")
    print("====================================")
    print("Menu Options - ")
    print("1. Create a new recipe")
    print("2. Search for a recipe by ingredient")
    print("3. Update an existing recipe")
    print("4. Delete a recipe")
    print("5. Exit")

    choice = input("Please select an option: ")

    if choice == '1':
      create_recipe(conn,cursor)
    elif choice == '2':
      search_recipe(conn,cursor)
    elif choice == '3':
      update_recipe(conn,cursor)
    elif choice =='4':
      delete_recipe(conn,cursor)
    elif choice =='5':
      print("Exiting program...Goodbye.")
      conn.commit()
      conn.close()
      break
    else:
      print("Error, please select another option.")

main_menu(conn, cursor)