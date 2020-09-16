# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/15 14:42:29 by armajchr          #+#    #+#              #
#    Updated: 2020/09/16 15:22:16 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from vector import Vector

class Matrix:
    def __init__(self, data=None, shape=None):
        count1 = 0
        count2 = 0
        self.data = []
        tmp = []
        if isinstance(data, list):
            for i in data:
                count1 += 1
                for y in range(3):
                    count2 += 1
                tmp.append(i)
            self.data.extend(tmp)
            tmp = []
            self.shape = tuple((count1, count2/count1))
        if isinstance(data, tuple):
            shape = (data[0], data[1])
            for i in range(shape[0]):
                for y in range(shape[1]):
                    count2 += 1
                    tmp.append(float(0))
                self.data.insert(i, tmp)
                tmp = []
            self.shape = shape
        if data == None and shape == None:
            print("Error: no info given")
            sys.exit()
    
    def __add__(self, op):
        final = Matrix(self.data)
        if isinstance(op, Matrix):
            for i in range(self.shape[0]):
                for y in range(self.shape[1]):
                    final.data[i][y] = self.data[i][y] + op.data[i][y]
        return (final)
    
    def __radd__(self, op):
        return (self.__add__(op))
    
    def __mul__(self, op):
        if isinstance(op, int):
            final = Matrix(self.data)
            for i in range(self.shape[0]):
                for y in range(self.shape[1]):
                    final.data[i][y] = self.data[i][y] * op
        if isinstance(op, Vector):
            final = Matrix((1, self.shape[1]))
            print(final)
            for i in range(self.shape[0] - 1):
                for y in range(self.shape[1]):
                    k = 0
                    while k <= self.shape[1] - 2:
                        final.data[i][y] += self.data[i + k][y] * op.values[k]
                        k += 1
        if isinstance(op, Matrix):
            final = Matrix((self.shape[0], self.shape[1]))
            print(final)
            for i in range(self.shape[0]):
                for y in range(self.shape[1]):
                    k = 0
                    while k <= self.shape[1] - 2:
                        final.data[i][y] += self.data[i + k][y] * op.data[i + k][y]
                        k += 1
                        print("i = ", i, "y = ", y, "k = ", k)
        return (final)
    
    def __str__(self):
        txt = "Matrix data : " + str(self.data)
        txt += "\nShape : " + str(self.shape)
        return (txt)
    
    def __repr__(self):
        txt = str(self.data + " : " + str(self.shap))
        return (txt)
     

m1 = Matrix([[2.0, 1.0, 3.0], [5.0, 9.2, 6.4]])
#m2 = Matrix((2,3))
m3 = Matrix([[2.0, 2.0, 2.0], [2.0, 2.0, 2.0]])
#v1 = Vector((1,5))
print(m1)
#print(m2)
print(m3)
print(m1 * m3)
#print(m2 * v1)