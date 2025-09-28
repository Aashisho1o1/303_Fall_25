import string
import datetime

# Caesar Cipher Functions
def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded_text = ""
   
   
    for char in input_text:
        if char.lower() in alphabet:
            # Finding the index of the character in alphabet
            old_index = alphabet.index(char.lower())
            # Calculate neew index with shift (wrapping around)
            new_index = (old_index + shift) % 26
            # Always output lowercase for encoded text
            encoded_text += alphabet[new_index]
        else:
            # Non-alphabetic characters remain unchanged
            encoded_text += char
    
    return (alphabet, encoded_text)

def decode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    decoded_text = ""
    
    for char in input_text:
        if char.lower() in alphabet:
            # Find the index of the character in alphabet
            old_index = alphabet.index(char.lower())
            # Calculate original index by subtracting shift (wrapping around)
            new_index = (old_index - shift) % 26
            # Get the original character and preserve original case
            if char.isupper():
                decoded_text += alphabet[new_index].upper()
            else:
                decoded_text += alphabet[new_index]
        else:
            # Non-alphabetic characters remain unchanged
            decoded_text += char
    
    return decoded_text

# Bank Account Classes
class BankAccount:
    """Base bank account class"""
    
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        self.name = name
        self.ID = ID
        
        # Handle creation_date
        if creation_date is None:
            self.creation_date = datetime.date.today()
        else:
            # Check if creation_date is in the future
            if creation_date > datetime.date.today():
                raise Exception("Creation date cannot be in the future")
            self.creation_date = creation_date
            
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money to the account"""
        if amount < 0:
            return  # Negative deposits not allowed
        self.balance += amount
        print(f"Balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        self.balance -= amount
        print(f"Balance: ${self.balance}")
    
    def view_balance(self):
        """View current account balance"""
        print(f"Balance: ${self.balance}")
        return self.balance

class SavingsAccount(BankAccount):
    """Savings account with additional restrictions"""
    
    def withdraw(self, amount):
        """Withdraw with savings account rules"""
        # Check if account has been open for at least 180 days
        days_since_creation = (datetime.date.today() - self.creation_date).days
        if days_since_creation < 180:
            print(f"Balance: ${self.balance}")
            return  # Can't withdraw before 180 days
        
        # Check for overdraft
        if self.balance - amount < 0:
            print(f"Balance: ${self.balance}")
            return  # Overdrafts not permitted
        
        # Proceed with withdrawal
        self.balance -= amount
        print(f"Balance: ${self.balance}")

class CheckingAccount(BankAccount):
    """Checking account with overdraft fees"""
    
    def withdraw(self, amount):
        """Withdraw with overdraft fees"""
        original_balance = self.balance
        self.balance -= amount
        
        # If withdrawal results in negative balance, charge $30 fee
        if original_balance >= 0 and self.balance < 0:
            self.balance -= 30
        
        print(f"Balance: ${self.balance}")