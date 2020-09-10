# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/10 18:18:46 by armajchr          #+#    #+#              #
#    Updated: 2020/09/10 18:37:30 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

#Create recipe 1
eggs = Recipe("Eggs", 1, 10, ['eggs', 'salt', 'pepper', 'bread', 'butter'], "", "lunch")
#Create recipe 2
lasagnes = Recipe("Lasagnes", 3, 60, ['pasta', 'bolo sauce', 'bechamel' 'meat', 'cheese'], "delicious", "lunch")
#init Book
cookbook = Book("cookbook")
#add recipe 1 and 2
Book.add_recipe(cookbook, eggs)
Book.add_recipe(cookbook, lasagnes)
#testing the functions
Book.get_recipe_by_name(cookbook, "Lasagnes")
Book.get_recipe_by_types(cookbook, 'lunch')