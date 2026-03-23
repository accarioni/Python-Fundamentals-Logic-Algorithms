# Exercise 1 - Counter exercise
# Purpose: Iterate through a range of numbers and print only the even numbers.

num_start = int(input("Enter the starting number (smaller number): "))
num_end = int(input("Enter the ending number (greater number): "))

while (num_start <= num_end):
  if (num_start % 2 == 0):
    print(num_start)
  num_start = num_start + 1