from recipe import Recipe
from book import Book


print("\nTest: allowed inputs for Recipe class.\n")
sandwich = Recipe("sandwich", 1, 10, ['ham', 'bread', 'cheese', 'tomatoes'], "lunch", "sandwich recipe.")
print(str(sandwich))
cake = Recipe("cake", 3, 60, ['flour', 'sugar', 'eggs'], "dessert", "cake recipe.")
print(str(cake))
salad = Recipe("salad", 2, 15, ['avocado', 'arugula', 'tomatoes', 'spinach'], "starter", "salad recipe.")
print(str(salad))
print("\nTest: allowed inputs for Book class.\n")
book = Book()
print("Create Time: ", book.creation_time)
print("\nTest: Book class method.\n")
print("\nTest: add_recipe method")

book.add_recipe(sandwich)
book.add_recipe(cake)
book.add_recipe(salad)
print("\nTest: get_recipes_by_type method.\n")
for recipe_type in ["starter", "dessert", "lunch"]:
    book.get_recipes_by_types(recipe_type)
print("\nTest: invalid recipe_type for get_recipes_by_type\n", "-" * 42)
book.get_recipes_by_types("42")
print("\nTest: invalid recipe_name for get_recipes_by_name\n", "-" * 42)
book.get_recipe_by_name("42")
print("\nTest: invalid inputs for Recipe\n", "-" * 42)
invalid = Recipe(1, "", "", "", 1, 1)