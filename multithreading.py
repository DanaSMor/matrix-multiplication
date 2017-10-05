#!/usr/bin/python

import sys
import utils
from threading import Thread

class Calculator(Thread):
  def __init__(self, line_matrix_a):
    Thread.__init__(self)
    self.line = line_matrix_a

  def run(self):
    for j in range(len(matrix_b[0])):
      for k in range(len(matrix_b)):
        result[self.line][j] += matrix_a[self.line][k] * matrix_b[k][j]

def makeMultiplication():
  for i in range(len(matrix_a)):
    worker = Calculator(i)
    worker.start()

default_size = int(sys.argv[1])
matrix_a = []
matrix_b = []
result = []

utils.makeMatrices(matrix_a, matrix_b, result, default_size)
makeMultiplication()
utils.printMatrices(matrix_a, matrix_b, result)