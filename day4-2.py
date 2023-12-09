## Advent of Code 2023
from utils import *

aoc = AOC(__file__, False)

value_sum = []

cards = []
card_orig = []
agg = []
for line in aoc.input:
  win_cards = 0
  card_number = int(re.findall(r"Card\s+(\d+)", line)[0])
  data_split = line.split(':')[1]
  win_data = re.findall(r"(\d+)", data_split.split('|')[0])
  card_data = re.findall(r"(\d+)", data_split.split('|')[1])
  cards.append([card_number, win_data, card_data,1])
  card_orig.append([card_number, win_data, card_data])
for card in cards:
  tmp = 0
  for number in card[2]:
    if number in card[1]:
      tmp += 1
  for i in range(card[-1]):
    for n in range(card[0], card[0] + tmp):
      cards[n][-1] += 1
for card in cards:
  agg.append(card[-1])
print(f'Total Cards: {sum(agg)}')

  