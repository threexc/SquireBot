#!/usr/bin/env python
# Python dice rolling and parsing
# Embed into a bot, service, whatever...
# Was bored...

import random
import re
import sys

def roll(sides):
    """ Roll a (sides) sided die and return the value. 1 <= N <= sides """
    return random.randint(1,sides)

def parse_dice(cmd):
  """ Parse strings like "2d6" or "1d20" and roll accordingly """
  pattern = re.compile(r'^((?P<count>\d*)d(?P<sides>\d*)(?P<mod>[-+*/><]?\d*))*')
  match = re.match(pattern, cmd)

  sides = int(match.group('sides'))
  try:
    mod = int(match.group('mod'))
  except:
    mod = 0
  try:
    count = int(match.group('count')[:-1])
  except:
    count = 1

  print(count)
  print(sides)
  print(mod)

  if count > 1:
    return [ roll(sides) for i in range(count) ]
  else:
    return roll(sides)


if __name__=="__main__":
    print(parse_dice(sys.argv[1]))
