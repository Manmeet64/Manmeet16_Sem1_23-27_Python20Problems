'''
Write a Python program to create a class representing a stack data structure.
Include methods for pushing and popping elements.
'''

# Class definition for a stack
class Stack:

    # Initialize the stack with an empty list
    def __init__(self):
        self.items = []

    # Add an item to the top of the stack
    def push(self, item):
        print("Item pushed into stack!")
        self.items.append(item)  # Append item to the end of the list

    # Remove and return the top item from the stack
    def pop(self):
        if len(self.items) == 0:
            print("\nStack is empty. Cannot pop from an empty stack.\n")
            return None  # Return None if stack is empty
        else:
            return self.items.pop()  # Remove and return the last item

    # Return the number of items in the stack
    def size(self):
        return len(self.items)

    # Print the elements of the stack
    def print_stack(self):
        print("Stack elements: ", end=" ")
        print(self.items)

# Main function to create a stack and provide a user interface
def main():
    # Create an instance of the Stack class
    my_stack = Stack()

    while True:  # Continuous loop for user interaction
        print("\n1) Push element")
        print("2) Pop element")
        print("3) Check size of stack")
        print("4) View Stack")
        print("5) Exit program\n")

        # Get user's choice and validate input
        choice = int(input("Enter choice: "))
        while True:
            if 1 <= choice <= 5:
                break  # Exit loop if choice is valid
            else:
                print("Invalid choice...Enter again")
                choice = int(input("Enter choice: "))

        # Perform actions based on user's choice
        if choice == 1:
            val = int(input("Enter the value to be pushed into the stack: "))
            my_stack.push(val)
        elif choice == 2:
            popped_element = my_stack.pop()
            if popped_element is not None:
                print(f"{popped_element} popped from stack!")
        elif choice == 3:
            print("Stack size:", my_stack.size())
        elif choice == 4:
            my_stack.print_stack()
        elif choice == 5:
            print("Exiting program.")
            exit()

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()
