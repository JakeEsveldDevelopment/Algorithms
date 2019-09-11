#!/usr/bin/python

import math
import sys

def recipe_batches(recipe, ingredients):
  max_batches = sys.maxsize

  for i in recipe:  
    try:
      ingredients_i_batches = ingredients[i] // recipe[i]
      if ingredients_i_batches < max_batches:
        max_batches = ingredients_i_batches
    except:
      max_batches = 0

  return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))