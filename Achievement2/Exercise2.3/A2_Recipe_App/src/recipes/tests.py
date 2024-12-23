from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

  def setUpTestData():
    Recipe.objects.create(
      name='Cheesy Toast', 
      ingredients='Bread, Cheese, Pickles',
      cooking_time=5,
      # difficulty='Easy',
      description='Fast comfort food!'
    )

  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')
    
  def test_recipe_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length
    self.assertEqual(max_length, 50)

  def test_recipe_str_method(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(str(recipe), 'Cheesy Toast')

  def test_recipe_creation(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.name, 'Cheesy Toast')
    self.assertEqual(recipe.cooking_time, 5)
    self.assertIn('Bread', recipe.ingredients)

  def test_calculate_difficulty(self):
    recipe = Recipe.objects.get(id=1)
    recipe.cooking_time = 15
    recipe.ingredients = 'Ingredient1, Ingredient2'
    recipe.save()
    self.assertEqual(recipe.difficulty, 'Intermediate')
    