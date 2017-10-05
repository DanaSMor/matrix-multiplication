import random
import time

def makeMatrices(matrix_a, matrix_b, result, size):
  default_range = 9
  max_range = size if size > default_range else default_range

  for x in range(0, size):
    matrix_a.append(random.sample(range(max_range), size))
    matrix_b.append(random.sample(range(max_range), size))
    result.append([0] * size)

def printMatrices(matrix_a, matrix_b, result):
  print('Matrix A')
  print(matrix_a)
  print('\n')
  print('Matrix B')
  print(matrix_b)
  print('\n')
  print('Resultado')
  print(result)