# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...


Purpose:  Gets the file to be read and error checks
Name: get_filename()
Parameters: none
Return: file_name
Algorithm:
1. Ask the user to input the name of the file they want to open.
2. While the file does not exist:
   3. Output " Error and please try again"
   4. Prompt user to enter the file again
3. Once a valid filename is provided, return the file_name.

Purpose: Read the names from the file into a list
Name: read_names
Parameters: file_name
Return: names
Algorithm:
1. Open the file specified by file_name for reading. 
2. Create an empty list names. 
3. For each line in the file:
   1. Strip any whitespace from the line (e.g., newline characters). 
   2. Append each line to the names list.
4. Close the file. 
5. Return the names list.

Purpose: Format and display the seat
Name: display_seating_arrangement 
Parameters: names (list)
Return: none
Algorithm:
1. Determine the total number of people using the length of the names list.
2. Store this in a variable called total_people.
3. Divide the total number of people by 5 to determine how many tables are required.
4. For each name in the list:
   1. Output the seating assignment in the right format
   2. Increment the seat number by 1 (current_seat += 1). 
   3. If the seat number exceeds 5 :
      1. Reset the seat number to 1 and increment the table number by 1 (current_table += 1). 
5. Output the seating arrangement with proper formatting. 

Purpose: Main function
Name: Main
Parameters: none
Return: none
Algorithm:
1. Output Welcome message
2. Call get_filename() to get the name of the file. 
3. Call read_data() to read the names from the file and store them in a list. 
4. Call display_seating_arrangement() to display the seating arrangement using the list of names.
5. Output Goodbye message