'''
Write a Python program to create a class representing a shopping cart. Include
methods for adding and removing items, and calculating the total price.
'''
# Class definition for a shopping cart
class ShoppingCart:

    # Initialize the cart with an empty list
    def __init__(self):
        self.cart = []

    # Add an item to the cart
    def add_items(self):
        item = input("Enter the name of the item you want to add: ").capitalize()
        quantity = int(input("How many would you like: "))
        price = float(input("Enter price of item: Rs."))
        self.cart.append({'item': item, 'quantity': quantity, 'price': price})

    # Remove an item from the cart
    def remove_items(self):
        if len(self.cart) == 0:  # Check if the cart is empty
            print("Your cart is empty.")
        else:
            print("\nItems in your shopping cart:\n")
            for i in range(len(self.cart)):
                print(f"{i+1}. {self.cart[i]['item']} - Rs.{self.cart[i]['price']} ({self.cart[i]['quantity']})")

            selection = int(input('\nEnter number of item you wish to remove: '))
            if 1 <= selection <= len(self.cart):  # Validate user input
                del self.cart[selection - 1]  # Remove the selected item
            elif selection == 0:
                self.clear_cart()  # Clear the entire cart if selected

    # Clear all items from the cart
    def clear_cart(self):
        self.cart.clear()

    # Display the items in the cart
    def view_cart(self):
        if len(self.cart) == 0:
            print("Your cart is empty.")
        else:
            for i in range(len(self.cart)):
                print(f"{i+1}. {self.cart[i]['item']} - Rs.{self.cart[i]['price']} ({self.cart[i]['quantity']})")

    # Calculate the total price of items in the cart
    def calculate_price(self):
        total = sum([item['price'] * item['quantity'] for item in self.cart])
        return total

# Main function to create a ShoppingCart object and provide a user interface
def main():
    shop = ShoppingCart()  # Create a ShoppingCart instance

    while True:  # Continuous loop for user interaction
        print("\n1)Add Items")
        print("2)Remove Items")
        print("3)Clear Cart")
        print("4)View Cart")
        print("5)Calculate Price")
        print("6)Checkout")
        print('7)Exit shop\n')

        choice = int(input("What do you want to do? "))  # Get user's choice

        if choice == 1:
            shop.add_items()  # Add items to the cart
        elif choice == 2:
            shop.remove_items()  # Remove items from the cart
        elif choice == 3:
            shop.clear_cart()  # Clear the cart
        elif choice == 4:
            shop.view_cart()  # View the cart contents
        elif choice == 5:
            print("Total:", shop.calculate_price())  # Display the total price
        elif choice == 6:
            print(f"Checking out...\nRs. {shop.calculate_price()} credited from your account\nYour items will be delivered shortly.")
            shop.clear_cart()  # Clear the cart after checkout
        elif choice == 7:
            exit()  # Exit the program
        else:
            print("Invalid choice")  # Handle invalid input

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()
