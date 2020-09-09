# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/09 16:21:45 by armajchr          #+#    #+#              #
#    Updated: 2020/09/09 16:25:11 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdof',
}

for keys, values in languages.items():
    print(keys, "was created by", values) 