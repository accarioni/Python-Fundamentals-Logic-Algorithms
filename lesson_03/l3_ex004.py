# Exercise 4 - Triangle classification
# Purpose: Validate triangle conditions and classify it as equilateral, isosceles, or scalene.

side1 = int(input('What is the length of the first side of the triangle? '))
side2 = int(input('What is the length of the second side of the triangle? '))
side3 = int(input('What is the length of the third side of the triangle? '))

if((side1 > 0) and (side2 > 0) and (side3 > 0) and (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)):
  # If all conditions are met, it is a valid triangle

  if(side1 == side2 == side3):
    print('Equilateral Triangle')

  elif(side1 == side2 or side1 == side3 or side2 == side3):
    print('Isosceles Triangle')

  elif(side1 != side2 != side3):
    print('Scalene Triangle')

else:
  print('At least one of the given values cannot form a triangle')