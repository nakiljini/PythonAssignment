# 1. For loop
# Write a program that takes input from the user and checks if a number is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")



# 2. Reverse a string using a for loop and check if it is a palindrome.
# Strings = “civic”, “hello”

s = input("Enter a string: ")
reversed_string = ""

for ch in s:
    reversed_string = ch + reversed_string

print("Reversed String:", reversed_string)

if s == reversed_string:
    print("Palindrome")
else:
    print("Not a Palindrome")



# 3. Generate the first N numbers of the Fibonacci sequence using input from the user.

n = int(input("Enter N for Fibonacci sequence: "))
a, b = 0, 1

print("Fibonacci Sequence:")
for i in range(n):
    print(a)
    a, b = b, a + b



# 4. From list [1,2,3,4,5], find two values whose sum is 9.
# Expected output: [4, 5]

lst = [1, 2, 3, 4, 5]

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == 9:
            print([lst[i], lst[j]])



# ------------------ WHILE LOOP ------------------

# 5. Print all even numbers between 1 and 20 using a while loop.

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1



# ------------------ BREAK ------------------

# 6. Find the first occurrence of a number in a list and stop further searching.
# numbers = [10, 20, 30, 40, 50]
# search_for = 30

numbers = [10, 20, 30, 40, 50]
search_for = 30

for num in numbers:
    if num == search_for:
        print("Found:", num)
        break



# ------------------ CONTINUE ------------------

# 7. Print only odd numbers from 1 to 10 using continue.

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)



# ------------------ PASS ------------------

# 8. What will be the output?

for i in range(5):
    if i == 3:
        pass
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4



# ------------------ MATCH CASE ------------------

# 9. Match Case
# Write a program that takes a day of the week as input and prints whether it's a weekday or weekend.

day = input("Enter day of the week: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")
