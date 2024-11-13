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
   4. Strip any whitespace from the line (e.g., newline characters). 
   5. Convert the line to a string and append it to the names list.
4. Close the file. 
5. Return the names list.

Purpose: Format and display the seat
Name: display_seating_arrangement 
Parameters: names (list)
Return: none
Algorithm:
1. Determine the total number of people using the length of the names list. 
2. Calculate the number of tables needed (each table seats 5 people). 
3. Use a loop to assign each name to a table and seat. 
4. Output the seating arrangement with proper formatting. 

Purpose: Main function
Name: Main
Parameters: none
Return: none
Algorithm:
1. Call get_filename() to get the name of the file. 
2. Call read_data() to read the names from the file and store them in a list. 
3. Call display_seating_arrangement() to display the seating arrangement using the list of names.