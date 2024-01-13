'''
Create a Bus child class that inherits from the Vehicle class. The default fare
charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we
need to add an extra 10% on full fare as a maintenance charge. So total fare for
bus instance will become the final amount = total fare + 10% of the total fare.
'''

# Base class for vehicles
class Vehicle:

    # Constructor to initialize seating capacity
    def __init__(self):
        self.seating_capacity = 0

    # Calculate rent based on seating capacity
    def calculate_rent(self):
        rent = self.seating_capacity * 100
        return rent

# Class for bikes, inheriting from Vehicle
class Bike(Vehicle):

    # Set seating capacity to 2 for bikes
    def __init__(self):
        self.seating_capacity = 2

    # Use parent class's method for rent calculation
    def calculate_rent(self):
        return super().calculate_rent()

# Class for 4-seater cars, inheriting from Vehicle
class Car4Seater(Vehicle):

    # Set seating capacity to 4 for cars
    def __init__(self):
        self.seating_capacity = 4

    # Use parent class's method for rent calculation
    def calculate_rent(self):
        return super().calculate_rent()

# Class for buses, inheriting from Vehicle
class Bus(Vehicle):

    # Constructor to initialize seating capacity based on user input
    def __init__(self, seats):
        self.seating_capacity = seats

    # Calculate rent with a 10% surcharge for buses
    def calculate_rent(self):
        rent =  (self.seating_capacity * 100) + 0.1 * (self.seating_capacity * 100)
        return rent

# Main function to demonstrate vehicle rent calculations
def main():
    bike = Bike()
    rent = bike.calculate_rent()
    print(f"Rent of bike: {rent}")

    car = Car4Seater()
    rent = car.calculate_rent()
    print(f"Rent of car: {rent}")

    seats = int(input("Enter no. of seats in bus: "))
    bus = Bus(seats)
    rent = bus.calculate_rent()
    print(f"Rent of Bus: {rent}")

# Call the main function to start the program
main()
