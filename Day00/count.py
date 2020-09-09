# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/09 13:43:12 by armajchr          #+#    #+#              #
#    Updated: 2020/09/09 14:48:56 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def analyzer(s):
    index = 0
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i == ' ':
            spaces += 1
        else:
            punct += 1
    index = len(s)
    print("The text contains", index, "characters\n"\
        "\n- ", upper, "upper letters\n" \
        "\n- ", lower, "lower letters\n" \
        "\n- ", punct, "punctuation marks\n" \
        "\n- ", spaces, "spaces")
    
def get_text(s):
    if s == "":
        while True:
            try:
                a = input("Write your text here: ")
                if len(a) > 0:
                    analyzer(a)
                    break
            except ValueError:
                print ("Error")
    elif s == "text_analyzer.__doc__":
        print("This function counts the number of upper and lower characters," \
            " punctuation and spaces in a given text.")
    else:
        analyzer(s)
                
def text_analyzer(s = "", *s2):
    count = 0
    for i in s2:
        count += 1
    if count > 0:
        print("ERROR")
        sys.exit()
    else:
        get_text(s)