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

First, open your terminal (like Windows CMD or Git Bash) and navigate to the project's directory. You can do this using the `cd` command, for example: `cd path/to/your/project/UFF_ComputerSystems/programming_fundamentals/2025_2/ad2`.

Once you are in the correct directory:

* To **create or add** passwords, run the command: `python encoder.py`
* To **search** for a saved password, run the command: `python decoder.py`
