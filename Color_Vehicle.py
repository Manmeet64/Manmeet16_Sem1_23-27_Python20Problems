'''
Define a class attribute “color” with a default value white. i.e., Every Vehicle
should be white.
'''
# Define a class to represent vehicles
class Vehicle:

    # Constructor to initialize vehicle attributes
    def __init__(self, make, color="White"):
        # Assign the make to the object's attribute
        self.make = make
        # Assign the color to the object's attribute, using "White" as a default
        self.color = color

    # Method to display vehicle information
    def display_info(self):
        # Print the vehicle make and color in a formatted string
        print(f"Vehicle: {self.color} {self.make}")

# Main function to demonstrate vehicle creation and information display
def main():
    # Create multiple Vehicle objects with different colors
    car1 = Vehicle("Ford")  # Uses default color "White"
    car2 = Vehicle("Porsche", "Blue")
    car3 = Vehicle("Audi", "Grey")
    car4 = Vehicle("Mercedes", "Black")

    # Call the display_info method for each vehicle object
    car1.display_info()
    car2.display_info()
    car3.display_info()
    car4.display_info()

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()
