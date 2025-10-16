# Binary Password Manager

## Objective

This project is an assignment for the Programming Fundamentals course, part of my undergraduate studies in Computer Systems at the Fluminense Federal University (UFF). The requirement is to develop two distinct programs: one to encode and write user-provided passwords to a binary file, and a second to read this file and decode a specific password based on a user-provided key.

## File Descriptions

This project is composed of two main Python scripts:

* **encoder.py**
    * Creates or appends to a binary password file (`passwords.db`). It prompts the user for entries and saves them.

* **decoder.py**
    * Reads the `passwords.db` file and allows the user to search for a password using its reference key.

## How to Run

Follow these steps in your terminal (like Windows CMD or Git Bash).

**1. Navigate to the Project Directory**
First, you need to be inside the folder where the `.py` files are located. Use the `cd` (change directory) command.

*Example:*
```cmd
cd path/to/your/project/UFF_ComputerSystems/programming_fundamentals/2025_2/ad2

2. Run the Desired Script Once you are in the correct directory, run one of the following commands:

    To create or add passwords:
    DOS

python encoder.py

To search for a saved password:
DOS

python decoder.py