"""
Cameron Bowler
"""


def main():
    MIN_LENGTH = 3

    password = get_password(MIN_LENGTH)

    print("*" * len(password))


def get_password(MIN_LENGTH):
    password = input("Enter password:")
    while len(password) < MIN_LENGTH:
        print("Password must be greater than two letters")
        password = input("Enter password:")
    return password


main()
