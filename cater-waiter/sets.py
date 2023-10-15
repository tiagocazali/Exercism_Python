"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return(dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """

    alcoholic_ingredients = set(ALCOHOLS)
    
    for ingredient in drink_ingredients:
        if ingredient in alcoholic_ingredients:
            return f'{drink_name} Cocktail'
    
    return f'{drink_name} Mocktail'

    # It is possible to do using List Comprehension 
    #if any(ingredient.lower() in alcoholic_ingredients for ingredient in drink_ingredients):
    


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """
    food_vegan = set(VEGAN)
    food_vegetarian = set(VEGETARIAN)
    food_keto = set(KETO)
    food_paleo = set(PALEO)
    food_omnivore = set(OMNIVORE)

    if set(dish_ingredients).issubset(food_vegan):
        category = 'VEGAN'
    elif set(dish_ingredients).issubset(food_vegetarian):
        category = 'VEGETARIAN'
    elif set(dish_ingredients).issubset(food_paleo):
        category = 'PALEO'
    elif set(dish_ingredients).issubset(food_keto):
        category = 'KETO'
    elif set(dish_ingredients).issubset(food_omnivore):
        category = 'OMNIVORE'
    
    return f'{dish_name}: {category}'


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    special_list = set(SPECIAL_INGREDIENTS)
    list_of_ingredients = set(dish[1])

    return dish[0], list_of_ingredients.intersection(special_list) #elements common to the original `set` and special_list
    

def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    all_ingredients = set()
    for each in dishes:
        all_ingredients = all_ingredients.union(each)
    return all_ingredients


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    dishes2 = set(dishes)
    appetizers2 = set(appetizers)
    
    return list(dishes2.difference(appetizers2))


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    #============ Rakeshksr's solution ===========
    all_ingredients = set()
    for ingredients in dishes:
        all_ingredients = all_ingredients ^ ingredients #all_ingredients.symmetric_difference(ingredients)
    return all_ingredients - intersection
