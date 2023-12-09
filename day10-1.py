## Advent of Code 2023
from utils import *
import numpy as np
aoc = AOC(__file__, True)

report_next_sequence = []

def get_iterations(iteration):
  tmp = ''
  output = []
  for x, y in zip(iteration[0::], iteration[1::]):
    tmp += f"{y-x},"

  return tmp[:-1]
 
for line in aoc.input: 
  iterations = []
  data_line = [int(s) for s in re.findall(r"[\d]+", line)]
  iterations.append([int(s) for s in get_iterations(data_line).split(',')])
  while iterations[-1][-1] != 0:
    iterations.append([int(s) for s in get_iterations(iterations[-1]).split(',')])

  for i in range(1,len(iterations)):
    iterations[i].append(iterations[i][-1] + iterations[i + 1][-1])
  print(iterations)