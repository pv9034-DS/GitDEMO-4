📁 Assignment 4: Files, Exceptions, and Errors in Python

This assignment includes two Python programs that demonstrate how to handle files and exceptions in Python.

✅ Task 1: Read a File and Handle Errors
🔹 Problem Statement:

Write a Python program that:

Opens and reads a text file named sample.txt.

Prints its content line by line.

Handles errors gracefully if the file does not exist.

🧠 Concepts Used:

File reading using open()

Exception handling with try-except

Iterating over file lines

📝 Sample Code:
def read_file():
    try:
        with open('sample.txt', 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'sample.txt' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file()

📌 Expected Output:

If sample.txt contains:

Hello, World!
Python is amazing.


Then the output will be:

Hello, World!
Python is amazing.


If the file doesn't exist:

Error: The file 'sample.txt' does not exist.

✅ Task 2: Write and Append Data to a File
🔹 Problem Statement:

Write a Python program that:

Takes user input and writes it to a file named output.txt.

Appends additional data to the same file.

Reads and displays the final content of the file.

🧠 Concepts Used:

Writing to a file ('w' mode)

Appending to a file ('a' mode)

Reading from a file

Exception handling

📝 Sample Code:
# Step 1: Get input from the user and write to 'output.txt'
text_to_write = input("Enter text to write to the file: ")
try:
    with open("output.txt", "w") as file:
        file.write(text_to_write + "\n")
    print("Data successfully written to output.txt.")
except Exception as e:
    print(f"An error occurred while writing: {e}")

# Step 2: Append additional text to the same file
text_to_append = input("\nEnter additional text to append: ")
try:
    with open("output.txt", "a") as file:
        file.write(text_to_append + "\n")
    print("Data successfully appended.")
except Exception as e:
    print(f"An error occurred while appending: {e}")

# Step 3: Read and display the final content of the file
try:
    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"An error occurred while reading: {e}")

📌 Expected Output:
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.

📦 Files Included:

task1_read_file.py

task2_write_append_file.py

sample.txt (for testing Task 1)

README.md (this file)
