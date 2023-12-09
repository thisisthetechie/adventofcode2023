## Advent of Code 2023
from utils import *

aoc = AOC(__file__, False)

value_sum = []
for line in aoc.input:
  numeric_values = ''
  for char in line:
    if char.isnumeric():
      numeric_values += char

  print(numeric_values[0] + numeric_values[-1])
  value_sum.append(int(numeric_values[0] + numeric_values[-1]))

print(f"Total Value of numbers is: {sum(value_sum)}")