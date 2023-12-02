## Advent of Code 2023
from utils import *

aoc = AOC(__file__, False)

max_ball_count = {
  "red": 12,
  "green": 13,
  "blue": 14
}

value_sum = []
for line in aoc.input:
  game_number = re.findall(r"Game\s(\d+).+", line)[0]
  valid_game = True
  game_data = re.findall(r"[^;]+", line.split(': ')[1].replace('\n',''))
  for game_line in game_data:
    game_balls = re.findall(r"(\d+)\s(\w+)",game_line)
    for game in game_balls:
      if int(game[0]) > max_ball_count[game[1]]:
        valid_game = False
        continue
  
  print(f'Game {game_number}: {valid_game}')
  if (valid_game):
    value_sum.append(int(game_number))

print(f'Sum of valid games: {sum(value_sum)}')

