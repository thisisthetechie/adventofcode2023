import re

class AOC:
    def __init__(self, file, example):
      day = re.findall(r"day(\d+)-(\d+).+", file)[0]
      if example:
          self.input = open(f"day{day[0]}-example.txt")
      else:
          self.input = open(f"day{day[0]}.txt")
      print ('{:-^31}'.format("\U0001F384" + "Advent of Code 2023"))
      print ('{:-^32}'.format(f"Day {day[0]} Part {day[1]}"))

number_text = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}