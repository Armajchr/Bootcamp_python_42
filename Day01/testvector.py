# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    testvector.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/15 10:37:57 by armajchr          #+#    #+#              #
#    Updated: 2020/09/15 14:40:05 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

## Creation des vecteurs
v1 = Vector([1, 2, 3, 4 , 5]) #liste
v2 = Vector((6, 11)) #tuple
v3 = Vector((11, 16)) #tuple

#Tests avec int
v4 = v1 + 2
print(repr(v4))
v5 = v2 - 6
print(repr(v5))
v6 = v3 * 10
print(repr(v6))
v7 = v1 / 4
print(repr(v7))

#test avec int reverse
v8 = 2 + v1
print(repr(v8))
v9 = 6 - v2
print(repr(v9))
v10 = 10 * v3
print(repr(v10))
v11 = 4 / v1
print(repr(v11))

#test avec vecteurs
v12 = v1 + v2
print(repr(v12))
v13 = v2 - v3
print(repr(v13))
v14 = v3 * v1
print(repr(v14))
v15 = v1 / v2
print(repr(v15))

#test avec vecteur reverse
v16 = v2 + v1
print(repr(v16))
v17 = v3 - v2
print(repr(v17))
v18 = v1 * v3
print(repr(v18))
v19 = v2 / v1
print(repr(v19))
