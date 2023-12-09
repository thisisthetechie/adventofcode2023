## Advent of Code 2023
from utils import *
import itertools

aoc = AOC(__file__, True)

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

seed_list = []
current_map = ''
for line in aoc.input:
  if line.startswith('seeds:'):
    
    seeds = [int(s) for s in re.findall(r'\d+', line)]
    for i in range(0, len(seeds), 2):
      seed_list.append(range(seeds[i], seeds[i] + seeds[i+1]))
  
  elif line[0].islower():
    current_map = re.findall(r"[\w-]+",line)[0]
  elif line[0].isnumeric():
    mapping = [int(s) for s in re.findall(r'\d+', line)]
    maps[current_map].append([mapping[1], range(mapping[0], mapping[0] + mapping[2])])


def lookup_map(map, destination):
  output = destination
  for map_value in maps[map]:
    if destination in map_value[1]:
      value_mapped = destination - map_value[1][0]
      output = map_value[0] + value_mapped
  return output

def find_seed(location):
  seed = lookup_map('seed-to-soil', 
    lookup_map('soil-to-fertilizer', 
      lookup_map('fertilizer-to-water', 
        lookup_map('water-to-light', 
          lookup_map('light-to-temperature', 
            lookup_map('temperature-to-humidity',
              lookup_map('humidity-to-location', location)
            )
          )
        )
      )
    )
  )

  return seed

location = 0
closest_location = ''
while closest_location == '':
  
  seed = find_seed(location)
  if seed in [ list for list in seed_list]:
    closest_location = location
    break
  else:
    location += 1

print(f"Closest Location: {location}")
