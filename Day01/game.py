# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/15 10:02:47 by armajchr          #+#    #+#              #
#    Updated: 2020/09/15 10:34:01 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class   GotCharacter(object):
    def __init__(self, name):
        self.name = name
        self.is_alive = True

class	Lannister(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        	super(Lannister, self).__init__(first_name)
        	self.family_name = "Lannister"
        	self.house_words = "Something that they say..."
    
    def print_house_words(self):
        print(self.house_words)
        
    def die(self):
        self.is_alive = False
