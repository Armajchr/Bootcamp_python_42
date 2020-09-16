# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: armajchr <armajchr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/15 10:37:32 by armajchr          #+#    #+#              #
#    Updated: 2020/09/15 14:41:17 by armajchr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Vector:
    def __init__(self, values, size=None):
        count = 0
        if  isinstance(values, int):
            self.values = []
            for i in values:
                self.values.append(float(i))
                count += 1
            if size == None:
                self.size = count
            else:
                self.size = size
        elif isinstance(values, tuple):
            self.values = []
            for i in range(values[0], values[1]):
                self.values.append(float(i))
                count += 1
            if size == None:
                self.size = count
            else:
                self.size = size
        elif isinstance(values, list):
            self.values = values
            if size == None:
                self.size = len(values)
            else:
                self.size = size

    def __add__(self,op):
        final = Vector(self.values)
        if isinstance(op, int):
            for i in range(self.size):
                final.values[i] = self.values[i] + op
                print(final.values[i])
        elif isinstance(op, Vector):
            for i in range(self.size):
                final.values[i] = self.values[i] + op.values[i]
        return (final)
     
    def __radd__(self, op):
        return (self.__add__(op))
     
    def __sub__(self, op):
        final = Vector(self.values)
        if isinstance(op, int):
            for i in range(self.size):
                final.values[i] = self.values[i] - op
        elif isinstance(op, Vector):
            for i in range(self.size):
                final.values[i] = self.values[i] - op.values[i]
        return (final)
    
    def __rsub__(self, op):
        final = Vector(self.values)
        if isinstance(op, int):
            for i in range(self.size):
                final.values[i] = op - self.values[i]
        elif isinstance(op, Vector):
            for i in range(self.size):
                final.values[i] = op - self.values[i]
        return (final)
    
    def __div__(self, op):
        final = Vector(self.values)
        if isinstance(op, int):
            if op == 0:
                print("Error: div by 0 impossible")
                return False
            else:
                for i in range(self.size):
                    final.values[i] = self.values[i] / op
        elif isinstance(op, Vector):
            for i in range(self.size):
                if i == 0:
                    print("Error: Div by 0 impossible")
                    return False
                else:
                    final.values[i] = self.values[i] / op.values[i]
        return (final)
    
    def __rdiv__(self, op):
        final = Vector(self.values)
        if isinstance(op, int):
            for i in range(self.size):
                if i == 0:
                    print("Error: Div by 0 impossible")
                    return False
                else:
                    final.values[i] = op / self.values[i]
        elif isinstance(op, Vector):
            for i in range(self.values):
                if i == 0:
                    print("Error: div value by 0 impossible")
                    return False
                else:
                    final.values[i] = op.values[i] / self.values[i]
        return (final)
    
    def __mul__(self, op):
        final = Vector(self.values)
        if isinstance(op, int):
            for i in range(self.size):
                final.values[i] = self.values[i] * op
        elif isinstance(op, Vector):
            for i in range(self.size):
                final.values[i] = self.values[i] * op.values[i]
        return (final)
    
    def __rmul__(self, op):
        return (self.__mul__(op))
    
    def __str__(self):
        txt = "vector values : " + str(self.values)
        txt += "\nNbr values : " + str(self.size)
        return (txt)
    
    def __repr__(self):
        txt = str(self.values) + " : " + str(self.size)
        return (txt)
        