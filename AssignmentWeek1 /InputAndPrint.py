# 1. Objective: Ask the user for their name and greet them.
# Task: Write a program that asks the user for their name and then prints a greeting message using their name.

name = input("Enter your name: ")
print("Hello", name, "Welcome to Python Programming!")



# 2. Objective: Perform basic arithmetic operations based on user input.
# Task: Ask the user to enter two numbers and print their sum, multiplication, and division.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_value = num1 + num2
multiply_value = num1 * num2
division_value = num1 / num2  # Assuming user will not input 0

print("Sum:", sum_value)
print("Multiplication:", multiply_value)
print("Division:", division_value)



# 3. Task: Ask the user to enter input names separated by commas,
# split the string using comma and copy to a list, and print.

names = input("Enter names separated by commas: ")
name_list = names.split(",")
print("List of names:", name_list)



# 4. Task: Ask the user to enter their age and check if they are eligible to vote.
# (Voting age is 18 or above)

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")



# 5. For value = 3.14159, using f-string print output with only 2 decimal places.
# Output: 3.14

value = 3.14159
print(f"{value:.2f}")
