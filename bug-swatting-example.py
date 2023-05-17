#!/bin/python3
import random
import time
import math


# Examples
fact = "A cow has four stomachs"
number = 10
number = 9
number = 16
square_root = math.sqrt(number)

# Now you try these
random_number = random.randint(1,100)
random_choice = random.choice(["red", "green", "blue"])
cards = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A"]
random.shuffle(cards) # This one has no variable, it works with the variable above
seconds_since_NYD_1970 = time.time() # I will explain this later
gmt_time = time.gmtime()
pretty_time = time.asctime(gmt_time)

print(number) 