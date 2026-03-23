# Exercise 2 - Simple conditional
# Purpose: Apply basic conditional statements (if) to execute code based on logical conditions.

age = 62

if(age > 60):
    print('You are eligible for benefits.')

damage = 10
shield = 5

if((damage > 10) and (shield == 0)):
    print('You are dead!')

north = True
east = False
west = False
south = True

if((north == True) or (east == True) or (south == True) or (west == True)):
  print('You escaped')