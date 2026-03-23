# Exercise 9 - Algorithms using for and while
# Purpose: Generate multiplication tables using nested loops.

n = 0

for i in range(1, 11, 1):
  n += 1
  print(f'\n Multiplication table of {n}:\n')

  for multiplier in range(1, 11, 1):
    multiplication = multiplier * n
    print(f'{n} x {multiplier} = {multiplication}')