## Advent of Code 2023
from utils import *

aoc = AOC(__file__, False)

value_sum = []
for line in aoc.input:
  score = 0
  
  card_number = re.findall(r"Card\s+(\d+)", line)[0]
  data_split = line.split(':')[1]
  win_data = re.findall(r"(\d+)", data_split.split('|')[0])
  card_data = re.findall(r"(\d+)", data_split.split('|')[1])
  for i in card_data:
    if i in win_data:
      if score > 0:
        score = score * 2
      else:
        score += 1
  value_sum.append(score)
  print(f'Card {card_number}: Score {score}')
  
print(f'Total Score: {sum(value_sum)}')

  