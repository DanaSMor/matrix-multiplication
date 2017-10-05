import random
import time

def makeMatrices(matrix_a, matrix_b, result, default_size):
  max_range = default_size if default_size > 10 else 9

  for x in range(0, default_size):
    matrix_a.append(random.sample(range(max_range), default_size))
    matrix_b.append(random.sample(range(max_range), default_size))
    result.append([0] * default_size)

def printMatrices(matrix_a, matrix_b, result):
  print('Matrix A')
  print(matrix_a)
  print('\n')
  print('Matrix B')
  print(matrix_b)
  print('\n')
  print('Resultado')
  print(result)