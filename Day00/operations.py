# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/09 14:48:35 by armajchr          #+#    #+#              #
#    Updated: 2020/09/09 16:17:06 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  sys
import  math

def usage():
    print("Usage: python operations.py <number1> <number2>\nExample:\n"\
        "	python operations 10 3")
    sys.exit()

def	is_int(s):
    i = len(s) - 1
    while (i >= 0):
        if i == 0 and len(s) > 1 and (s[0] == '-' or (s[0] >= '0' and s[0] <= '9')):
            return (1)
        elif s[0] == '-' and len(s) == 1:
            return (0)
        if i > 0 and s[i] < '0' or s[i] > '9':
            return (0)
        i -= 1
    return (1)

def operations(a, b):
    add = int(a) + int(b)
    diff = int(a) - int(b)
    prod = int(a) * int(b)
    print("Sum:     	", add, "\nDifference:	", diff, "\nProduct:	", prod)
    if (int(b) == 0):
        print("\nQuotient:	ERROR (div by zero)\nRemainder: ERROR (modulo by zero)")
    else:
        quot = int(a) / int(b)
        rem = int(a) % int(b)
        print("Quotient:	", quot, "\nRemainder:	",rem)

def	get_args():
    if len(sys.argv) != 3:
        usage()
        sys.exit()
    if is_int(sys.argv[1]) == 0 or is_int(sys.argv[2]) == 0:
        print("InputError: only numbers\n")
        usage()
    else:
    	operations(sys.argv[1], sys.argv[2])
    
get_args()
    