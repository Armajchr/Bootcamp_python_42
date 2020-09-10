# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/10 16:34:22 by armajchr          #+#    #+#              #
#    Updated: 2020/09/10 18:37:19 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe
import sys

class   Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.dico = {'starte': [], 'lunch': [], 'dessert': []}
    
    def get_recipe_by_name(self, name):
        if not isinstance(name, str):
            print("ERROR1: recipe name is not a string")
            sys.exit()
        try:
            if len(name) == 0:
                print("ERROR: recipe name is empty")
                sys.exit()
            for items in self.dico.values():
                for elem in items:
                    if elem.name == name:
                        print(elem)
                        return(elem)
            print("ERROR: no matches in recipes with given recipe name")
        except ValueError:
            pass
        pass
    
    def get_recipe_by_types(self, recipe_type):
        #Get all recipe names for a given recipe_type
        if not isinstance(recipe_type, str):
            print("ERROR: recipe_type is not a string")
            sys.exit()
        try:
            if len(recipe_type) == 0:
                print("ERROR: recipe_type is empty")
                sys.exit()
            if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
                print("ERROR: Recipes can only be starter, lunch or dessert")
                sys.exit()
            for items in self.dico.keys():
                if items == recipe_type:
                    print("Recipes in " + recipe_type + ":")
                    for elem in self.dico[recipe_type]:
                        print(elem.name)
                    return
        except ValueError:
            pass
        pass
    
    def add_recipe(self, recipe):
        #Add a recipe to the book and update last_update
        if not isinstance(recipe, Recipe):
            print("ERROR: This is not a recipe")
            sys.exit()
        if recipe.recipe_type in self.dico.keys():
            self.dico[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        else:
            print("ERROR: Recipe_type is not starter, lunch or dessert")
            sys.exit()
        pass