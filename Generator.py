'''
Define a class with a generator which can iterate the numbers, which are divisible
by 7, between a given range 0 and n.
'''
# Define a class to generate numbers divisible by 7
class Generator:

    # Constructor to initialize an empty list to store generated numbers
    def __init__(self):
        self.numbers = []

    # Method to iterate through numbers and generate those divisible by 7
    def iterate(self, number):
        # Loop through numbers from 0 to the given limit (inclusive)
        for i in range(number + 1):
            # Check if the current number is divisible by 7
            if i % 7 == 0:
                # If divisible, append it to the list of generated numbers
                self.numbers.append(i)
        # Return the list of generated numbers
        return self.numbers

# Main function to demonstrate the Generator class
def main():
    # Create an instance of the Generator class
    gen = Generator()

    # Print a message for the user
    print("Divisibility by 7 checker")

    # Prompt the user to enter a limit
    num = int(input("Enter limit: "))

    # Call the iterate method to generate numbers divisible by 7 up to the limit
    numbers = gen.iterate(num)

    # Print the generated numbers
    print(numbers)

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()
