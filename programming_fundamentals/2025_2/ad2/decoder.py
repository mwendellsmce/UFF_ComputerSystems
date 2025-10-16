# File constant
FILE_NAME = 'passwords.db'

saved_passwords = {}

try:
    with open(FILE_NAME, 'rb') as file:
        lines = file.readlines()

        # The loop iterates through the list of lines, skipping 2 at a time (reference, password)
        for i in range(0, len(lines), 2):
            reference = lines[i].decode('utf-8').strip()
            password = lines[i+1].decode('utf-8').strip()
            saved_passwords[reference] = password

    # Continuous user interaction
    while True:
        search_key = input("\nEnter the password reference to search for (or press Enter to exit): ")

        # 1. Check the exit condition first
        if not search_key:
            print("Exiting program.")
            break  # Stops the loop

        # 2. If not exiting, perform the search
        if search_key in saved_passwords:
            found_password = saved_passwords[search_key]
            print(f"Password found for '{search_key}': {found_password}")
        else:
            print(f"The reference '{search_key}' was not found in the database.")

except FileNotFoundError:
    # If 'passwords.db' does not exist, inform the user.
    print(f"Error: The file '{FILE_NAME}' was not found. Please run the encoder.py script first.")
