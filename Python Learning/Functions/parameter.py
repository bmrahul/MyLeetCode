"""
To specify default values for parameters,
When you call a function and pass an argument to the parameter that has a default value, the function will use that argument instead of the default value.
"""

def greet(name, message='Hello'):
    print(f'{message} {name}')

greet('BM Rahul', 'Hi')