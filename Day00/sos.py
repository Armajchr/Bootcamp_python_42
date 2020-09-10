# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/10 13:32:33 by armajchr          #+#    #+#              #
#    Updated: 2020/09/10 14:18:18 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', "E": '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.--.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', ' ': ' / '
}

def sos(s):
    s2 = ""
    for i in s:
        for keys, values in morse.items():
            if i == keys:
                for y in values:
                    s2 += y
                s2 += " "
    s2 = s2.rstrip()
    print(s2)
        

def get_args(s):
    if len(sys.argv) == 1:
        sys.exit()
    for arg in sys.argv:
        s = s + " " + arg
    s = s.split()
    del s[0]
    s2 = ""
    count = -1
    for i in s:
        count += 1
        s2 += s[count] + " "
    s2 = s2.rstrip()
    s2 = s2.upper()
    for i in s2:
        if  i != ' ' and (i < '0' or i > '9' and i < 'A' or i > 'Z'):
            print("ERROR")
            sys.exit()
    sos(s2)
    
s = ""
get_args(s)