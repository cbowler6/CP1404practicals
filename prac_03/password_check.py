"""
Cameron Bowler
"""
MIN_LENGTH = 3


def main():
    password = get_password(MIN_LENGTH)

    print("*" * len(password))


def get_password(minimum):
    password = input("Enter password:")
    while len(password) < minimum:
        print("Password must be greater than two letters")
        password = input("Enter password:")
    return password


main()
