"""
Cameron Bowler
"""

MIN_LENGTH = 3

password = input("Enter password:")
while len(password) < MIN_LENGTH:
    print("Password must be greater than two letters")
    password = input("Enter password:")

print("*" * len(password))