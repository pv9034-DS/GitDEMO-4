# Task 2: Write and Append Data to a File

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
