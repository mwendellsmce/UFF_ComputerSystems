# File constant
FILE_NAME = 'passwords.db'
file_mode = 'wb'  # Default mode: 'wb' (write binary), creates a new file

try:
    # Tries to open the file to test its existence. Raises an error if it doesn't exist.
    with open(FILE_NAME, 'rb'):
        pass  # The file exists, now let's decide what to do.

        response = input(
            f"The file '{FILE_NAME}' already exists. Do you want to add new passwords (y) or create a new file (n)? ").lower()
        if response == 'y':
            file_mode = 'ab'  # Mode 'append binary' to add to the end of the file

except FileNotFoundError:
    # If the file doesn't exist, this block is skipped, keeping the default 'wb' mode.
    pass

# Data collection
num_passwords_str = input("\nEnter the number of new passwords you would like to store: ")
num_passwords = int(num_passwords_str)

references = []
passwords = []

# Collect references
print("\n--- Phase 1: Enter all references ---")
for i in range(num_passwords):
    ref = input(f"Enter reference {i + 1}/{num_passwords}: ")
    references.append(ref)

# Collect the password for each reference
print("\n--- Phase 2: Enter the password for each reference ---")
for ref in references:
    password = input(f"Enter the password for '{ref}': ")
    passwords.append(password)

# Write to file
with open(FILE_NAME, file_mode) as file:
    for ref, password in zip(references, passwords):
        ref_bytes = ref.encode('utf-8')
        password_bytes = password.encode('utf-8')

        file.write(ref_bytes)
        file.write(b'\n')
        file.write(password_bytes)
        file.write(b'\n')

print(f"\n{num_passwords} new passwords were successfully saved to '{FILE_NAME}'.")