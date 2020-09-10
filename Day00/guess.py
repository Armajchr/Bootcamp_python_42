# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/10 14:18:50 by armajchr          #+#    #+#              #
#    Updated: 2020/09/10 14:48:32 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import random


def result(rnd, g, count):
    if g == 42:
        print("The answer to the ultimate question of life, the universe and everything is 42")
    if rnd == g:
        if count == 1:
            print("Congratulations, you got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("you won in", count, "attemps!")
        menu()
    elif g < rnd:
        print("Too low!")
    else:
        print("too high!")
  
def menu():
    rnd = random.randint(1, 99)
    count = 0
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck padawan!")
    while True:
        try:
            g = input("What's your guess between 1 and 99?\n>>")
            if g == "exit" or g == "EXIT":
                print("Goodbye my old friend!")
                sys.exit()
            if g >= '1' and g <= '99':
                count += 1
                result(rnd, int(g), count)
                continue
            else:
                print("That's not a number or your number is not in range[1->99].")
                continue
        except ValueError:
            print("ERROR")

menu()            