def main():
    total = 0
    number_of_items = int(input("Number of items:"))
    while number_of_items < 0:
        print("invalid number of items")
        number_of_items = int(input("Number of items:"))
    for i in range(number_of_items):
        price = float(input("Prize of item:"))
        total += price
    if total >= 100:
        total *= 0.9
    print("Total price for", i+1, "items is {:.2f}".format(total))


main()
