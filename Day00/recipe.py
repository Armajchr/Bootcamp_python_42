# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/10 09:48:16 by armajchr          #+#    #+#              #
#    Updated: 2020/09/10 12:50:33 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cook_book = {
    'sandwich' : {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 10},
    'cake' : {'ingredients': ['flour', ' suggar', 'eggs'], 'meal': 'dessert', 'prep_time': 60},
    'salad' : {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15}
}

def	add_rcp(cook_book):
    while True:
        try:
            count = 0
            rcp = input("Please name the new recipe:")
            for i, y in cook_book.items():
                if i == rcp:
                    count += 1
                    print("Recipe allready exist, if you want to change it please delete it first, if not, please choose another name")
            if count == 0:
                ing = str(input("Choose ingredients:"))
                ing = ing.split()
                meal = str(input("Choose type of meal:"))
                time = int(input("How long to cook it?"))
                break
        except ValueError:
            print("ERROR")
            continue
    cook_book.update({rcp: {'ingredients' : ing, 'meal': meal, 'prep_time': time}})
    menu(cook_book)

def del_rcp(cook_book):
    while True:
        try:
            a = str(input("Please select a recipe to delete:"))
            for i, y in cook_book.items():
                if a == i:
                    del cook_book[i]
                    menu(cook_book)
            print("This recipe is not in the cookbook. Please chose another one")
            continue
        except ValueError:
            print("ERROR")
    menu(cook_book)

def print_rcp(cook_book):
    while True:
        try:
            count = 0
            rcp = str(input("Choose a recipe to print:"))
            for i, y in cook_book.items():
                if i == rcp:
                    print("\nThe recipe for :", i)
                    print("the ingredients list:", y['ingredients'])
                    print("To be eaten for", y['meal'])
                    print("Take", y['prep_time'], "minutes of cooking")
                    count += 1
                    print("\n")
                    menu(cook_book)
            if count == 0:
                print("This recipe is not in the cookbook")
                print_rcp(cook_book)
        except ValueError:
            print("ERROR")
                    

def print_cb(cook_book):
    for i, y in cook_book.items():
        print("\nThe recipe for :", i)
        print("the ingredients list:", y['ingredients'])
        print("To be eaten for", y['meal'])
        print("Take", y['prep_time'], "minutes of cooking\n")
    menu(cook_book)

def exit_cb():
    print("Goodbye old friend")
    sys.exit()

def	choose_fct(cook_book, a):
    if a == 1:
        add_rcp(cook_book)
    if a == 2:
        del_rcp(cook_book)
    if a == 3:
        print_rcp(cook_book)
    if a == 4:
        print_cb(cook_book)
    else:
        exit_cb()

def	menu(cook_book):
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    while True:
        try:
            a = input(">>")
            if (int(a) >= 1 and int(a) <= 5):
                choose_fct(cook_book, int(a))
                break
            else:
                print("This options does not exist, please type the corresponding number.")
                print("to exit, enter 5")
        except ValueError:
            print("This options does not exist, please type the corresponding number.")
            print("to exit, enter 5")
            continue

menu(cook_book)