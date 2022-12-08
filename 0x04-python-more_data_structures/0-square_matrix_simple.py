#!/usr/bin/python3
def square_matrix(matrix=[]):
return [list(map(lamda x: x ** 2, row)) for row in matrix]
