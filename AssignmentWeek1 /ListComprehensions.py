# 1. Given a list of numeric strings, convert them into integers using List Comprehensions.
strings = ["1", "2", "3", "4", "5"]
int_list = [int(x) for x in strings]
print(int_list)     # Output: [1, 2, 3, 4, 5]



# 2. Extract all integers from a list that are greater than 10 using List Comprehensions.
numbers = [1, 5, 13, 4, 16, 7]
greater_than_10 = [n for n in numbers if n > 10]
print(greater_than_10)   # Output: [13, 16]



# 3. Create a list of squares for numbers from 1 to 5 using List Comprehensions.
squares = [x * x for x in range(1, 6)]
print(squares)     # Output: [1, 4, 9, 16, 25]



# 4. Convert a 2D list into a 1D list using List Comprehensions.
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flat_list = [item for row in matrix for item in row]
print(flat_list)    # Output: [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]



# 5. Create a dictionary using dictionary comprehension.
# keys = ['a', 'b', 'c'], values = [1, 2, 3]
keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)     # Output: {'a': 1, 'b': 2, 'c': 3}



# 6. From the dictionary, keep only students with scores > 80 using dictionary comprehension.
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
above_80 = {name: score for name, score in scores.items() if score > 80}
print(above_80)     # Output: {'Alice': 85, 'Charlie': 90}
