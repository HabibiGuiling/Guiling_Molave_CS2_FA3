def main():
    """Prompts the user to enter a password and checks if the length is valid."""
    while True:
        password = input("Enter your password: ")

        """Assigns the password variable value to check_password_length and runs the code below if the function returns True."""
        if check_password_length(password):
            print("Password length is valid.")
            break
        else:
            print("Password length is too short or too long. Please try again.")

"""Checks the length of the password."""
def check_password_length(password):
    password_length = len(password)

    """Returns True if the password length is between 8 and 15 characters."""
    if password_length >= 8 and password_length <= 15:
        return True
    else:
        return False

main()


