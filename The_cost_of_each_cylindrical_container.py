import math
radius = input (" Enter The radius of the cylindrical container : ")
height = input (" Enter The height of the cylindrical container : ")
cost = input (" Enter the cost per cm square cylindrical container : ")
# type casting
r = float(radius)
h = float(height)
c = float(cost)
A = (2*math.pi*r*h) + (math.pi*(r**2))
The_cost = A*c
print ("the cost of the container = " ,The_cost)
