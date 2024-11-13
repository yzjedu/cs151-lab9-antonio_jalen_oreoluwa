# Programmers: Oreoluwa Adebusoye, Jalen, Antonio Dueno
# Course: CS151, Zelalem Yalew
# Due Date: 11/13
# Programming Assignment: Lab 09
# Problem Statement: Create a program that will organize a seating plan for a list of names in a file.
# Data In: User inputs which file containing a list of names they wish to assign seats to
# Data Out: Program outputs list of tables and seats and who will be seating at each.
# Credits: Lecture note codes 10 and 11

import os

# Purpose: Prompts the user for a valid file name and ensures it exists.
# Name: read_filename
# Parameters: None
# Return: The valid file name entered by the user
def read_filename():
    # Prompt user for the filename to read
    file_name = (input("What file do you want to read? "))

    # Check if the file exists, and if not, ask again until a valid file is entered
    while not os.path.isfile(file_name):
        print("That file does not exist. Please try again.")
        file_name = (input("\nWhat file do you want to read? "))

    # Return the file name if it exists
    return file_name


# Purpose: Reads the names from the file and stores them in a list.
# Name: read_file_to_list
# Parameters: file_name (str)
# Return: A list of names (str) from the file.
def read_file_to_list(file_name):
    names = []
    try:
        # Open the file for reading
        file_data = open(file_name, 'r')

        # Read each line into the list
        for line in file_data:
            line = line.strip()  # Remove any whitespace/newline
            if line:  # Ensure the line is not empty
                names.append(line)

        # Close the file after reading
        file_data.close()

        # Return the list of data
        return names
    except:
        # Ensure the file is closed in case of an error
        file_data.close()

        # Print an error message and return an empty list
        print("Error reading file")

        return names # Return the empty list


# Purpose: Formats and displays the seating arrangement for each name.
# Name: display_seating_arrangement
# Parameters:  names (list)- The list of names to assign to tables and seats.
# Return: None
def display_seating_arrangement(names):
    total_people = len(names)

    people_per_table = 5
    total_tables = total_people // people_per_table

    print(f"\nTotal tables needed: {total_tables}\n")

    current_table = 1
    current_seat = 1

    # Iterate through the names and assign them to seats and tables
    for name in names:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Table {current_table}, Seat {current_seat}, {name}")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~")

        # Move to the next seat
        current_seat += 1

        # If the table reaches 6 seats, reset seat to 1 and increment table number
        if current_seat > people_per_table:
            current_seat = 1
            current_table += 1


# Purpose: Coordinates the program flow.
# Name: main
# Parameters: None
# Return: None
def main():
    # Get the filename from the user
    file_name = read_filename()

    # Read the names from the file and store them in a list
    names = read_file_to_list(file_name)

    # Display the seating arrangement
    display_seating_arrangement(names)


# Run the main program if this file is executed
main()