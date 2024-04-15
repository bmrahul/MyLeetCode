#  function is a recursive function because it has a call to itself:

def fibonacci(value):
    if value <= 1:
        return value
    else:
        return (fibonacci(value - 1) + fibonacci(value - 2))
    

print("Fibonacci Sequence: ")
for i in range(10):
    print(fibonacci(i))
