Username Validator (Python)

A simple Python program that validates a username based on basic rules.
This project is created to practice string methods, conditional statements, and user input handling in Python.

📌 Validation Rules

The username must satisfy the following conditions:

Must not exceed 12 characters

Must not contain spaces

Must contain only alphabetic characters (no digits or symbols)

🧠 Concepts Used

input() for user input

len() to check string length

String membership (" " in username)

String method: isalpha()

if-elif-else conditional statements

💻 Code
# Validate user input
# 1. User input must not be more than 12 characters.
# 2. User input must not contain spaces.
# 3. User input must not contain digits.

▶️ Sample Output
Enter your username: john123
Username must not contain digits

Enter your username: john doe
Username must not contain spaces

Enter your username: johndoe
Hello johndoe !

🚀 How to Run

Make sure Python is installed

Save the file as username_validator.py

Run the program:

python username_validator.py

📂 Project Purpose

This project is part of my Python learning journey and helps in understanding:

Input validation

String handling

Writing clean conditional logic


