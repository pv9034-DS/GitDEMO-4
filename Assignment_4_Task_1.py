# Task: Read a file and handle errors
def read_file():
    try:
        # Open the file sample.txt in read mode
        with open('sample.txt', 'r') as file:
            # Read the file line by line
            for line in file:
                print(line.strip())  # Print each line without extra newline
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: The file 'sample.txt' does not exist.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to read the file
read_file()
