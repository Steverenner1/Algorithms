#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batch = 0
  counter = 0
  for i in recipe:
    try:
      batches = ingredients[i] // recipe[i] # 1st loop = 1st ingredient, etc
    except:
      batches = 0
    if counter == 0 or batches <= max_batch:
      max_batch = batches
    counter += 1
  return max_batch


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }
  # ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))