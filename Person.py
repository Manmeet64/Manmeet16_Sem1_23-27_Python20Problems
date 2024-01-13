'''
Write a Python program to create a person class. Include attributes like name,
country and date of birth. Implement a method to determine the person's age.
'''

import time  # Import the time module for date and time functions

# Create a class to represent a person
class Person:

    def __init__(self, name, country, date, month, year):
        """Initialize the person's attributes."""
        self.name = name
        self.country = country
        self.date = date
        self.month = month
        self.year = year

    def calculate_age(self):
        """Calculate the person's age in years and months."""
        current_year, current_month, current_day = time.localtime()[:3]  # Get current date components

        if (current_month, current_day) < (self.month, self.date):
            # If current month/day is before birth month/day, adjust for full year not passing yet
            age_years = current_year - self.year - 1
            age_months = (current_month + 12) - self.month
        else:
            age_years = current_year - self.year
            age_months = current_month - self.month

        return age_years, age_months

# Define the main function
def main():

    # Lists for error checking month and day inputs
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    isLeap = False  # Flag to track leap years

    # Get user input for person's details
    name = input("Enter name: ")
    country = input("Enter country: ")

    # Validate year input
    while True:
        year = int(input("Enter year of birth: "))
        if year > time.localtime().tm_year:
            print("Invalid Year")
        else:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                isLeap = True
            break

    # Validate month input
    while True:
        month = int(input("Enter birth month number: "))
        if month in months:
            break
        else:
            print("Invalid month!")

    # Validate day input
    while True:
        day = int(input("Enter day of birth: "))
        if month in days_31:
            if 1 <= day <= 31:  # Check for valid day range
                break
        elif month in days_30:
            if 1 <= day <= 30:
                break
        elif month == 2:
            if isLeap and 1 <= day <= 29:  # Handle leap year for February
                break
            elif not isLeap and 1 <= day <= 28:
                break
        print(f"Error: Invalid day for month {month}")  # Display error message if invalid

    # Create a Person object
    p2 = Person(name, country, day, month, year)

    # Print the calculated age
    print(f"Age: {p2.calculate_age()[0]} years, {p2.calculate_age()[1]} months")

# Run the main function only if the script is executed directly
if __name__ == "__main__":
    main()
