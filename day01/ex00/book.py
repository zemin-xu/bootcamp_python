from datetime import datetime
from recipe import Recipe
class Book:

    def __init__(self):
        self.name = 'recipe_book'
        self.creation_time = datetime.now()
        self.last_update = self.creation_time
        print(self.creation_time)

        self.recipes_list = {
        'starter': [],
        'lunch': [],
        'dessert': [],
        }

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        pass


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
