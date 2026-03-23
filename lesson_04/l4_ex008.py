# Exercise 8 - Algorithms using "for"
# Purpose: Iterate through a range, filter even numbers, and compute their average.

counter = 0
sum_values = 0

for i in range(1, 101):
  if (i % 2 == 0):
    counter += 1
    sum_values += i

average = sum_values / counter

print(f'The average of even numbers from 0 to 100 is {average}')