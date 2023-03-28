def read_dict_from_file(filename):
    """
    Takes in the name of a file containing a recipe or 
    pantry list and reads it into a dictionary.
    
    An example doctest using the file above:
    >>> read_dict_from_file('recipe.txt')
    {'flour': 200.0, 'salt': 2.5}
    """
    d = dict()
    with open(filename) as file:
        for line in file:
            key, value = line.split('::')
            value = float(value)
            d[key] = value
    return d

def can_make(recipe, pantry):
    """
    Given the contents of the pantry, returns a boolean indicating 
    whether or not it is possible to follow the recipe. Note that 
    the parameters to this function are dictionaries, and not 
    filenames. The pantry should not be modified in this function
    """
    for ingredient in recipe:
        if ingredient not in pantry or pantry[ingredient] < recipe[ingredient]:
            return False
    return True 

def make_recipe(recipe, pantry):
    """
    Given a recipe and a pantry with enough ingredients to make the recipe, 
    modify the contents of the pantry to remove as many quantities as the 
    recipe requires. You may modify the pantry in place, but return the modified 
    pantry in order to test the output using doctests. 

    # using the recipe and pantry defined above
    >>> recipe = read_dict_from_file('recipe.txt')
    >>> pantry = read_dict_from_file('pantry.txt')
    >>> make_recipe(recipe, pantry)
    {'flour': 200.0, 'sugar': 300.0, 'salt': 7.5, 'chocolate': 150.0}
    """
    for ingredient in recipe:
        pantry[ingredient] -= recipe[ingredient]
    return pantry

def main():
    pantry_filename = input("Enter pantry filename: ")
    pantry = read_dict_from_file(pantry_filename)
    while True:
        recipe_filename = input("What recipe should we bake next (Press enter to quit.)? ")
        if recipe_filename == '':
            break
        recipe = read_dict_from_file(recipe_filename)

        if can_make(recipe, pantry):
            make_recipe(recipe, pantry)
            print("You can make that recipe! Your pantry now looks like this: ")
            print(pantry)
        else:
            print("You can't make that recipe.")
        print()

if __name__ == '__main__':
    main()







