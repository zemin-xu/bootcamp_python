import sys
cookbook = {
    'sandwich': 
    {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    'cake':
    {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'salad':
    {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    },
}


def print_recipe(recipt_name):
    recipt_key = cookbook[recipt_name]
    if recipt_key == None:
        print("recipt not found")
        return
    print("Recipe for {}".format(recipt_name))
    print("Ingredients list: {}".format(recipt_key.get('ingredients')))
    print("To be eaten for {}.".format(recipt_key.get('meal')))
    print("Takes {} minutes of cooking.".format(recipt_key.get('prep_time')))

def print_all():
    for k in cookbook.keys():
        print_recipe(k)

def add_recipe():
    recipt_name = input("give me the name of recipt to add: \n")
    recipt_ingredients = input("give me the ingredients, seperated by comma\n")
    ingre_list = recipt_ingredients.split(',')
    recipt_type = input("the type\n")
    recipt_time = input("the time\n")
    cookbook[recipt_name] = {
        'ingredients': ingre_list,
        'meal': recipt_type,
        'prep_time': recipt_time,
    }

def delete_recipe():
    recipt_name = input("give me the name of recipt to delete: \n")
    del(cookbook[recipt_name])

def menu():
    while (True):
        print("Please select an option by typing the coresponding number: ")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cook book")
        print("5: Quit")
        command = input()
        if (command == '1'):
            add_recipe()
        elif (command == '2'):
            delete_recipe()
        elif (command == '3'):
            print_recipe(input("Please give me the recipe name you want to know\n"))
        elif (command == '4'):
            print_all()
        elif (command == '5'):
            print("quit the program")
            return
        else:
            print("unknown command\n")
            continue

menu()
