from prac_08.silver_service_taxi import SilverServiceTaxi

car_name = SilverServiceTaxi("holden", 100, 2)
car_name.drive(18)
print(car_name.get_fare())

print(car_name)