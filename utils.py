import random
import time

def makeMatricesRandom(matrix_a, matrix_b, result, size):
  default_range = 9
  max_range = size if size > default_range else default_range

  for x in range(0, size):
    matrix_a.append(random.sample(range(max_range), size))
    matrix_b.append(random.sample(range(max_range), size))
    result.append([0] * size)

def makeMatrices(matrix_a, matrix_b, result, size):
  data_a = open("matrices/A%sx%s.txt" % (size, size), 'r')
  data_b = open("matrices/B%sx%s.txt" % (size, size), 'r')

  for x in range(0,size):
    if x == 0:
      data_a.readline()
      data_b.readline()

    line_a = list(map(int, data_a.readline().split('\n')[0].strip().split(' ')))
    line_b = list(map(int, data_b.readline().split('\n')[0].strip().split(' ')))

    matrix_a.append(line_a)
    matrix_b.append(line_b)
    result.append([0] * size)

def printResult(result, size):
  result_file = open("matrices/C%sx%s.txt" % (size, size), 'w')

  for x in range(0, len(result)):
    line = ' '.join(list(map(str, result[x])))
    result_file.write(line)
    result_file.write("\n")

