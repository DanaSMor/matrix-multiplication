#!/usr/bin/python

import sys
import utils
import time
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

default_size = 4
size = int(sys.argv[1]) if len(sys.argv) > 1 else default_size
total_time = 0

for x in range(0,20):
  matrix_a = []
  matrix_b = []
  result = []

  start_time = time.time()
  utils.makeMatrices(matrix_a, matrix_b, result, size)
  makeMultiplication()
  utils.printResult(result, size)
  end_time = time.time()

  print("Matrix multiplication to %sx%s size was finished in %s" % (size, size, (end_time - start_time)))
  total_time += (end_time - start_time)

print("Total time to 20 execution was %s. Average time was %s" % (total_time, (total_time/20)))