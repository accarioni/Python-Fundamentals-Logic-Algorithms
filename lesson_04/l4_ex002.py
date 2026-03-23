# Exercise 2 - Counter exercise
# Purpose: Collect a fixed number of values and calculate their average.

sum_grades = 0
counter = 1

while (counter <= 5):
  grade = float(input(f'Enter grade {counter}: '))
  sum_grades = sum_grades + grade
  counter = counter + 1

final_average = sum_grades / 5

print(f'Your final average is {final_average}')