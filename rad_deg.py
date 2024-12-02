# A small maths conversion programme that will convert a users input in Radians and convert it to Degrees.
# I decided to do this whilst doing a University course.
# Copyright (C) R34P3R-H09.

import math

rads = int(input('Please enter the value in Radians: ')) #Asking for the user input.

degs = (math.cos(math.radians(rads)))*(180/math.pi) #The calculation to convert.

print(degs) #Value in degrees.






