# 1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
# Of 10 numbers
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generate first 10 Fibonacci numbers
fib = fibonacci_generator()
for i in range(10):
    print(next(fib))

# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34



# 2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.
def infinite_multiples(n):
    current = n
    while True:
        yield current
        current += n

# Input n=3
multiples = infinite_multiples(3)
for i in range(5):
    print(next(multiples))

# Output:
# 3
# 6
# 9
# 12
# 15
# ...



# 3. Write a generator function called repeat_word(word, times) that yields the given word a specified number of times.
def repeat_word(word, times):
    for i in range(times):
        yield word

# word = "hello"
# times = 5
word = "hello"
times = 5
for repeated_word in repeat_word(word, times):
    print(repeated_word)

