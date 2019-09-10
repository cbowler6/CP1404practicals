from prac_06.guitar import Guitar


guitars = []
name = input("name:")
while name != "":
    year = input("year:")
    cost = input("cost:")
    added_guitar = Guitar(name, year, cost)
    guitars.append(added_guitar)
    print(added_guitar, "added.")
    name = input("name:")

if guitars:  # lists, strings and other collections are False when empty, True when non-empty
    # In order for sorting to work on Guitar objects,
    # at least the __lt__ method must be defined in Guitar class
    guitars.sort()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
           {2}".format(i + 1, guitar, vintage_string))
else:
    print("No guitars :( Quick, go and buy one!")








# print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))