import csv

# 1. Write a Python program to read the entire content of a file named sample.txt and display it.
try:
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File 'sample.txt' not found. Please create the file first.")



# 2. Write a Python program to count the number of words in a file named words.txt
try:
    with open('words.txt', 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"Number of words in words.txt: {word_count}")
except FileNotFoundError:
    print("File 'words.txt' not found. Please create the file first.")



# 3. Create a program to write the string "Hello, Python!" into a file named output.txt.
with open('output.txt', 'w') as file:
    file.write("Hello, Python!")
print("Content written to output.txt successfully")



# 4. Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. 
# Add at least three entries
data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV file 'students.csv' created successfully")



# 5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.
def read_file_generator(filename):
    """Generator function to read file line by line"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please create the file first.")

# Example usage:
# Assuming a file named 'large_file.txt' with 100+ lines exists
filename = 'large_file.txt'
line_generator = read_file_generator(filename)

# Fetch all data from the file using the generator
all_lines = []
for line in line_generator:
    all_lines.append(line)

print(f"Total lines read: {len(all_lines)}")
# To print all lines, uncomment the following:
# for line in all_lines:
#     print(line)

