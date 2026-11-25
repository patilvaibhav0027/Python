# Assignment 3
# Find the area of a circle with radius 7 (π × r²), rounded to 2 decimals, and also its ceil and floor.
# Find the hypotenuse of a right triangle with sides 3 and 4.
# Print the smallest and largest of 8, 3, 15, -2.

import math

radius = 7
#area of the circle
area = math.pi * math.pow(radius, 2) #math - module and pi, pow are the functions
print(round(area,2)) #round is the function used 2 is the no.of integers after point
print(math.ceil(area)) #lower nearest number
print(math.floor(area)) #highest nearest number

# Find the hypotenuse of a right triangle with sides 3 and 4.
#hypotenuse = sqrt of the (square sum of 2 sides)
print(math.sqrt(pow(3,2)+pow(4,2)))

# Print the smallest and largest of 8, 3, 15, -2.
print("smallest", min(8, 3, 15, -2))
print("largest", max(8, 3, 15, -2)) 
 