'''
Write a Python program to create a class representing a bank. Include methods for
managing customer accounts and transactions.
'''
# Class definition for a bank
class Bank:

    # Initialize the bank with an empty dictionary to store accounts
    def __init__(self):
        self.accounts = {}

    # Create a new account with the given account number and initial balance
    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:  # Check if the account already exists
            self.accounts[account_number] = initial_balance  # Add the account to the dictionary
            print(f"Account created successfully for account number {account_number} with initial balance {initial_balance}.")
        else:
            print(f"Account with account number {account_number} already exists.")

    # Get the balance for a specific account
    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]  # Return the balance
        else:
            print(f"Account with account number {account_number} does not exist.")
            return None

    # Deposit money into a specific account
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount  # Update the balance
            print(f"Deposited {amount} into account number {account_number}. New balance: {self.accounts[account_number]}.")
        else:
            print(f"Account with account number {account_number} does not exist.")

    # Withdraw money from a specific account
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:  # Check for sufficient funds
                self.accounts[account_number] -= amount  # Update the balance
                print(f"Withdrew {amount} from account number {account_number}. New balance: {self.accounts[account_number]}.")
            else:
                print(f"Insufficient funds in account number {account_number}.")
        else:
            print(f"Account with account number {account_number} does not exist.")

# Main function to demonstrate bank operations
def main():
    my_bank = Bank()  # Create a Bank object

    my_bank.create_account(1001, 500)
    my_bank.create_account(1002, 12000)

    my_bank.deposit(1001, 200)
    my_bank.withdraw(1002, 300)

    print(f"Balance in account 1001: {my_bank.get_balance(1001)}")

    # Print the final balances of all accounts
    print("Final account balances:")
    for acc_num, balance in my_bank.accounts.items():
        print(f"Account number: {acc_num}   Balance: {balance}")

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()
