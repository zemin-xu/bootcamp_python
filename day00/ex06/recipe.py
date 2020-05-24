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
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
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

def add_recipe(recipt_name):
    print("add")

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
            add_recipe(input("Please give me the recipe name you will add: "))
        elif (command == '2'):
            add_recipe(input("Please give me the recipe name you will add: "))
        elif (command == '3'):
            print_recipe(input("Please give me the recipe name you want to know\n"))
        elif (command == '4'):
            add_recipe(input("Please give me the recipe name you will add: "))
        elif (command == '5'):
            print("quit the program")
            return
        else:
            print("unknown command\n")
            continue

menu()
