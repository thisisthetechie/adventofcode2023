## Advent of Code 2023
from utils import *

aoc = AOC(__file__, False)

def identify_numbers(input):
  results = re.findall(r"(?<=(?=(\d|one|two|three|four|five|six|seven|eight|nine)))", input)
  output = ''
  for number in results:
    if number.isnumeric():
      output += number
    else:
      output += str(number_text[number])
  return output


value_sum = []
for line in aoc.input:
  numeric_values = identify_numbers(line)  
  print(numeric_values[0] + numeric_values[-1])
  value_sum.append(int(numeric_values[0] + numeric_values[-1]))

print(f"Total Value of numbers is: {sum(value_sum)}")