# 1. Given a list, let's see how to double each element of the given list. Using map()
a = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, a))
print(doubled)     # Expected Output: [2, 4, 6, 8]



# 2. Use filter() and lambda to extract all even numbers from a list of integers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)     # Expected Output: [2, 4, 6, 8, 10]



# 3. Use reduce() and lambda to find the longest word in a list of strings.
from functools import reduce

words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest_word)     # Expected Output: 'banana'



# 4. Use map() to square each number in the list and round the result to one decimal place.
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
squared_rounded = list(map(lambda x: round(x * x, 1), my_floats))
print(squared_rounded)     # Expected Output: [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]



# 5. Use filter() to select names with 7 or fewer characters from the list.
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
short_names = list(filter(lambda name: len(name) <= 7, my_names))
print(short_names)     # Expected Output: ['olumide', 'josiah', 'omoseun']



# 6. Use reduce() to calculate the sum of all numbers in a list.
from functools import reduce

numbers_sum = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers_sum)
print(sum_result)     # Expected Output: 15


