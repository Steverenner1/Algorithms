#!/usr/bin/python

import sys

gamePlay = [["rock"], ["paper"], ["scissors"]]
def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  if n == 1: # how many valid plays are done with rock
    return gamePlay
 
  result = []

  arrA = rock_paper_scissors(n - 1)
  
  for subArr in arrA:
    for play in gamePlay:
      newPlay = subArr + play
      result.append(newPlay)

  return result

print(rock_paper_scissors(4))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')