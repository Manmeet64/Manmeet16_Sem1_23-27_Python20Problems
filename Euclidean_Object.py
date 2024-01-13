'''
To find the Euclidean distance between two points in a two dimensional space
using class and object
'''

import math  # Import the math module for square root calculation

class Euclidian:
    """
    Class to represent a Euclidean distance calculator.
    """

    def __init__(self, x1, y1, x2, y2):
        """
        Initializes the calculator with coordinates of two points.

        Args:
            x1 (int): x-coordinate of the first point.
            y1 (int): y-coordinate of the first point.
            x2 (int): x-coordinate of the second point.
            y2 (int): y-coordinate of the second point.
        """

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate(self):
        """
        Calculates the Euclidean distance between the two points.

        Returns:
            float: The Euclidean distance between the points.
        """

        # Calculate the squared difference of x-coordinates and y-coordinates
        self.square = ((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)

        # Calculate the Euclidean distance using the square root function
        self.distance = math.sqrt(self.square)

        return self.distance

def main():
    """
    Prompts the user for point coordinates and calculates the Euclidean distance.
    """

    x1 = int(input("Enter point X1: "))
    y1 = int(input("Enter point Y1: "))
    x2 = int(input("Enter point X2: "))
    y2 = int(input("Enter point Y2: "))

    # Create an instance of the Euclidian class
    calc = Euclidian(x1, y1, x2, y2)

    # Calculate and display the Euclidean distance
    print(f"Euclidean distance between ({x1},{y1}) and ({x2},{y2}): {calc.calculate()}")

if __name__ == "__main__":
    """
    Ensures this code runs only when executed directly, not when imported as a module.
    """

    main()  # Call the main function to start the program
