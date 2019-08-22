def main():
    name = input("Please enter your name: ")
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    out_file.close()


    in_file = open("name.txt", "r")
    name = in_file.read().strip()
    print("Your name is", name)
    in_file.close()


    in_file = open("numbers.txt", "r")
    total = 0
    for line in in_file:
        total += int(line)
    print(total)
    in_file.close()


main()
