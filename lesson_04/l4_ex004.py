# Exercise 4 - Exit loop using a keyword
# Purpose: Repeat user input until a specific keyword is entered.

print('Enter a sentence that will be repeated by the program.')
print('To exit, type "exit".')
text = input('Enter a sentence: ')
print(text)

while (text != "exit"):
  text = input('Enter a sentence: ')
  print(text)