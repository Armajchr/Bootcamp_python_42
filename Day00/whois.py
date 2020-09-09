# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/09 13:27:03 by armajchr          #+#    #+#              #
#    Updated: 2020/09/09 16:41:54 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def get_args():
    if len(sys.argv) != 2:
        print("ERROR")
        sys.exit()
    n = sys.argv[1]
    if not n.isdigit():
        print("ERROR")
        sys.exit()
    return (n)

def whois(n):
    if int(n) == 0:
        print("I'm Zero")
    elif (int(n) % 2) == 0:
        print("I'm Even")
    elif (int(n) % 2) != 0:
        print("I'm odd")
    sys.exit()
    
n = 0
n = get_args()
whois(n)