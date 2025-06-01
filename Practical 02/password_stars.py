MIN_LENGTH = 8
def main():
    """Main Function to coordinate password input and display"""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Prompt the user to enter a password and validate its length"""
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f'Password must be at least {MIN_LENGTH} characters long')
        password = input("Enter password: ")
    return password
def print_asterisks(password):
    """Print a line of asteriks equal in length to the password."""
    print('*' * len(password))

main()