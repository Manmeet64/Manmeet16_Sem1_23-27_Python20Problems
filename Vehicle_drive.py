'''
Create a base class called “Vehicle” with a method called “drive.” Implement two
subclasses, “Car” and “Bicycle,” that inherit from “Vehicle” and override the “drive”
method with their own implementations.
'''
# Define a base class for vehicles
class Vehicle:

    # Generic method for driving a vehicle
    def drive(self):
        print("Generic vehicle is being driven.")

# Subclass for cars, inheriting from Vehicle
class Car(Vehicle):

    # Override the drive method to provide a car-specific implementation
    def drive(self):
        print("Car is being driven on the road.")

# Subclass for bicycles, inheriting from Vehicle
class Bicycle(Vehicle):

    # Override the drive method to provide a bicycle-specific implementation
    def drive(self):
        print("Bicycle is being pedaled on the path.")

# Main function to demonstrate vehicle object creation and method calls
def main():
    # Create instances of Vehicle, Car, and Bicycle
    generic_vehicle = Vehicle()
    car = Car()
    bicycle = Bicycle()

    # Call the drive method on each object to see their different behaviors
    generic_vehicle.drive()  # Output: Generic vehicle is being driven.
    car.drive()              # Output: Car is being driven on the road.
    bicycle.drive()         # Output: Bicycle is being pedaled on the path.

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()
