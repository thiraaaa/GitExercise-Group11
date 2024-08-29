class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AccountSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        username = input("Enter a username (3-15 characters, no spaces): ")
        password = input("Enter a password (at least 8 characters): ")

        if self.validate_username(username) and self.validate_password(password):
            new_account = Account(username, password)
            self.accounts.append(new_account)
            print("Account created successfully!")
        else:
            print("Invalid username or password. Please try again.")