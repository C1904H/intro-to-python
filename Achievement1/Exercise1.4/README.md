# Exercise 1.4: File Handling in Python

## Tasks
- Use files to store and retrieve data in Python

## Output
- Created 2 scripts: **"recipe_input.py"** and **"recipe_search.py"**
- "recipe_input.py" takes recipes from the user, compiles them and their ingredients into a list, and stores in a binary file for later use.  The script can be run again later to add more recipes.
- "recipe_search.py" accesses the binary file, listing ingredients that are available. User enters an ingredient, and the script displays every recipe containing that specific ingredient. 
- `try\except` blocks handle `FileNotFoundError` and other exceptions.