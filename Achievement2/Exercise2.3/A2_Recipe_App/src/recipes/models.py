from django.db import models

class Recipe(models.Model):
  name= models.CharField(max_length=50)
  ingredients= models.TextField()
  cooking_time= models.PositiveIntegerField(help_text="Cooking time in minutes")
  difficulty= models.CharField(max_length=20) 
  description= models.TextField()

  def calculate_difficulty(self):
    num_ingredients = len(self.ingredients.split(','))

    if self.cooking_time < 10 and num_ingredients <= 4:
        self.difficulty = 'Easy'
    elif self.cooking_time < 10:
        self.difficulty = 'Medium'
    elif num_ingredients <= 4:
        self.difficulty = 'Intermediate'
    else:
        self.difficulty = 'Hard'

  def save(self, *args, **kwargs):
        self.calculate_difficulty()
        super().save(*args, **kwargs)

  def __str__(self):
    return str(self.name)
