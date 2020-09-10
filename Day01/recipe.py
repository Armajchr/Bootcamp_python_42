# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/10 16:38:15 by armajchr          #+#    #+#              #
#    Updated: 2020/09/10 18:18:05 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_args(name, lvl, time, ingr, desc, type):
    if not isinstance(name, str):
        print("ERROR: name is not a string")
        return (0)
    try:
        if len(name) == 0:
            print("ERROR: name is empty")
            return (0)
    except ValueError:
        pass
    if not isinstance(lvl, int):
        print("ERROR: cooking_lvl is not an int")
        return (0)
    try:
        if lvl <= 0 or lvl > 5:
            print("ERROR: cooking_lvl is out of range")
            return (0)
    except ValueError:
        pass
    if not isinstance(time, int):
        print("ERROR: time is not an int")
        return (0)
    try:
        if time < 0:
            print("ERROR: time can't be negative")
            return (0)
    except ValueError:
        pass
    if not isinstance(ingr, list):
        print("ERROR: ingredients are not a list")
        return (0)
    try:
        if len(ingr) == 0:
            print("ERROR: ingredients list is empty")
            return (0)
        for i in ingr:
            if not isinstance(i, str):
                print("ERROR: ingredient is not a string")
                return (0)
            if len(i) == 0:
                print("ERROR: one of the ingredient is empty")
                return (0)
    except ValueError:
        pass
    if not isinstance(desc, str):
        print("ERROR: description is not a string")
        return (0)
    if not isinstance(type, str):
        print("ERROR: recipe_type is not a string")
        return (0)
    try:
        if len(type) == 0:
            print("ERROR: recipe_type is empty")
            return (0)
        if type != "starter" and type != "lunch" and type != "dessert":
            print("ERROR: recipe_type can only be starter, lunch and dessert")
            return (0)
    except ValueError:
        pass
    return (1)

class   Recipe:
    def __init__(self, name, lvl, time, ingr, desc, type):
        if check_args(name, lvl, time, ingr, desc, type) == 1:
            self.name = name
            self.cooking_lvl = lvl
            self.cooking_time = time
            self.ingredients = ingr
            self.description = desc
            self.recipe_type = type
            
    def __str__(self):
        #Return the string to print with the recipe info
        txt = ""
        txt = "The recipe " + self.name + " is a lvl " + str(self.cooking_lvl) + " recipe"
        txt += "\nYou will need " + str(self.cooking_time) + " minutes to cook it"
        txt += "\nThe needed ingredients are: " + str(self.ingredients)
        txt += "\nHere is a description of the recipe: " + self.description
        txt += "\nThe recipe_type is: " + self.recipe_type
        return (txt)