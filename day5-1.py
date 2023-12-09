## Advent of Code 2023
from utils import *
from tabulate import tabulate
import pandas as pd
import numpy
import array
aoc = AOC(__file__, False)

seeds = []
maps = {
  "seed-to-soil": [],
  "soil-to-fertilizer": [],
  "fertilizer-to-water": [],
  "water-to-light": [],
  "light-to-temperature": [],
  "temperature-to-humidity": [],
  "humidity-to-location": []
}
locations = []


current_map = ''
for line in aoc.input:
  if line.startswith('seeds:'):
    seeds = [int(s) for s in re.findall(r'\d+', line)]
  elif line[0].islower():
    current_map = re.findall(r"[\w-]+",line)[0]
  elif line[0].isnumeric():
    maps[current_map].append([int(s) for s in re.findall(r'\d+', line)])

def lookup_map(map, source):
  for map_value in maps[map]:
    destination_start = int(map_value[0])
    source_start = int(map_value[1])
    range_length = int(map_value[2])

    if source in range(source_start, source_start + range_length):
      value_mapped = source - source_start
      return destination_start + value_mapped

def process_lookup(map_to_search, value):
  tmp = lookup_map(map_to_search, value)
  if tmp == None:
    tmp = value
  return tmp


for seed in seeds:
  soil = process_lookup('seed-to-soil', seed)

  fertilizer = process_lookup('soil-to-fertilizer', soil)

  water = process_lookup('fertilizer-to-water', fertilizer)

  light = process_lookup('water-to-light', water)

  temperature = process_lookup('light-to-temperature', light)

  humidity = process_lookup('temperature-to-humidity', temperature)

  location = process_lookup('humidity-to-location', humidity)

  locations.append(location)
print(f"Closest Location: {min(locations)}")
