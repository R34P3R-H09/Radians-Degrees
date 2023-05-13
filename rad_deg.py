#A small maths conversion programme that will convert a users input in Radians and convert it to Degrees.

import math

rads = int(input('Please enter the value in Radians: ')) #Asking for the user input.

degs = (math.cos(math.radians(rads)))*(180/math.pi) #The calculation to convert.

print(degs) #Value in degrees.






