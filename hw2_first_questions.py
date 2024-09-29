# 1) Function to triple a value
def triple(x):
    return x * 3

# 2) Function to subtract two values
def subtract(a, b):
    return a - b

# 3) Function to create a dictionary from a list of 2-tuples
def dictionary_maker(tuple_list):
    result = {}
    for key, value in tuple_list:
        result[key] = value
    return result

# Example usage:
print(triple(4))  # Output: 12
print(subtract(10, 5))  # Output: 5
print(dictionary_maker([('foo', 1), ('bar', 3)]))  # Output: {'foo': 1, 'bar': 3}
