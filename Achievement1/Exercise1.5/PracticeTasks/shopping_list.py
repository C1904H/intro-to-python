
class ShoppingList ():
  def __init__(self, list_name):
    self.list_name = list_name
    self.shopping_list = []

  def add_item(self, item):
    if not item in self.shopping_list:
      self.shopping_list.append(item)
      print("Item added to shopping list")
    else:
      print("Item already in shopping list")

  def remove_item(self, item):
    if item in self.shopping_list:
      self.shopping_list.remove(item)
      print("Item removed from shopping list")
    else:
      print("Item not in shopping list")

  def view_list(self):
    if not self.shopping_list:
      print("No items in shopping list")
    else:
      print("Shopping List:")
      for item in self.shopping_list:
        print(item)

# Creat pet_store_list object
pet_store_list = ShoppingList('Pet Store Shopping List')

# Add named items to pet_store_list
pet_store_list.add_item ('dog food')
pet_store_list.add_item ('frisbee')
pet_store_list.add_item ('bowl')
pet_store_list.add_item ('collars')
pet_store_list.add_item ('flea collars')

# Remove 'flea collars' from list
pet_store_list.remove_item('flea collars')

# Try to add 'frisbee' to list again
pet_store_list.add_item('frisbee')

# Display entire shopping list
pet_store_list.view_list()