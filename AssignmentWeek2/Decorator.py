import time
from functools import wraps

# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function 
# to calculate the start and end time. Calculate the total time taken and print.
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total time taken: {total_time:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)
    return numbers

append_numbers()



# 2. Create a parameterised decorator retry that retries a function a specified number of times.
def retry(max_attempts):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise e
                    print(f"Attempt {attempt} failed. Retrying...")
            return None
        return wrapper
    return decorator

@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("World")



# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x <= 0:
            raise ValueError("Argument must be positive")
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

# Example:
print(square_root(16))     # Output: 4.0
# print(square_root(-4))   # Would raise ValueError



# 4. Create a decorator cache that caches the result of a function based on its arguments.
def cache(func):
    cache_dict = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        if key in cache_dict:
            print("Returning cached result...")
            return cache_dict[key]
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result
    return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x

expensive_computation(5)
expensive_computation(5)



# 5. Create a decorator requires_permission that checks if a user has the 'admin' permission 
# before allowing access to a function, if a different user then responds "Access denied".
def requires_permission(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if 'admin' not in user.get('permissions', []):
            print("Access denied")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 123)     # Access granted
delete_user(user2, 456)     # Access denied
delete_user(user3, 789)     # Access denied

