from prac_06.car import Car

print("Let's drive!")
car_name = input("Enter your car name:")
car_name = Car(100, car_name)

print(car_name, "\nMenu\nd) drive\nr) refuel\nq) quit")

choice = input("Enter your choice:").upper()
while choice != "Q":
    if choice == "D":
        distance_to_drive = int(input("How many km do you wish to drive?"))
        while distance_to_drive < 0:
            print("Distance must be >= 0")
            distance_to_drive = int(input("How many km do you wish to drive?"))
        if distance_to_drive > car_name.fuel:

            print("The car drove {}km and ran out of fuel.".format(car_name.fuel))
            car_name.drive(distance_to_drive)
        else:
            car_name.drive(distance_to_drive)
            print("The car drove {}km".format(distance_to_drive))
    if choice == "R":
        fuel = int(input("How many units of fuel do you want to add to the car?"))
        while fuel < 0:
            print("Fuel amount must be >= 0")
            fuel = int(input("How many units of fuel do you want to add to the car?"))
        print("added {} units of fuel.".format(fuel))
        car_name.add_fuel(fuel)
    else:
        print("Invalid choice\n")  # why is this printing after user enters the distance they wish to drive

    print(car_name, "\nMenu\nd) drive\nr) refuel\nq) quit")
    choice = input("Enter your choice:").upper()
print("Good bye {}'s driver.".format(car_name.name))

