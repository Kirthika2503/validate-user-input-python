# Validate user input
# 1. User input must contain more than 12 characters.
# 2. User input must not contain spaces.
# 3. User input must not contain digits.
 
username = input("Enter your username: ")

if len(username) > 12:
  print("Username must not be more than 12 characters")

# elif not username.find(" ") == -1 can also be used.
# username.find(" ") == -1 is true when username does not contain spaces.
# if username is github then username.find(" ") is 1.
elif " " in username:
  print("Username must not contain spaces")

# elif not username.isaplha() can also be used.
elif username.isalpha() == False: 
  print("Username must not contain digits")

else:
  print(f"Hello {username} !")