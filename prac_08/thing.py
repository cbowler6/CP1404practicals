from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    current_fare = 0

    menu(taxis, current_taxi, current_fare)
    print("Taxis are now:")
    for taxi in taxis:
        print(taxi)


def menu(taxis, current_taxi, current_fare):
    choice = None
    while choice != "Q":
        choice = input("Let's Drive!\nq)uit, c)hoose taxi, d)rive").upper()
        if choice == "C":
            print("Taxi's available:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_choice = int(input("Choose taxi:"))
            current_taxi = taxis[taxi_choice]

        if choice == "D":
            if current_taxi is not None:
                current_taxi.start_fare()
                current_taxi.drive(int(input("Drive how far:")))
                current_fare += current_taxi.get_fare()
                print("Your {} trip cost you {}".format(current_taxi.name, current_taxi.get_fare()))
        print("Bill to date: {}".format(current_fare))
    print("Total trip costs are {}".format(current_fare))








main()
