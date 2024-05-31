from sets_categories_data import (ALCOHOLS)
def clean_ingredients(dish_name, dish_ingredients):
    y = set(dish_ingredients)
    return (dish_name, y)



def check_drinks(drink_name, drink_ingredients):
    y = ""
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            y = "Cocktail"
            break
        else:
            y = "Mocktail"
    return f"{drink_name}{y}"
