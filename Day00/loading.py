# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/10 16:28:11 by armajchr          #+#    #+#              #
#    Updated: 2020/09/10 16:32:06 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_progress(lst):
    ret = 0
    for elem in ft_progress(lst):
        ret += elem
        print("ETA:")
        yield ret