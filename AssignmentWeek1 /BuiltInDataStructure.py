# 1. Given a list of numbers, find and print the maximum and minimum values.
nums = [1, 2, 3, 4, 5]
print("Maximum:", max(nums))
print("Minimum:", min(nums))



# 2. Given two lists, merge the values from both lists into one and print.
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
merged_list = a + b
print("Merged List:", merged_list)



# 3. From a list, print the number of times the value 3 appears in the list.
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
count_3 = a.count(3)
print("Count of 3:", count_3)



# 4. From the list, sort the list and print.
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
a.sort()
print("Sorted List:", a)



# 5. Given a set, add the element 6 to it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print("Updated Set:", numbers)



# 6. Given a set, remove the element 3 from it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("Set after removing 3:", numbers)



# 7. Given two sets, find and print their intersection.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Intersection:", set1.intersection(set2))



# 8. Given a tuple, count the number of occurrences of 'apple'.
fruits = ('apple', 'banana', 'apple', 'cherry')
count_apple = fruits.count('apple')
print("Count of 'apple':", count_apple)



# 9. Given two tuples, concatenate them and print the result.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Concatenated Tuple:", combined)



# 10. Access and print the value associated with the key "age" from the dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Age:", person["age"])



# 11. Add new key 'gender' to dictionary and assign “M” to it and print.
person = {"name": "Alice", "age": 30, "city": "New York"}
person["gender"] = "M"
print("Updated Dictionary:", person)



# 12. Remove the key "city" from the above dict and print.
person = {"name": "Alice", "age": 30, "city": "New York"}
del person["city"]
print("After Removing 'city':", person)



# 13. Given two dictionaries, merge them into one.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)
