# 1. Using below list and enumerate(), print index followed by value.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry



# 2. Using below dict and enumerate, print key followed by value
person = {"name": "Alice", "age": 30, "city": "New York"}
for index, (key, value) in enumerate(person.items()):
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 30
# city: New York



# 3. Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], 
# use enumerate() to create a list of tuples where each tuple contains the index and 
# the corresponding fruit, but only for even indices.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
even_indices = [(index, fruit) for index, fruit in enumerate(fruits) if index % 2 == 0]
print(even_indices)

# Output:
# [(0, 'apple'), (2, 'cherry'), (4, 'elderberry')]

