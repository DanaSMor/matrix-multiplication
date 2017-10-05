#!/usr/bin/python

import sys
import utils

def makeMultiplication():
  for i in range(len(matrix_a)):
    for j in range(len(matrix_b[0])):
      for k in range(len(matrix_b)):
        result[i][j] += matrix_a[i][k] * matrix_b[k][j]

default_size = int(sys.argv[1])
matrix_a = []
matrix_b = []
result = []

utils.makeMatrices(matrix_a, matrix_b, result, default_size)
makeMultiplication()
utils.printMatrices(matrix_a, matrix_b, result)
