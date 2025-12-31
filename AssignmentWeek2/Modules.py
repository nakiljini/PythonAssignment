from datetime import datetime, timedelta
import os

# 1. Using datetime, add a week and 12 hours to a date. Given date: March 22, 2020, at 10:00 AM. 
# Print original date time and new date time
original_date = datetime(2020, 3, 22, 10, 0, 0)
new_date = original_date + timedelta(weeks=1, hours=12)
print(f"Original date time: {original_date.strftime('%B %d, %Y, at %I:%M %p')}")
print(f"New date time: {new_date.strftime('%B %d, %Y, at %I:%M %p')}")



# 2. Code to get the dates of yesterday, today, and tomorrow.
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")



# 3. Write a code snippet using os module, to get the current working directory and print and create a folder "test". 
# List all the files and folders in the current working directory and remove the directory "test" that was created.
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Create folder "test"
test_folder = os.path.join(current_dir, "test")
if not os.path.exists(test_folder):
    os.makedirs(test_folder)
    print("Folder 'test' created successfully")

# List all files and folders in current working directory
print("\nFiles and folders in current directory:")
for item in os.listdir(current_dir):
    item_path = os.path.join(current_dir, item)
    if os.path.isdir(item_path):
        print(f"  [DIR] {item}")
    else:
        print(f"  [FILE] {item}")

# Remove the directory "test"
if os.path.exists(test_folder):
    os.rmdir(test_folder)
    print("\nFolder 'test' removed successfully")



# 4. Write a Python program to rename a file from old_name.txt to new_name.txt.
old_filename = "old_name.txt"
new_filename = "new_name.txt"

# Create a sample file if it doesn't exist
if not os.path.exists(old_filename):
    with open(old_filename, 'w') as f:
        f.write("Sample content")

# Rename the file
if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
    print(f"File renamed from '{old_filename}' to '{new_filename}'")
    
    # Optionally rename it back for demonstration
    # os.rename(new_filename, old_filename)



# 5. Create a file and Write a Python program to get the size of a file named example.txt
filename = "example.txt"

# Create a sample file if it doesn't exist
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("This is a sample file for demonstration purposes.")

# Get the size of the file
if os.path.exists(filename):
    file_size = os.path.getsize(filename)
    print(f"Size of '{filename}': {file_size} bytes")



# 6. Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
date_string = "Feb 25 2020 4:20PM"
date_obj = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(f"Converted datetime object: {date_obj}")



# 7. Subtract 7 days from the date 2025-02-25 and print the result.
date = datetime(2025, 2, 25)
new_date = date - timedelta(days=7)
print(f"New date: {new_date.strftime('%Y-%m-%d')}")



# 8. Format the date 2020-02-25 as "Tuesday 25 February 2020"
date = datetime(2020, 2, 25)
formatted_date = date.strftime("%A %d %B %Y")
print(f"Formatted date: {formatted_date}")

