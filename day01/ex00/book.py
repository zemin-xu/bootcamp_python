from datetime import datetime
from recipe import Recipe
class Book:

    def __init__(self):
        self.name = 'recipe_book'
        self.creation_time = datetime.now()
        self.last_update = self.creation_time

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
        if str(recipe_type) in self.recipes_list:
            for r in self.recipes_list[recipe_type]:
                print(str(r))
        else:
            print("key not found")
        pass


    def add_recipe(self, recipe):
        try:
            if isinstance(recipe, Recipe):
                self.name = recipe
                if recipe.recipe_type == 'starter':
                    self.recipes_list['starter'].append(recipe)
                elif recipe.recipe_type == 'lunch':
                    self.recipes_list['lunch'].append(recipe)
                elif recipe.recipe_type == 'dessert':
                    self.recipes_list['dessert'].append(recipe)
                self.last_update = datetime.now()
            else:
                raise AttributeError
        except AttributeError:
            print("type error for recipe")
            pass 
        """Add a recipe to the book and update last_update"""
        pass
