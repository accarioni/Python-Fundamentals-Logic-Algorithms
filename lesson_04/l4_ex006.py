# Exercise 6 - Login validation with continue
# Purpose: Validate user credentials by repeating input until correct login information is provided.

while True:
  username = input('Enter the username: ')
  if (username != "student"):
    continue
  password = input('Enter the password: ')
  if (password == "student"):
   break

print(f'Access granted. Welcome, {username}!')