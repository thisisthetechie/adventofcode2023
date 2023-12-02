## Advent of Code 2023
from utils import *

aoc = AOC(__file__, False)

value_sum = []
for line in aoc.input:
  max_ball_count = {
    "red": 0,
    "green": 0,
    "blue": 0
  }
  game_number = re.findall(r"Game\s(\d+).+", line)[0]
  game_data = re.findall(r"[^;]+", line.split(': ')[1].replace('\n',''))
  for game_line in game_data:
    game_balls = re.findall(r"(\d+)\s(\w+)",game_line)
    for game_ball in game_balls:
      if int(game_ball[0]) > max_ball_count[game_ball[1]]:
        max_ball_count[game_ball[1]] = int(game_ball[0])
  
  print(f'Game {game_number}: {max_ball_count}')
  value_sum.append(max_ball_count['red'] * max_ball_count['green'] * max_ball_count['blue'])


print(f'Sum of valid games: {sum(value_sum)}')

