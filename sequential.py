#!/usr/bin/python

import random
import time
import sys

default_size = int(sys.argv[1])
matrix_a = []
matrix_b = []
result = []

def makeMatrices():
  for x in range(0,default_size):
    matrix_a.append(random.sample(xrange(default_size), default_size))
    matrix_b.append(random.sample(xrange(default_size), default_size))
    result.append([0] * default_size)

def makeMultiplication():
  for i in range(len(matrix_a)):
    for j in range(len(matrix_b[0])):
      for k in range(len(matrix_b)):
        result[i][j] += matrix_a[i][k] * matrix_b[k][j]

def printMatrices():
  print('Matrix A')
  print(matrix_a)
  print('\n')
  print('Matrix B')
  print(matrix_b)
  print('\n')
  print('Resultado')
  print(result)

makeMatrices()
makeMultiplication()
printMatrices()
