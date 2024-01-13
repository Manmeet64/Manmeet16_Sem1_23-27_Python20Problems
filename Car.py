'''
Create a Python class called “Car” with attributes like make, model, and year.
Then, create an object of the “Car” class and print its details.
'''
# Define a class to represent cars
class Car:

    # Constructor to initialize car attributes
    def __init__(self, make, model, year):
        # Assign the make to the object's attribute
        self.make = make
        # Assign the model to the object's attribute
        self.model = model
        # Assign the year to the object's attribute
        self.year = year

    # Method to display car details in a formatted string
    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

# Main function to demonstrate car object creation and information display
def main():
    # Create two Car objects with different details
    car1 = Car("Rolls-Royce", "Phantom VIII", 2017)
    car2 = Car("Lamborghini", "Sian", 2019)

    # Call the display_details method for each car object to print its information
    car1.display_details()
    car2.display_details()

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()

