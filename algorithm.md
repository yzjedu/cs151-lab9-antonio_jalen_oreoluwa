# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

Main tasks:
- Getting the list of names you want to use for the 

Purpose:  Gets the file to be read and error checks
Name: get_file
Parameters: none
Return: file_name
Algorithm:
1. Ask user to input the file they want to open
2. while the file does not exist:
   3. Output " Error and please try again"
   4. Prompt user to enter the file again
3. Return file_name

Purpose: Read the names from the file into a list
Name: read_data
Parameters: file_name
Return: data
Algorithm:
1. Open and read the file from file_name
2. Create empty list (values)
2. for line in fd :
   3. line = line.strip()
   4. line = str(line)
   5. values.append(line)
3. Store the values from the file into a list
4. Close file
5. Return values

Purpose: Format and display the seat
Name: seating_arrangement 
Parameters: 
Return: 
Algorithm:
1. 

Purpose: Main function
Name: Main
Parameters: 
Return: 
Algorithm:
1. Call filename
2. Call list
3. Call display