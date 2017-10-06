#!/usr/bin/python

import sys
import utils

def makeMultiplication():
  for i in range(len(matrix_a)):
    for j in range(len(matrix_b[0])):
      for k in range(len(matrix_b)):
        result[i][j] += matrix_a[i][k] * matrix_b[k][j]

default_size = 4
size = int(sys.argv[1]) if len(sys.argv) > 1 else default_size
matrix_a = []
matrix_b = []
result = []

utils.makeMatrices(matrix_a, matrix_b, result, size)
makeMultiplication()
utils.printResult(result, size)
