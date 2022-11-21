#!/bin/python3
import random

# Show the game instructions on the screen
print("I am thinking of a number between one and five. Can you guess it?")

# Generate a random integer (whole number) and make it a string
random_number = random.randint(1,5)
random_number = str(random_number)

# Get the user to input their guess
guess = input("What is your guess? -->")

# Check the answer
if guess == random_number:
  print("Correct!") # Only show this if it was correct
else:
  print("That is not it!") # Only show this if it was correct

# Show this message if they got it right or wrong
print("I was thinking of the number: "+ random_number) 