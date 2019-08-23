def main():
    UPPER = 127
    LOWER = 33

    # character = input("Enter a character:")
    # print("The ASCII code for {} is {}".format(character, ord(character)))
    # ASCII_code = int(input("Enter a number between 33 and 127"))
    # while ASCII_code < LOWER or ASCII_code > UPPER:
    #     print("must be a number between 33 and 127")
    #     ASCII_code = int(input("Enter a number between 33 and 127"))
    # print("The character for {} is {}".format(ASCII_code, chr(ASCII_code)))


    # for i in range(33, 127):
    #     print("{:>3}  {}".format(i, chr(i)))

    num_line = int(input("Enter lines to be printed: "))
    for i in range(33, num_line + 33):
        print("{:>3}  {}".format(i, chr(i)))

main()
