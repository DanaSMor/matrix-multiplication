#!/usr/bin/python

import sys
import utils
import time

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

start_time = time.time()
utils.makeMatrices(matrix_a, matrix_b, result, size)
makeMultiplication()
utils.printResult(result, size)
end_time = time.time()

print("Matrix multiplication to %sx%s size was finished in %s" % (size, size, (end_time - start_time)))
