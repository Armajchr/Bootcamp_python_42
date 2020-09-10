# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/10 12:52:18 by armajchr          #+#    #+#              #
#    Updated: 2020/09/10 13:31:23 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

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

def get_args():
    if len(sys.argv) != 3:
        print("ERROR")
        sys.exit()
    if is_int(sys.argv[1]):
        print("ERROR")
        sys.exit()
    filterwords(str(sys.argv[1]), int(sys.argv[2]))

def filterwords(s,a):
    s = s.split()
    count = -1
    for i in s:
        count += 1
        for y in i:
            if y < 'A' or (y > 'Z' and y < 'a') or y > 'z':
                del s[count]
        if len(i) <= a:
            del s[count]
    print(s)

get_args()