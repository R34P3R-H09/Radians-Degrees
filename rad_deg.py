# A small maths conversion programme that will convert a users input in Radians and convert it to Degrees.
# I decided to do this whilst doing a University course. I found that i had a lot of conversions to do in a short amount of time.
# This seemed like a good idea to save the time.
# Copyright (C) R34P3R-H09.

import math

rads = int(input('Please enter the value in Radians: ')) #Asking for the user input in Rads

degs = (math.cos(math.radians(rads)))*(180/math.pi) #The calculation to convert the users input in Rads to DegS.

print(degs) # Prints the required value in degrees.






