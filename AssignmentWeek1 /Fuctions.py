# 1. Define a function calculate_area that calculates the area of a rectangle
# and returns the result. If no width is provided, it defaults to 10.

def calculate_area(length, width=10):
    return length * width

# Example:
print(calculate_area(5))          # width default = 10 → Output: 50
print(calculate_area(5, 4))       # Output: 20



# 2. Write a recursive function to compute the factorial of a non-negative integer.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example:
print(factorial(5))   # Output: 120



# 3. Write a function that takes one parameter as a string, reverses it, and returns the result.

def reverse_string(s):
    reversed_value = ""
    for ch in s:
        reversed_value = ch + reversed_value
    return reversed_value

# Example:
print(reverse_string("hello"))   # Output: "olleh"



# 4. Write a Python function that takes two parameters as lists
# and returns the sum of all the numbers in both lists combined.
# a = [8, 2, 3, 0, 7]   b = [3, -2, 5, 1]

def sum_two_lists(list1, list2):
    return sum(list1) + sum(list2)

a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]

print(sum_two_lists(a, b))   # Output: 27



# 5. Write a Python function that takes a list and returns a new list
# with distinct and sorted elements.
# a = [4,1,2,3,3,1,3,4,5,1,7]
# Output = [1,2,3,4,5,7]

def distinct_sorted_list(lst):
    return sorted(set(lst))

a = [4,1,2,3,3,1,3,4,5,1,7]
print(distinct_sorted_list(a))   # Output: [1, 2, 3, 4, 5, 7]
