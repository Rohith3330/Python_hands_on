def authenticate(username, password):
    predefined_username = username
    predefined_password = password
    
    # Continuously prompt users for authentication
    while True:
        # Prompt user to enter username and password
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        
        if input_username == predefined_username and input_password == predefined_password:
            print("Welcome, {}!".format(username))
            break  # Break out of the loop if authentication is successful
        else:
            print("Invalid credentials. Please try again.")
            choice = input("Enter 'exit' to quit or press Enter to try again: ")
            if choice.lower() == 'exit':
                break  # Break out of the loop if the user chooses to exit

def main():
    # Define predefined username and password
    username = "user123"
    password = "1234"

    # Call the authentication function
    authenticate(username, password)
if __name__ == "__main__":
    main()