# hypotnuse -> sqrt(base * base + height * height)

import math

# input
base = 3
height = 4

# process
hypotenuse = math.sqrt(math.pow(base, 2) + math.pow(height, 2))

# output
print("The hypotenuse of given right angle traingle with base ", base, " and height ", height, " is : ", hypotenuse)