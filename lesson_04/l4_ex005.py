# Exercise 5 - Exit loop using break
# Purpose: Use an infinite loop with break to terminate execution based on a condition.

print("Enter a message.")
print('To exit, type "exit".')

while True:
  message = input('')
  print(message)
  if (message == "exit"):
    break