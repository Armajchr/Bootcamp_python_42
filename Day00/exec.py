# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/09 11:36:15 by armajchr          #+#    #+#              #
#    Updated: 2020/09/09 12:53:17 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def swap_rev(s):
    s = s[::-1]
    s = s.swapcase()
    s = s.rstrip()
    print (s)

def get_args(s):
    if len(sys.argv) == 1:
        sys.exit()
    for arg in sys.argv:
        s = s + " " + arg
    return (s[8:])
    
s = ""
s = get_args(s)
swap_rev(s)