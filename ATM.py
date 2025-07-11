import random
# ATM Machine Simulation

class ATM:
    # ATM class to handle balance, deposit, and withdraw operations.
    def __init__(self):
        # Initialize balance to zero
        self.balance = 0

    def check_balance(self):
        # Returns the current balance.
        return self.balance

    def deposit(self, amount):

        # Deposits a positive amount to the balance.
        # Raises ValueError if amount is not positive.

        if amount <= 0:
            raise ValueError('The amount should be +ve.')
        self.balance += amount

    def withdraw(self, amount):
    
        # Withdraws a positive amount from the balance if sufficient funds exist.
        # Raises ValueError if amount is not positive or exceeds balance.
        
        if amount <= 0:
            raise ValueError('The withdraw amount should be +ve.')
        if amount > self.balance:
            raise ValueError('Invalid amount..')
        self.balance -= amount

               

class ATMcontroller:

    # Controller class to interact with the user and ATM class.
    
    def __init__(self):
        # Create an instance of ATM
        self.atm = ATM()
    
    def gen_opt(self):
        OTP=random.randint(100000, 999999) #Generate the otp with 6 digit
        print("Your OTP is : ",OTP) #diplay the otp
        while True:
            user_otp=int(input("Enter the OTP : ")) 
            if user_otp==OTP:
                print('\nWelcome to the ATM!')
                break
            else:
                print("Invalid OTP")
        
        # Prompts the user for a number input and validates it.
    def get_number(self,prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print('Invalid number..')

    def display_menu(self):
        
        # Displays the ATM menu options.
    
        
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

    def check_balance(self):
        
        # Prints the current balance.
        
        balance = self.atm.check_balance()
        print(f'The balance amount is : ${balance}')

    def deposit(self):
        
        # Handles deposit operation with input validation.
        
        while True:
            try:
                amount = self.get_number('Enter the amount for deposit : ')
                self.atm.deposit(amount)
                print(f'Successfully deposited amount : ${amount}.')
                break
            except ValueError as error:
                print(error)

    def withdraw(self):
        
        # Handles withdraw operation with input validation.
        
        while True:
            try:
                amount = self.get_number('Enter the amount for withdraw : ')
                self.atm.withdraw(amount)
                print(f'Successfully withdrew amount : ${amount}.')
                break
            except ValueError as error:
                print(error)

    def run(self):
        
        self.gen_opt()  #Call the otp for verification

        # Runs the ATM menu loop and handles user choices.
        
        while True:
            self.display_menu()
            user_input = input('Enter the option : ')
            if user_input == '1':
                self.check_balance()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                print('Thank you for visiting ATM.')
                # print('self.deposit')
                # print('self.withdraw')
                break
            else:
                print('Invalid option..')

def main():
    
    # Main function to start the ATM controller.
    
    atm = ATMcontroller()
    atm.run()

if __name__ == "__main__":
    main()

