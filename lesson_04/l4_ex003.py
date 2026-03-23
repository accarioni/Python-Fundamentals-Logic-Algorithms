# Exercise 3 - Input validation with a loop
# Purpose: Ensure the user enters a valid value using a loop for validation.

value = int(input('Enter a value greater than zero: '))
while (value <= 0):
  value = int(input('Enter a value greater than zero: '))
print(f'You entered {value}. Ending the program.')


# Exercise 3 (Professor) - Exit loop using break
# Purpose: Use an infinite loop with break to terminate execution based on a condition.

print("Enter a message.")
print('To exit, type "exit".')

while True:
  message = input('')
  print(message)
  if (message == "exit"):
    break