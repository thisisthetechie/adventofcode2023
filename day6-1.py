## Advent of Code 2023
from utils import *

aoc = AOC(__file__, True)

time = []
distance = []
speed = 6

for line in aoc.input:
  if line.startswith('Time'):
    time = [int(s) for s in re.findall(r"[\d]+", line)]
  elif line.startswith('Distance'):
    distance = [int(s) for s in re.findall(r"[\d]+", line)]

for run in time:
  for hold_time in range(run):
    distance_travelled = hold_time * 6
    print(distance_travelled)