
# Define a base class for shoes
class Shoe:

    # Constructor to initialize color and brand
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    # Method to add a shoe to the store (will be overridden in subclasses)
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} shoes added to store!")

# Define a class for Converse shoes, inheriting from Shoe
class Converse(Shoe):

    # Constructor to initialize color, top style, and tongue color
    def __init__(self, color, lowOrHighTop, tongueColor):
        # Call the parent class constructor with brand set to "Converse"
        super().__init__(color, brand="Converse")
        self.lowOrHighTop = lowOrHighTop
        self.tongueColor = tongueColor

    # Override the add_shoe method to include Converse-specific details
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.lowOrHighTop}-top {shoeType.tongueColor} tongue-color {self.brand} added to store!")

# Define a class for combat shoes, inheriting from Shoe
class CombatShoe(Shoe):

    # Constructor to initialize color, brand, military branch, and camouflage type
    def __init__(self, color, brand, militiaryBranch, jungleOrDesert):
        super().__init__(color, brand)
        self.militiaryBranch = militiaryBranch
        self.jungleOrDesert = jungleOrDesert

    # Override the add_shoe method to include combat shoe-specific details
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} {self.militiaryBranch} {self.jungleOrDesert}-camo combat boots added to store")

# Define a class for sandals, inheriting from Shoe
class Sandal(Shoe):

    # Constructor to initialize color, brand, toe type, and waterproof status
    def __init__(self, color, brand, openOrClosedToe, waterproof):
        super().__init__(color, brand)
        self.openOrClosedToe = openOrClosedToe
        self.waterproof = waterproof

    # Override the add_shoe method to include sandal-specific details
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} {self.openOrClosedToe}-toe {self.waterproof} sandals added to store!")

# Main function to simulate a shoe store admin interface
def main():
    print("----WELCOME TO THE SHOE-STOP(Admin Side)----")

    while True:
        # Present a menu of shoe categories
        print("\n\n1)Regular Shoes")
        print("2)Converse Shoes")
        print("3)Combat Shoes")
        print("4)Sandals")
        choice = int(input("\nWhat do you want to add: "))

        # Handle user's choice and create appropriate shoe objects
        if choice == 1:
            # Get details for regular shoes
            color = input("\nEnter color of shoe: ").capitalize()
            brand = input("Enter brand: ").capitalize()
            shoe = Shoe(color, brand)
            shoe.add_shoe(shoe)

        elif choice == 2:
            # Get details for Converse shoes
            print("\nWelcome to the Converse section!\n")
            color = input("Enter color of converse: ").capitalize()
            low_or_high = input("Is it Low or High Top? (Type 'Low' or 'High'): ").capitalize()
            tongue_col = input("What is the color of Tongue? (Type 'Blue', 'Green', 'Red', 'Yellow', 'Black': ").capitalize()
            converse = Converse(color, low_or_high, tongue_col)
            converse.add_shoe(converse)

        elif choice == 3:
            # Get details for combat shoes
            print("\nWelcome to Combat Shoes Section!\n")
            color = input("Enter color of combat shoe: ")
